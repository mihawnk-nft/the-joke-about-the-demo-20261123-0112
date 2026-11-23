# The Demo That Knew Too Much — entry for the-joke-about-the-demo-20261123-0112 (make.fun).
# A program that writes one joke about working beside AI coding agents to entry.txt.
# Deterministic: the same joke bytes on every run, no randomness, no I/O
# besides the single output file.
import os

JOKE = (
    "My AI coding agent crashed the live demo, apologised, and fixed it — "
    "by restoring the code I'd written before I asked it for help."
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
