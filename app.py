
"""
Aplikasi Web Chatbot RenangPedia menggunakan Flask.

Jalankan:
    python app.py

Buka:
    http://127.0.0.1:5000
"""

import os
import uuid
from pathlib import Path

from flask import Flask, abort, jsonify, render_template, request, session

from chatbot import ChatbotEngine, ChatHistory, load_themes


BASE_DIR = Path(__file__).resolve().parent
THEME_ID = "renangpedia"


def create_app(config=None):
    app = Flask(__name__)

    # Konfigurasi aplikasi
    app.config.update(
        SECRET_KEY=os.environ.get(
            "SECRET_KEY", "renangpedia-secret-key"
        ),
        DATABASE=os.environ.get(
            "DATABASE", str(BASE_DIR / "chat_history.db")
        ),
        THEMES_DIR=str(BASE_DIR / "themes"),
        THRESHOLD=float(os.environ.get("THRESHOLD", "0.45")),
        ADMIN_KEY=os.environ.get("ADMIN_KEY", ""),
        MAX_LEN=500,
    )

    if config:
        app.config.update(config)

    # Memuat tema RenangPedia
    all_themes = load_themes(app.config["THEMES_DIR"])

    if THEME_ID not in all_themes:
        raise ValueError(
            "Tema renangpedia tidak ditemukan di folder themes."
        )

    themes = {THEME_ID: all_themes[THEME_ID]}

    # Membuat engine chatbot
    engines = {
        THEME_ID: ChatbotEngine(
            themes[THEME_ID],
            app.config["THRESHOLD"]
        )
    }

    # Menghubungkan database
    history = ChatHistory(app.config["DATABASE"])

    # Mengambil ID sesi pengguna
    def get_session_id():
        if "sid" not in session:
            session["sid"] = uuid.uuid4().hex
        return session["sid"]

    # Memeriksa tema
    def get_theme_or_404(theme_id):
        if theme_id not in themes:
            abort(404, description="Tema chatbot tidak ditemukan.")
        return themes[theme_id]

    # Memeriksa akses admin
    def check_admin():
        key = app.config["ADMIN_KEY"]
        if key and request.args.get("key") != key:
            abort(403, description="Kunci admin salah atau tidak ada.")

    # ==================================================
    # HALAMAN WEB
    # ==================================================

    # Halaman pembuka sebelum masuk ke chatbot
    @app.route("/")
    def index():
        return render_template("welcome.html")

    # Halaman utama chatbot
    @app.route("/home")
    def home():
        return render_template(
            "index.html",
            themes=themes.values()
        )

    # Halaman percakapan chatbot
    @app.route("/chat/<theme_id>")
    def chat_page(theme_id):
        theme = get_theme_or_404(theme_id)
        return render_template("chat.html", theme=theme)

    # Halaman admin
    @app.route("/admin/<theme_id>")
    def admin_page(theme_id):
        check_admin()
        theme = get_theme_or_404(theme_id)

        return render_template(
            "admin.html",
            theme=theme,
            summary=history.summary(theme_id),
            stats=history.stats(theme_id),
            unknown=history.unknown_questions(theme_id),
            threshold=app.config["THRESHOLD"],
        )

    # ==================================================
    # REST API
    # ==================================================

    @app.get("/api/themes")
    def api_themes():
        return jsonify([
            {
                "id": theme["id"],
                "name": theme["name"],
                "description": theme["description"],
            }
            for theme in themes.values()
        ])

    # API untuk mengirim pertanyaan
    @app.post("/api/chat")
    def api_chat():
        data = request.get_json(silent=True) or {}

        message = str(data.get("message", "")).strip()
        theme_id = data.get("theme", THEME_ID)

        if theme_id not in engines:
            return jsonify({"error": "Tema tidak valid."}), 400

        if not message:
            return jsonify({"error": "Pesan tidak boleh kosong."}), 400

        if len(message) > app.config["MAX_LEN"]:
            return jsonify({
                "error": (
                    f"Pesan maksimal {app.config['MAX_LEN']} karakter."
                )
            }), 400

        sid = get_session_id()

        # Memproses pertanyaan menggunakan engine
        result = engines[theme_id].reply(message)

        # Menyimpan pertanyaan dan jawaban ke database
        history.add(
            sid,
            theme_id,
            "user",
            message,
            result["intent"],
            result["score"],
        )

        history.add(
            sid,
            theme_id,
            "bot",
            result["reply"],
            result["intent"],
            result["score"],
        )

        return jsonify(result)

    # API untuk melihat kandidat intent
    @app.post("/api/explain")
    def api_explain():
        data = request.get_json(silent=True) or {}

        theme_id = data.get("theme", THEME_ID)

        if theme_id not in engines:
            return jsonify({"error": "Tema tidak valid."}), 400

        message = str(data.get("message", ""))[:app.config["MAX_LEN"]]

        return jsonify({
            "threshold": app.config["THRESHOLD"],
            "candidates": engines[theme_id].explain(message),
        })

    # API untuk mengambil riwayat
    @app.get("/api/history/<theme_id>")
    def api_history(theme_id):
        get_theme_or_404(theme_id)

        return jsonify(
            history.get(get_session_id(), theme_id)
        )

    # API untuk menghapus riwayat
    @app.delete("/api/history/<theme_id>")
    def api_clear_history(theme_id):
        get_theme_or_404(theme_id)

        history.clear(get_session_id(), theme_id)

        return jsonify({"status": "ok"})

    # API untuk mengambil statistik
    @app.get("/api/stats/<theme_id>")
    def api_stats(theme_id):
        check_admin()
        get_theme_or_404(theme_id)

        return jsonify(history.stats(theme_id))

    # ==================================================
    # PENANGANAN ERROR
    # ==================================================

    @app.errorhandler(403)
    @app.errorhandler(404)
    def handle_error(err):
        if request.path.startswith("/api/"):
            return jsonify({"error": err.description}), err.code

        return render_template(
            "404.html",
            message=err.description,
            code=err.code,
        ), err.code

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
