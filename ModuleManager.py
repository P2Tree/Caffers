
import os
import yaml

class Module():
    def __init__(self, path, name):
        self.module_path = path
        self.module_name = name

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
        try:
            with open(self.module_path + self.module_name, 'rU') as module:
                questions = module.readlines()
                number = len(questions) # total number of questions
            return questions, number

        except FileNotFoundError:
            print("[ERROR] can't find module file")


    def add_question(self, question):

        if not os.path.exists(self.module_path + self.module_name):
            print("[LOG] can't find module file")
            self.create_module()

        with open(self.module_path + self.module_name, 'a') as module:
            module.write(question + "\n")

    def show_all_questions(self):
        with open(self.module_path + self.module_name, 'r') as module:
            questions = yaml.load(module)

        for q in questions:
            print(q + ": " + questions[q])

    def change_question(self, item_number, question):
        # TODO: yaml文件的写入仍然有问题
        qlist = self.get_questions_item_list()

        if item_number not in qlist:
            raise Exception("[ERROR] 输入问题序号错误")

        questions = dict()
        try:
            with open(self.module_path + self.module_name, 'w') as module:
                questions[item_number] = question
                module.write(yaml.dump(questions))
        except:
            raise
        finally:
            print("修改完毕")



    def get_questions_item_list(self):
        with open(self.module_path + self.module_name, 'r') as module:
            questions = yaml.load(module)

        qlist = []
        for q in questions:
            qlist.append(q)

        return qlist
