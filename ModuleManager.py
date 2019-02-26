
import os
import yaml

class Module():
    def __init__(self, path, name):
        self.module_path = path
        self.module_name = name

        if not os.path.exists(self.module_path + self.module_name):
            print("[LOG] can't find module file")
            self.create_module()

    def create_module(self):
        if not os.path.exists(self.module_path):
            try:
                os.makedirs(self.module_path)
                print("[LOG] Create new module path, done")
            except IOError:
                print("[ERROR] Create new module path failed")
        else:
            if os.path.exists(self.module_path + self.module_name):
                print("[LOG] module file is existed")
                return

            print("[LOG] Create new module file")
            try:
                file = open(self.module_path + self.module_name, 'w')
                file.close()
            except IOError:
                print("[ERROR] create module file failed")


    def get_questions(self):
        with open(self.module_path + self.module_name, 'r') as module:
            questions = yaml.load(module)

        if questions is None:
            raise Exception("模板文件内容为空")

        qlist = []
        for q in questions:
            print(q + ": " + questions[q])
            qlist.append(questions[q])

        number = len(qlist)
        return qlist, number


    def add_question(self, question):

        with open(self.module_path + self.module_name, 'r') as module:
            questions = yaml.load(module)

        number = len(questions)
        questions["Q"+str(number+1)] = question

        with open(self.module_path + self.module_name, 'w') as module:
            yaml.dump(questions, module, default_flow_style=False)


    def show_all_questions(self):
        with open(self.module_path + self.module_name, 'r') as module:
            questions = yaml.load(module)

        if questions is None:
            raise Exception("模板文件内容为空")

        for q in questions:
            print(q + ": " + questions[q])

    def change_question(self, item_number, question):
        qlist = self.get_questions_item_list()

        if item_number not in qlist:
            raise Exception("[ERROR] 输入问题序号错误")

        try:
            with open(self.module_path + self.module_name, 'r') as module:
                questions = yaml.load(module)
                questions[item_number] = question
            with open(self.module_path + self.module_name, 'w') as module:
                yaml.dump(questions, module, default_flow_style=False)
        except:
            raise


    def get_questions_item_list(self):
        with open(self.module_path + self.module_name, 'r') as module:
            questions = yaml.load(module)

        if questions is None:
            raise Exception("模板文件内容为空")

        qlist = []
        for q in questions:
            qlist.append(q)

        return qlist
