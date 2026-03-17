#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script: build_popclip_extensions.py

Usage:
1. Put this script in the root folder, for example:
   OBTEXT/
     Sources/
       CN/
       International/
       Invest/
     Outputs/
     popclip_generate.py

2. Run:
   python3 popclip_generate.py

Behavior:
- Scan every subfolder under Sources/
- Create one .popclipext folder in Outputs/ for each source folder
- Copy these files from each source folder:
  config.js
  Config.plist
  obtext.png
"""

import os
import shutil

FILES_TO_COPY = [
    "config.js",
    "Config.plist",
    "obtext.png",
]


def ensure_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def build_one_extension(source_subdir: str, output_root: str) -> None:
    folder_name = os.path.basename(source_subdir.rstrip(os.sep))
    target_dir = os.path.join(output_root, f"{folder_name}.popclipext")

    if os.path.exists(target_dir):
        print(f"Warning: removing existing folder -> {target_dir}")
        shutil.rmtree(target_dir)

    os.makedirs(target_dir)

    missing_files = []

    for filename in FILES_TO_COPY:
        src = os.path.join(source_subdir, filename)
        dst = os.path.join(target_dir, filename)

        if not os.path.exists(src):
            missing_files.append(filename)
            continue

        shutil.copy2(src, dst)
        print(f"Copied: {src} -> {dst}")

    if missing_files:
        print(f"Warning: {folder_name} is missing files: {', '.join(missing_files)}")

    print(f"Done: {target_dir}\n")


def main() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sources_dir = os.path.join(script_dir, "Sources")
    outputs_dir = os.path.join(script_dir, "Outputs")

    if not os.path.isdir(sources_dir):
        print(f"Error: Sources folder not found -> {sources_dir}")
        return

    ensure_dir(outputs_dir)

    subfolders = [
        os.path.join(sources_dir, name)
        for name in os.listdir(sources_dir)
        if os.path.isdir(os.path.join(sources_dir, name))
    ]

    if not subfolders:
        print(f"Error: no source subfolders found under -> {sources_dir}")
        return

    print(f"Found {len(subfolders)} source folder(s).\n")

    for source_subdir in sorted(subfolders):
        build_one_extension(source_subdir, outputs_dir)

    print("All done.")


if __name__ == "__main__":
    main()