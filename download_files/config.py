import os



RESOURCE_URL_STR = "https://www.funmanga.com/uploads/chapter_files/7872/"
# EXAMPLE_URL: https://www.funmanga.com/uploads/chapter_files/7872/0/p_00044.jpg
RESOURCE_FORMAT = ".jpg"

SPECIAL_CHAPTERS_TO_IGNORE = [323]  # TODO: needs to be implemented

# Path to download files into
ROOT = "/Users/deniz/desktop/manga"
RESOURCE_NAME = "Vagabond"
PATH = os.path.join(ROOT, RESOURCE_NAME)