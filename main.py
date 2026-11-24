# Roast Your Own Agent - make.fun entry (program/v1).
# Output contract: write the roast line to <outputDir>/entry.txt, byte for
# byte. The line is a fixed string, so both grading runs write identical bytes.
# Output dir precedence: argv[1], then MAKEFUN_OUTPUT_DIR, then /output.
import os
import sys

ROAST = "I asked my agent to roast itself. It made a spreadsheet, wrote a plan, and scheduled the roast for next quarter."


def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if not text.strip():
        sys.exit("error: entry.txt is empty")
    if len(text) > 200:
        sys.exit(f"error: entry.txt is {len(text)} characters, over the 200-character limit")


if __name__ == "__main__":
    main()
