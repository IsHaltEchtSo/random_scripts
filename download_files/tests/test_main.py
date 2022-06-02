"""
to test the dl approach
"""
# TODO: improve GIVEN/WHEN/THEN descriptions
# TODO: write unit-tests for these functions
# TODO: write e2e-tests for this utility

import pytest
from download_files.main import \
    map_chapter, get_chapter_and_pages, check_for_manga_and_chapter_directory, construct_dl_url, download_from_url_to_target_dir


def test_construct_dl_url():
    """
    Whether the download-URL is constructed correctly
    """

    # GIVEN the basic URL, chapter index, pages and file_format
    url = "www.google.com/"
    chapter_index = 5
    page_one_digit, page_two_digit, page_three_digit, page_four_digit, page_five_digit = 7, 49, 343, 2401, 16807
    file_format = ".jpg"


    # WHEN the dl_urls are constructed with construct_dl_url()-function
    dl_url_one_digit = construct_dl_url(
        url=url,
        chapter_index=chapter_index,
        page=page_one_digit,
        file_format=file_format,
    )

    dl_url_two_digit = construct_dl_url(
        url=url,
        chapter_index=chapter_index,
        page=page_two_digit,
        file_format=file_format,
    )

    dl_url_three_digit = construct_dl_url(
        url=url,
        chapter_index=chapter_index,
        page=page_three_digit,
        file_format=file_format,
    )

    dl_url_four_digit = construct_dl_url(
        url=url,
        chapter_index=chapter_index,
        page=page_four_digit,
        file_format=file_format,
    )

    dl_url_five_digit = construct_dl_url(
        url=url,
        chapter_index=chapter_index,
        page=page_five_digit,
        file_format=file_format,
    )

    # THEN these asserts should work?
    assert dl_url_one_digit     == "www.google.com/5/p_00007.jpg"
    assert dl_url_two_digit     == "www.google.com/5/p_00049.jpg"
    assert dl_url_three_digit   == "www.google.com/5/p_00343.jpg"
    assert dl_url_four_digit    == "www.google.com/5/p_02401.jpg"
    assert dl_url_five_digit    == "www.google.com/5/p_16807.jpg"


def test_download_from_url_to_target_dir():
    """
    Whether a resource is accessed and downloaded from.
    """
    # GIVEN a

    # WHEN the download is being called

    # THEN their should be a new file in the temp directory