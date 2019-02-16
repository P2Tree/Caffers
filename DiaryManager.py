
import datetime
import os

class Diary():
    def __init__(self, path):
        self.diary_path = path
        self.diary_name = None

    def new_diary(self):
        self.diary_name = "diary-" + datetime.datetime.now().strftime("%Y-%m-%d") + ".md"

        if not os.path.exists(self.diary_path):
            print("[LOG] Diary path is not existed")
            try:
                os.makedirs(self.diary_path)
                print("[LOG] Create new Diary path, done")
            except IOError:
                print("[ERROR] Create new Diary path failed")
                return -1

        if os.path.exists(self.diary_path + self.diary_name):
            print(datetime.datetime.now().strftime("%Y年%m月%d日") + "的日记已经存在")
            return 1

        print("新建" + datetime.datetime.now().strftime("%Y年%m月%d日") + "的日记")
        render = Render()
        try:
            with open(self.diary_path + self.diary_name, 'w') as diary:
                diary.write(render.header_1(datetime.datetime.now().strftime("%Y年%m月%d日") + "\n"))
            return 0
        except IOError:
            print("[ERROR] diary create failed")
            return -1


    '''
        展示当前日记
    '''
    def show(self):
        try:
            print("*****")
            with open(self.diary_path + self.diary_name, 'r') as diary:
                for line in diary.readlines():
                    print(line, end="")
            print("\n*****")

        except FileNotFoundError:
            print("[Error] Diary of " + datetime.datetime.now().strftime("%Y/%m/%d") + " is Not Existed")

    '''
        追加新的回答到当前日记
    '''
    def add_answer(self, question, answer):
        render = Render()
        try:
            with open(self.diary_path + self.diary_name, 'a') as diary:
                diary.write(render.header_2(question))
                diary.write(render.blockquote(answer))
                diary.write("\n")
            return True
        except FileNotFoundError:
            print("[Error] Diary of " + datetime.datetime.now().strftime("%Y/%m/%d") + " is Not Existed")
            return False

class Render():
    def header_1(self, content):
        res = '# ' + content
        return res

    def header_2(self, content):
        res = '## ' + content
        return res

    def header_3(self, content):
        res = '### ' + content
        return res

    def blockquote(self, content):
        res = '> ' + content
        return res

    def plain_text(self, content):
        res = "'''" + content + "'''"
        return res

    def text(self, content):
        res = content
        return res

