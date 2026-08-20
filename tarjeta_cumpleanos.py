#!/usr/bin/env python3
"""Tarjeta de cumpleaños pixel art, animada y monocromática."""

import os
import random
import shutil
import sys
import time

RESET = "\033[0m"
BOLD = "\033[1m"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
HOME = "\033[H"

FRAMES = [
    [
        "  /\\___/\\              \\o/              /\\___/\\  ",
        " (  o o  )              █              (  o o  ) ",
        " /   ^   \\            / \\             /   ^   \\ ",
        "(  \\___/  )          _/   \\_          (  \\___/  )",
        " /|     |\\                            /|     |\\ ",
        "(_|_   _|_)                          (_|_   _|_)",
    ],
    [
        "  /\\___/\\              o_              /\\___/\\  ",
        " (  ^ ^  )             /█              (  ^ ^  ) ",
        " /   o   \\            / \\             /   o   \\ ",
        "(  \\___/  )           /  _>           (  \\___/  )",
        " /|    _|\\                            /|_    |\\ ",
        "(_|___/  _)                          (_  \\___|_)",
    ],
    [
        "  /\\___/\\             _o/              /\\___/\\  ",
        " (  o o  )              █              (  o o  ) ",
        " /   ^   \\             /\\             /   ^   \\ ",
        "(  \\___/  )          _/  \\_           (  \\___/  )",
        " /|_    |\\                            /|    _|\\ ",
        "(_  \\___|_)                          (_|___/  _)",
    ],
    [
        "  /\\___/\\             \\o_              /\\___/\\  ",
        " (  ^ ^  )              █\\             (  ^ ^  ) ",
        " /   o   \\             / \\            /   o   \\ ",
        "(  \\___/  )           <_  \\          (  \\___/  )",
        " /|     |\\                            /|     |\\ ",
        "(_|_   _|_)                          (_|_   _|_)",
    ],
]


def centered(text, width):
    return " " * max(0, (width - len(text)) // 2) + text


def confetti(width, density=26):
    row = [" "] * width
    for _ in range(min(density, width)):
        row[random.randrange(width)] = random.choice("*+.:o")
    return "".join(row)


def draw(name, frame_number, width):
    frame = FRAMES[frame_number % len(FRAMES)]
    title = f"<3  FELIZ CUMPLEAÑOS, {name.upper()}!  <3"
    subtitle = "QUE TU DIA ESTE LLENO DE AMOR, ALEGRIA Y RONRONEOS"
    lines = [confetti(width), "", BOLD + centered(title, width) + RESET]
    lines.extend([centered(subtitle, width), ""])
    lines.extend(centered(line, width) for line in frame)
    lines.extend(["", centered("♪  MIAU, MIAU... A BAILAR!  ♪", width), "", confetti(width)])
    return "\n".join(lines)


def main():
    os.system("")
    name = "Mi Amor"
    if len(sys.argv) > 1:
        name = " ".join(sys.argv[1:]).strip() or name
    width = max(72, min(shutil.get_terminal_size((90, 28)).columns, 110))

    try:
        print(HIDE_CURSOR, end="", flush=True)
        for i in range(48):
            print(HOME + "\033[2J" + draw(name, i, width), end="", flush=True)
            time.sleep(0.22)
        print("\n" + centered("TE AMO Y QUIERO CELEBRAR MUCHOS CUMPLEAÑOS CONTIGO <3", width))
        print(centered("PRESIONA ENTER PARA CERRAR", width), flush=True)
        input()
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        print(RESET + SHOW_CURSOR)


if __name__ == "__main__":
    main()
