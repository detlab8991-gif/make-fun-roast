# Roast Your Own Agent - make.fun entry (program/v1).
# Output contract: write the roast line to <outputDir>/entry.txt, byte for
# byte. The line is a fixed string, so both grading runs write identical bytes.
import os

ROAST = "I asked my agent to roast itself. It made a spreadsheet, wrote a plan, and scheduled the roast for next quarter."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
