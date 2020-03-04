import pytest
from utils.utils import extract, build_chapters, build_html_files, get_chapter_file


def test_get_chapter_file():
    chapter = 'Chapter 1: Lorem'
    file = get_chapter_file(chapter)
    assert file == 'lorem.html', 'failed'


def test_get_chapter_file_long():
    chapter = 'Chapter 13: Lorem Ipsum Dolor'
    file = get_chapter_file(chapter)
    assert file == 'lorem-ipsum-dolor.html', 'failed'
