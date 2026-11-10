"""Uji unit untuk mesin chatbot (tanpa Flask)."""
from pathlib import Path

import pytest

from chatbot.engine import ChatbotEngine, load_themes, preprocess, similarity

THEMES = load_themes(Path(__file__).resolve().parent.parent / "themes")


def test_preprocess_normalisasi_dan_stopword():
    assert preprocess("Gimana cara isi KRS, kak?") == ["bagaimana", "cara", "isi", "krs"]


def test_similarity_kalimat_sama_bernilai_satu():
    t = ["jadwal", "kuliah"]
    assert similarity(t, t) == 1.0


def test_similarity_kalimat_berbeda_rendah():
    assert similarity(["gudeg"], ["jadwal", "kuliah"]) < 0.3


def test_semua_tema_termuat():
    assert {"kampus", "kuliner", "wisata"} <= set(THEMES)


@pytest.mark.parametrize("theme_id, pesan, intent", [
    ("kampus", "halo", "salam"),
    ("kampus", "kapan pengisian krs?", "krs"),
    ("kampus", "gmn cara bayar UKT", "ukt"),
    ("kampus", "perpustakaan buka jam brp", "perpustakaan"),
    ("kampus", "makasih ya", "terima_kasih"),
    ("kuliner", "gudeg itu apa sih", "gudeg"),
    ("kuliner", "resep nasi goreng dong", "resep_nasi_goreng"),
    ("wisata", "ada apa aja di malioboro", "malioboro"),
    ("wisata", "naik apa keliling jogja", "transportasi"),
])
def test_klasifikasi_intent(theme_id, pesan, intent):
    engine = ChatbotEngine(THEMES[theme_id])
    tag, _ = engine.classify(pesan)
    assert tag == intent


def test_salah_ketik_masih_dikenali():
    engine = ChatbotEngine(THEMES["kampus"])
    tag, _ = engine.classify("jadwl kuliah")
    assert tag == "jadwal_kuliah"


def test_pertanyaan_di_luar_tema_memberi_fallback():
    engine = ChatbotEngine(THEMES["kampus"])
    hasil = engine.reply("siapa pemenang piala dunia")
    assert hasil["intent"] is None
    assert hasil["reply"] in THEMES["kampus"]["fallback"]


def test_placeholder_nama_bot_diganti():
    engine = ChatbotEngine(THEMES["kampus"])
    hasil = engine.reply("kamu siapa")
    assert "{nama_bot}" not in hasil["reply"]
    assert "SiAkad" in hasil["reply"]


def test_explain_mengurutkan_kandidat_dari_skor_tertinggi():
    engine = ChatbotEngine(THEMES["kampus"])
    kandidat = engine.explain("gmn cara bayar UKT")
    assert kandidat[0]["intent"] == "ukt"
    assert kandidat[0]["pattern"] == "cara bayar ukt"
    skor = [k["score"] for k in kandidat]
    assert skor == sorted(skor, reverse=True)


def test_validate_theme_menemukan_kesalahan():
    from chatbot.engine import validate_theme
    rusak = {"id": "x", "name": "X", "bot_name": "B", "avatar": "*", "color": "#000",
             "description": "d", "greeting": "g", "suggestions": [], "fallback": ["f"],
             "intents": [{"tag": "a", "patterns": ["halo"], "responses": ["hai"]},
                         {"tag": "b", "patterns": ["halo"], "responses": []}]}
    masalah = validate_theme(rusak)
    assert any("responses kosong" in m for m in masalah)
    assert any("'a' dan 'b'" in m for m in masalah)


def test_semua_tema_bawaan_valid():
    from chatbot.engine import validate_theme
    for theme in THEMES.values():
        assert validate_theme(theme) == []


def test_akurasi_data_uji_kampus_minimal_90_persen():
    from evaluate import baca_data, evaluasi
    akurasi, _ = evaluasi(THEMES["kampus"], baca_data("kampus"), 0.45)
    assert akurasi >= 0.9
