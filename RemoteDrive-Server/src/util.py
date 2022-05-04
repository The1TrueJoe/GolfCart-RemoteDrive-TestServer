# Drive Computer
# Remote Drive Test Server
#
# Part of the GSSM Autonomous Golf Cart
# Written by:
#   Benjamin Chauhan, class of 2022
#   Joseph Telaak, class of 2022

# ASCII Art Header for Console Output
title = """
   ________________ __  ___   ___         __        ______           __
  / ____/ ___/ ___//  |/  /  /   | __  __/ /_____  / ____/___ ______/ /_
 / / __ \__ \\\__ \/ /|_/ /  / /| |/ / / / __/ __ \/ /   / __ `/ ___/ __/
/ /_/ /___/ /__/ / /  / /  / ___ / /_/ / /_/ /_/ / /___/ /_/ / /  / /_
\____//____/____/_/  /_/  /_/  |_\__,_/\__/\____/\____/\__,_/_/   \__/

"""

# Info Block Printed to Console on Init
info_block = """
    GSSM's Auto Golf Cart Project
    Hardware Module Tester

    Project Built for Dr. Parshall's Engineering Projects Course

    Software written by 
        Joseph Telaak (The1TrueJoe), GSSM Class of 2022

    See https://github.com/GSSM-AutoGolfCart
"""

def to_color(string, color):
    colors = {
        "black": "\033[0;30m",
        "red": "\033[0;31m",
        "green": "\033[0;32m",
        "yellow": "\033[0;33m",
        "blue": "\033[0;34m",
        "purple": "\033[0;35m",
        "cyan": "\033[0;36m",
        "white": "\033[0;37m",
        "reset": "\033[0m"

    }

    return colors[color] + str(string) + colors["reset"]

if __name__ == "__main__":
    # Banner and Info Block
    print(to_color(title, "cyan"))
    print(info_block) 