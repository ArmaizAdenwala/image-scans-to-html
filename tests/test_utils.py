import pytest
from utils.utils import extract, build_chapters, build_html_files, get_chapter_file, InvalidChapterException


def test_get_chapter_file():
    chapter = 'Chapter 1: Lorem'
    file = get_chapter_file(chapter)
    assert file == 'lorem.html', 'failed'


def test_get_chapter_file_long():
    chapter = 'Chapter 13: Lorem Ipsum Dolor'
    file = get_chapter_file(chapter)
    assert file == 'lorem-ipsum-dolor.html', 'failed'


def test_get_chapter_file_invalid_chapter_exception():
    with pytest.raises(InvalidChapterException):
        chapter = 'Lorem Ipsum Dolor'
        get_chapter_file(chapter)


def test_get_chapter_file_chapter_name_not_at_start():
    with pytest.raises(InvalidChapterException):
        chapter = 'Lorem Ipsum Chapter 12: Dolor'
        get_chapter_file(chapter)


def test_get_chapter_file_chapter_name_at_end():
    with pytest.raises(InvalidChapterException):
        chapter = 'Lorem Ipsum Chapter 12:'
        get_chapter_file(chapter)
