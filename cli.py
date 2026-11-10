
"""
Chatbot RenangPedia melalui terminal tanpa browser.

Jalankan:
    python cli.py
    python cli.py --debug
    python cli.py --ambang 0.50

Ketik 'keluar' untuk berhenti.
"""

import argparse
from pathlib import Path

from chatbot import ChatbotEngine, load_themes


BASE_DIR = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(
        description="Chatbot RenangPedia di terminal"
    )

    parser.add_argument(
        "--tema",
        default="renangpedia",
        help="ID tema chatbot"
    )

    parser.add_argument(
        "--ambang",
        type=float,
        default=0.45,
        help="Ambang batas skor kemiripan"
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        help="Tampilkan tiga kandidat intent teratas"
    )

    args = parser.parse_args()

    themes = load_themes(BASE_DIR / "themes")

    if args.tema not in themes:
        print(f"Tema '{args.tema}' tidak ditemukan.")
        return

    theme = themes[args.tema]
    bot = ChatbotEngine(theme, args.ambang)

    print(f"{theme['avatar']} {theme['bot_name']}")
    print(theme["greeting"])
    print("\nKetik 'keluar' untuk berhenti.\n")

    while True:
        try:
            pesan = input("Anda: ").strip()

        except (EOFError, KeyboardInterrupt):
            print()
            break

        if pesan.lower() in {"keluar", "exit", "quit"}:
            break

        if not pesan:
            continue

        hasil = bot.reply(pesan)

        print(f"{theme['bot_name']}: {hasil['reply']}")

        label = hasil["intent"] or "tidak dikenali"

        print(
            f"   [Intent: {label} | Skor: {hasil['score']:.2f}]"
        )

        if args.debug:
            print("\nKandidat intent:")

            for i, kandidat in enumerate(
                bot.explain(pesan), 1
            ):
                print(
                    f"   {i}. {kandidat['intent']:<25} "
                    f"{kandidat['score']:.2f} "
                    f"| Pola: {kandidat['pattern']}"
                )

        print()

    print("Terima kasih telah menggunakan RenangPedia!")


if __name__ == "__main__":
    main()
