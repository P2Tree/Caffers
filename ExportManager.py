
import markdown
import os
from configparser import ConfigParser

class Export():
    def __init__(self):
        cfg = ConfigParser()
        cfg.read(os.environ['HOME'] + '/.caffers.conf')
        self.path = cfg.get('installation', 'path')
        self.diary_path = self.path + 'Diary/'
        self.export_html_path = self.path + 'Export/Html/'

    def md2html(self, mdstr):
        exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.tables',
                'markdown.extensions.toc']

        html = '''
            <html lang="zh-cn">
            <head>
            <meta content="text/html; charset=utf-8" http-equiv="content-type" />
            <link href="../../Render/misty-light.css" rel="stylesheet">
            </head>
            <body>
            %s
            </body>
            </html>
            '''

        #<link href="default.css" rel="stylesheet">
        #<link href="github.css" rel="stylesheet">
        ret = markdown.markdown(mdstr, extensions=exts)
        return html % ret

    def export_html(self, diary_name):
        with open(self.diary_path + diary_name, 'r') as diary:
            md = diary.read()

        filename = diary_name.split('.')[0]
        export_filename = self.export_html_path + filename + '.html'

        if not os.path.exists(self.export_html_path):
            print("[LOG] Export HTML path is not existed")
            try:
                os.makedirs(self.export_html_path)
                print("[LOG] Create new export HTML path, done")
            except Exception:
                print("[ERROR] Create new export HTML path failed")

        if os.path.exists(export_filename):
            res = input("日记渲染文件已存在，是否覆盖？[y/n]")
            if res != 'y':
                return False
            os.remove(export_filename)

        with open(export_filename, 'w') as file:
            file.write(self.md2html(md))

