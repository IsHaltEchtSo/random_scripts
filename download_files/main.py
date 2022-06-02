import os
import urllib.request
from typing import Tuple

from config import \
    RESOURCE_NAME, RESOURCE_URL_STR, RESOURCE_FORMAT, PATH


def greet_user(resource_name: str, resource_url: str) -> None:
    """
    info text so the user knows what's going on
    """
    print(".    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .\n")  # TODO: turn this into a decorator for main
    print(f"YOU ARE ABOUT TO DOWNLOAD FILES OF `{resource_name}`")
    print(f"FROM `{resource_url}`!")


def map_chapter(chapter_number: int) -> int:
    """
    Sometimes, in-between chapters exist and mess up with enumeration of the chapters.
    Here you can specify where these in-between chapters appear to exclude them.
    """
    # chapter 1 starts at index 0
    if chapter_number < 323:
        chapter_index = chapter_number - 1

    # chapter 323 is a special in-between chapter that needs to be excluded
    # hence, from index 324 onwards, index == chapter number
    elif chapter_number > 323:
        chapter_index = chapter_number
    
    return chapter_number, chapter_index


def get_chapter_and_pages() -> Tuple[int, int]:
    """
    get user input about chapter number and amount of images to download
    """
    chapter = int(input("WHICH CHAPTER DO YOU WANT? \n >>> "))
    pages = int(input("WHAT IS THE LAST IMAGE NUMBER OF THAT CHAPTER? \n >>> "))

    return chapter, pages


def check_for_manga_and_chapter_directory(path: str, chapter:int) -> None:
    """
    Check whether a directory for the manga exists, and whether it contains a 
    directory for the chapter. Create them if not existing.
    """
    # check for the manga's directory
    try:
        os.listdir(path)
    except FileNotFoundError:
        os.mkdir(path)

    # check for the chapter's directory
    try:
        os.listdir(path + f"/Chapter-{chapter}")
    except FileNotFoundError:
        os.mkdir(path + f"/Chapter-{chapter}")


def construct_dl_url(url: str, chapter_index: int, page: int, file_format: str) -> str:
    """
    Depending on the page-number, adjust the `p_00000` part of the URL. 
    Two digit page like 13 becomes `p_00013`, four digit page like 1234 becomes `p_01234` and so on.
    """
    if page < 10:
        download_url = os.path.join(url, str(chapter_index), f"p_0000{page}{file_format}")

    elif page >= 10 and page < 100:
        download_url = os.path.join(url, str(chapter_index), f"p_000{page}{file_format}")

    elif page >= 100 and page < 1_000:
        download_url = os.path.join(url, str(chapter_index), f"p_00{page}{file_format}")

    elif page >= 1000 and page < 10_000:
        download_url = os.path.join(url, str(chapter_index), f"p_0{page}{file_format}")
    
    elif page >= 10_000 and page < 100_000:
        download_url = os.path.join(url, str(chapter_index), f"p_{page}{file_format}")

    return download_url


def download_from_url_to_target_dir(download_url: str, target_dir: str, page: int, file_format: str) -> None:
    """
    Given some URL, download its file into the target directory.
    """
    file_name = os.path.join(target_dir, f"Page {page}{file_format}")
    file_opener = urllib.request.URLopener()
    file_opener.addheader(
        "User-Agent",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
    )

    file_opener.retrieve(url=download_url, filename=file_name)


def print_success_message(manga:str, chapter:int, pages:int) -> None:
    """
    Let the user know that his download was successful.
    """
    print(f"Download complete for chapter {chapter} of Manga {manga}: pages 1 - {pages}")


def main():
    # give instructions to the user
    greet_user(
        resource_name=RESOURCE_NAME, 
        resource_url=RESOURCE_URL_STR
    )

    # ask for chapter and number of pages
    chapter, pages = get_chapter_and_pages()

    # check whether the manga and the chapters have a directory, else create them
    check_for_manga_and_chapter_directory(path=PATH, chapter=chapter)

    # hold real chapter number and index of the chapter stored on the desired website
    chapter_number, chapter_index = map_chapter(chapter_number=chapter)
    TARGET_DIR = os.path.join(PATH, f"chapter-{chapter_number}")

    # loop through all images
    for page in range(1, pages + 1):

        # construct URL and download the file for every page
        download_url = construct_dl_url(
            url=RESOURCE_URL_STR, 
            chapter_index=chapter_index, 
            page=page, 
            file_format=RESOURCE_FORMAT,
        )

        download_from_url_to_target_dir(
            download_url=download_url, 
            target_dir=TARGET_DIR,
            page=page,
            file_format=RESOURCE_FORMAT,
        )

    # print 'DL complete for chapter X of Manga Y: pages 1 - Z'
    print_success_message(manga=RESOURCE_NAME, chapter=chapter, pages=pages)


if __name__ == "__main__":
    main()
