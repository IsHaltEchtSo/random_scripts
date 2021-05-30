# import dependencies
from config import *


def main():
    # load the files from the directory
    files = os.listdir(PATH)

    # loop through all files of the directory
    for file in files:
        if file.endswith(FILE_SUFFIX):
            # change each file to another name
            num = file[EXTRACTION_DETAIL]
            os.rename(
                PATH + f"/{file}",
                PATH + f"/{num}.jpg"
            )


if __name__ == "__main__":
    main()
