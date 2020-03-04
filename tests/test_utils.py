import pytest
import glob

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


def test_extract():
    res = extract('./test_data/*.jpg')
    assert res.index('Chapter 1: Lorem') == 0, 'failed'
    assert res.index('Chapter 2: lpsum') == 9, 'failed'
    assert res.index('Chapter 3: lpsum') == 14, 'failed'
    assert res.index(
        'Fusce sed diam erat. Suspendisse bibendum, nisl hendrerit malesuada tempor, leo purus'
    ) == 11, 'failed'


def test_build_chapters():
    lines = [
        'Chapter 1: lorem', 'lorem', 'Chapter 2: ipsum', 'dolor', 'sit', 'amet'
    ]
    chapters = build_chapters(lines)
    assert chapters['Chapter 1: lorem'] == 'lorem\n', 'failedkjjik'
    assert chapters['Chapter 2: ipsum'] == 'dolor\nsit\namet\n', 'failed'


def test_build_html_files():
    chapters = {
        'Chapter 1: Lorem': 'lorem\n',
        'Chapter 2: Ipsum': 'lorem\nipsum\ndolor\n'
    }
    build_html_files(chapters, './test_html/')
    files = glob.glob('./test_html/*.html')
    assert len(files) == 2
