from utils import extract, build_chapters, build_html_files

lines = extract()

chapters = build_chapters(lines)

build_html_files(chapters)
