#author: whz
#lib_info_page:http://html.python-requests.org/

from requests_html import HTMLSession
import os
NOVEL_CHAPTERS = "http://www.xbiquge.cc/book/28810/"

session = HTMLSession()

def get_html_page(url):
    page = session.get(url)
    return page

def get_all_chapters(chapter_page):
    chapters = chapter_page.html.find('#list',first=True)
    return chapters

def get_text_from_novel_page(novel_page):
    content = novel_page.html.find('#content',first=True)
    return content.full_text


if __name__ == '__main__':
    page = get_html_page(NOVEL_CHAPTERS)
    # print(get_all_chapters(page).text)
    chapter = get_all_chapters(page)
    novel_page_list = chapter.absolute_links #拿到的是乱序的，诡异
    novel_page_list = sorted(novel_page_list)

    main_body = ''

    for novel_page_link in novel_page_list:
        novel_page = get_html_page(novel_page_link)
        text = get_text_from_novel_page(novel_page)
        if text == "":
            continue
        print('%s  done', novel_page_link)
        main_body += text
    with open('text.txt', 'wt') as fileout:
        fileout.write(main_body)

