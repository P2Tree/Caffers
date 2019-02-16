
from ModuleManager import Module
from DiaryManager import Diary
from ExportManager import Export
from configparser import ConfigParser
import os

class Interface():

    def __init__(self):
        print("[LOG] arguments input")
        self.questions = []
        self.number = 0
        cfg = ConfigParser()
        cfg.read(os.environ['HOME'] + '/.caffers.conf')
        self.path = cfg.get('installation', 'path')
        self.module_path = self.path
        self.module_name = "ModuleFile"
        self.diary_path = self.path + "Diary/"

    def add_diary(self):
        self.catch_module()

        diary = self.dialog()

        if diary == -1:
            return

        self.export(diary)

    def catch_module(self):
        print("[LOG] Call ModuleManager")
        module = Module(self.module_path, self.module_name)
        self.questions, self.number = module.get_questions()

    '''
        新建日记，增加回答
    '''
    def dialog(self):
        print("[LOG] Call DairyManager")

        diary = Diary(self.diary_path)
        res = diary.new_diary()
        if res == -1:
            return -1
        elif res == 1:
            #TODO: 将来对已经存在的日记做特殊处理，检查问题是否存在，修改存在的问题，而不是直接追加
            return -1

        for n in range(0, self.number):
            answer = input(self.questions[n])
            diary.add_answer(self.questions[n], answer)

        print("完成回答")

        diary.show()

        return diary


    def export(self, diary):
        print("[LOG] Call ExportManager")

        export = Export()
        export.export_html(diary.diary_name)


    def go_add_question(self):
        print("go_add_question")
        module = Module(self.module_path, self.module_name)
        question = input("请输入需要添加的问题：")
        module.add_question(question)
        print("添加成功")

    def go_change_password(self):
        print("go_change_password")
        pass

    def go_backup_diary(self):
        print("go_backup_diary")
        pass




