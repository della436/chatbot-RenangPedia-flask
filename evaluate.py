
"""
Evaluasi akurasi chatbot RenangPedia menggunakan data uji.

File data uji:
    evaluasi/renang.csv

Format CSV:
    kalimat,intent

Jalankan:
    python evaluate.py
    python evaluate.py --tema renangpedia
    python evaluate.py --tema renangpedia --sweep
"""

import argparse
import csv
from collections import Counter
from pathlib import Path

from chatbot import ChatbotEngine, load_themes


BASE_DIR = Path(__file__).resolve().parent


def baca_data(tema):
    path = BASE_DIR / "evaluasi" / f"{tema}.csv"

    if not path.exists():
        raise FileNotFoundError(
            f"File evaluasi tidak ditemukan: {path}"
        )

    with open(path, encoding="utf-8-sig", newline="") as f:
        return [
            (r["kalimat"], r["intent"])
            for r in csv.DictReader(f)
        ]


def evaluasi(theme, data, ambang):
    if not data:
        raise ValueError("Dataset evaluasi masih kosong.")

    bot = ChatbotEngine(theme, ambang)
    hasil = []

    for kalimat, harapan in data:
        tebakan, skor = bot.classify(kalimat)
        tebakan = tebakan or "fallback"
        hasil.append((kalimat, harapan, tebakan, skor))

    benar = sum(
        1 for _, harapan, tebakan, _ in hasil
        if harapan == tebakan
    )

    return benar / len(hasil), hasil


def main():
    parser = argparse.ArgumentParser(
        description="Evaluasi chatbot RenangPedia"
    )

    parser.add_argument(
        "--tema",
        default="renangpedia"
    )

    parser.add_argument(
        "--ambang",
        type=float,
        default=0.45
    )

    parser.add_argument(
        "--sweep",
        action="store_true",
        help="Bandingkan beberapa ambang batas"
    )

    args = parser.parse_args()

    themes = load_themes(BASE_DIR / "themes")

    if args.tema not in themes:
        raise ValueError(
            f"Tema '{args.tema}' tidak ditemukan."
        )

    theme = themes[args.tema]
    data = baca_data(args.tema)

    if args.sweep:
        print(
            f"Tema {args.tema}: {len(data)} kalimat uji\n"
        )

        print("ambang  akurasi")

        for ambang in [
            0.30, 0.35, 0.40, 0.45,
            0.50, 0.55, 0.60, 0.70
        ]:
            akurasi, _ = evaluasi(theme, data, ambang)

            print(
                f" {ambang:.2f}   {akurasi:6.1%}  "
                + "#" * round(akurasi * 30)
            )

        return

    akurasi, hasil = evaluasi(
        theme,
        data,
        args.ambang
    )

    print(
        f"Tema {args.tema} · ambang {args.ambang} "
        f"· {len(data)} kalimat uji"
    )

    print(f"Akurasi: {akurasi:.1%}\n")

    total = Counter(
        harapan for _, harapan, _, _ in hasil
    )

    benar = Counter(
        harapan for _, harapan, tebakan, _ in hasil
        if harapan == tebakan
    )

    print(f"{'intent':<30}{'benar':>6}{'total':>7}")

    for intent in sorted(total):
        print(
            f"{intent:<30}"
            f"{benar[intent]:>6}"
            f"{total[intent]:>7}"
        )

    salah = [
        data_uji for data_uji in hasil
        if data_uji[1] != data_uji[2]
    ]

    if salah:
        print("\nKalimat yang salah ditebak:")

        for kalimat, harapan, tebakan, skor in salah:
            print(
                f'- "{kalimat}" -> {tebakan} '
                f"({skor:.2f}), seharusnya {harapan}"
            )


if __name__ == "__main__":
    main()
