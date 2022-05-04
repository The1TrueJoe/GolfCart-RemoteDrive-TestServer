# Drive Computer Core Library
# Main
#
# Part of the GSSM Autonomous Golf Cart
# Written by Joseph Telaak, class of 2022

import sys

if __name__ == "__main__":
    # Version Check
    python_major = sys.version_info[0]
    python_version = str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])

    # Check for Python 3\
    python_major = sys.version_info[0]
    python_version = str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])

    if python_major != 3:
        print(f"The GSSM Auto Golf Cart Drive Computer Software Requires Python 3. You are using {python_version}")
        sys.exit(1)

    # Imports
    import src.util as util

    # Banner and Info Block
    print(util.to_color(util.title, "cyan"))
    print(util.info_block)

    # Run Program
    import src.drive as drive
    drive.main()