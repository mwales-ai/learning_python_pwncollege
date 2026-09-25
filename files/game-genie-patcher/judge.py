#!/usr/bin/exec-suid -- /usr/local/bin/python3 -I

import sys
import os
import hashlib

# sha256 of a correctly patched cat_mercs_1.1.nes (both SZYONU and SZYPKK
# applied). Not a secret - the point of this challenge is patching the
# bytes correctly, not guessing a hash, so there is nothing to protect by
# hiding it.
EXPECTED_HASH = "b2873ddd97c244fca0476cff5ddc9c9ab9c2776e4e3ef3ccf185eb1450d6f5ea"


def main(argv):
    if len(argv) != 2:
        print("You need to pass me the path of your patched ROM file")
        print("Example: /challenge/judge.py /home/hacker/cat_mercs_patched.nes")
        return 1

    rom_path = argv[1]

    if not os.path.exists(rom_path):
        print(f"I cannot find a file named {rom_path}")
        return 1

    if os.path.isdir(rom_path):
        print(f"{rom_path} is a directory, not a ROM file")
        return 1

    try:
        with open(rom_path, "rb") as f:
            rom_data = f.read()
    except OSError as e:
        print(f"I could not read {rom_path}: {e}")
        return 1

    actual_hash = hashlib.sha256(rom_data).hexdigest()

    if actual_hash != EXPECTED_HASH:
        print("That ROM does not match what I expected.")
        print(f"  expected sha256: {EXPECTED_HASH}")
        print(f"  your file's sha256: {actual_hash}")
        print("Check that you patched both Game Genie codes, at the right")
        print("file offsets, and that you wrote out every other byte of the")
        print("ROM completely unchanged.")
        return 1

    print("That's a perfect patch!")
    with open("/flag", "r") as f:
        print(f.read())

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
