import pytesseract
import glob
import re
import stringcase


def extract():
    pages = glob.glob('./data/*.jpg')
    pages.sort()

    text = ''

    for page in pages:
        print('extracting: {}'.format(page))
        text += pytesseract.image_to_string(page)

    lines = text.split('\n')
    return lines


def build_chapters(lines):
    chapters = {}
    cur_chapter = None
    cur_string = ''
    for line in lines:
        is_chapter = re.match(r"^(Chapter [0-9]+:)", line)

        if is_chapter:
            if cur_chapter is not None:
                chapters[cur_chapter] = cur_string
            cur_chapter = line
            cur_string = ''
        else:
            cur_string += line
    return chapters


def get_chapter_file(chapter):
    chapter_spinal_case = convert_chapter_to_spinal(chapter)
    return '{}.html'.format(chapter_spinal_case)


def build_html_files(chapters):
    chapter_keys = list(chapters.keys())
    for index, chapter in enumerate(chapter_keys):
        chapter_file = get_chapter_file(chapter)
        file_name = './html/{}'.format(chapter_file)
        html_file = open(file_name, 'w')

        prev_link = ''
        next_link = ''
        if index > 0:
            prev_chapter = chapter_keys[index - 1]
            prev_chapter_file = get_chapter_file(prev_chapter)
            prev_link = '<p><a href="{}">Previous</a></p>'.format(
                prev_chapter_file)

        if (index < len(chapters.keys()) - 1):
            next_chapter = chapter_keys[index + 1]
            next_chapter_file = get_chapter_file(next_chapter)
            next_link = '<p><a href="{}">Next</a></p>'.format(
                next_chapter_file)

        content = """<html>
<head>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<div>
<h1>{0}</h1>
<p>{1}</p>{2}{3}</div></body>
</html>""".format(chapter, chapters[chapter], prev_link, next_link)
        html_file.write(content)
        html_file.close()


def convert_chapter_to_spinal(chapter):
    name = re.sub(r"^(Chapter [0-9]+: )", '', chapter)
    return stringcase.spinalcase(name)
