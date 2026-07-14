#!/usr/bin/env python3
"""
Velocity TTRPG — File Integrity Checker
Run from the repo root after any editing session:
    python verify_integrity.py

Checks every .md file under Core Rules/ for:
  - Null bytes (sign of Edit tool corruption)
  - Files that end without a trailing newline
  - Known truncation patterns from past corruption events
"""

import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
CORE_RULES = os.path.join(BASE, "Core Rules")

# Known past truncation markers — if a file ends with any of these, it is cut off.
# Each is a string that should NEVER be a valid file ending.
KNOWN_CUT_MARKERS = [
    "(requir",
    "correct pass",
    ", per",          # ends mid-sentence "...per 3 points of Strength, per"
    "deal 1 additiona",
    "healing and beas",
    "call for ",
    "Solan's Glor",
    "[Unc",
    "Maximum Healt",
    "+3 flat. Final",
    "characters ma",   # Example of Play
    "delivery type",   # Poisons.md (without the semicolon)
    "| Kinet",         # Damage.md table row cut
    "[Demon Lineage ", # mid-link
    "\nSun",           # Vampire Lineage
    "Campaign s",      # Magic.md
    "| Mortal Nat",    # Human Race
    "[Strength Skill](Unive",  # Skills.md
    "**E\n",           # Reflex Skill mid-Effect line
    "the target t",    # Whisper Walk
    "Casting Cost:** 2\n",  # Level 2 Spells (Solan's Light header)
    "does not warn",   # Solan's Glory
]


def check_file(path):
    issues = []
    with open(path, 'rb') as f:
        data = f.read()

    # 1. Null bytes
    null_count = data.count(b'\x00')
    if null_count > 0:
        issues.append("NULL BYTES: " + str(null_count) + " null bytes found")

    # 2. Decode
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError as e:
        issues.append("ENCODING ERROR: " + str(e))
        return issues

    # 3. Trailing newline
    if not text.endswith('\n'):
        issues.append("NO TRAILING NEWLINE — ends with: " + repr(text[-40:]))

    # 4. Known cut markers
    stripped = text.rstrip('\n')
    for marker in KNOWN_CUT_MARKERS:
        if stripped.endswith(marker.rstrip()):
            issues.append("KNOWN TRUNCATION PATTERN: " + repr(stripped[-60:]))
            break

    return issues


def main():
    total = 0
    problem_files = []

    for root, dirs, files in os.walk(CORE_RULES):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for fname in sorted(files):
            if not fname.endswith('.md'):
                continue
            fpath = os.path.join(root, fname)
            rel = os.path.relpath(fpath, BASE)
            total += 1
            issues = check_file(fpath)
            if issues:
                problem_files.append((rel, issues))

    print("Velocity TTRPG File Integrity Check")
    print("Scanned " + str(total) + " .md files in Core Rules/")
    print("")

    if not problem_files:
        print("All files clean.")
        return 0
    else:
        print("PROBLEMS IN " + str(len(problem_files)) + " FILE(S):")
        print("")
        for path, issues in problem_files:
            print("  " + path)
            for issue in issues:
                print("    - " + issue)
        print("")
        return 1


if __name__ == '__main__':
    sys.exit(main())
