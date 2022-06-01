# import dependencies
import os
from typing import List
from config import \
    PATH, FILE_PREFIX, FILE_SUFFIX


def rename_files(prefix: str, suffix: str, files: List[str]):
    """
    Strip the files off of their prefixes and suffixes.
    """
    for file in files:
        if file.startswith(prefix) and file.endswith(suffix):
            # TODO: for some reason, l-/rstrip also strips some of the `main` characters
            # if the suffix/prefix is provided a whitespace. For now, excluding whitespaces
            # and calling an additional strip() handles this problem.
            new_file_name = file.lstrip(prefix).rstrip(suffix).strip()  

            os.rename(
                PATH + f"/{file}",
                PATH + f"/{new_file_name}.pdf"
            )

            print(f"Successfully changed `{file}` to `{new_file_name}`!")


def main():
    files = os.listdir(PATH)

    rename_files(prefix=FILE_PREFIX, suffix=FILE_SUFFIX, files=files)


if __name__ == "__main__":
    main()
