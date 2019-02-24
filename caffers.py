
from InterfaceManager import Interface
from ModuleManager import Module
from StatisticManager import Statistic
from DiaryManager import Diary
from configparser import ConfigParser
import os

def run():

    cfg = ConfigParser()
    cfg.read(os.environ['HOME'] + '/.caffers.conf')
    path = cfg.get('installation', 'path')

    print("[LOG] Begin to run")
    interface = Interface(path)
    statistic = Statistic(path, "StatisticFile")
    module = Module(path, "ModuleFile")
    diary = Diary(path + "Diary/")

    res = input("是否打开日记本？[y/n]")
    if res != 'y':
        print("放弃本次回答，日记关闭")
        return False

    res = input("是否开始写日记？[y/n]")
    if res == 'y':
        interface.add_diary()
    else:
        print("请选择其他功能：")
        show_menu()
        select_item = input("请输入序号：")
        while select_item != '0':
            if select_item == '1':
                question = input("请输入需要添加的问题：")
                module.add_question(question)
                res = input("继续添加？[y/n]")
                while res == 'y':
                    question = input("请输入需要添加的问题：")
                    module.add_question(question)
                    res = input("继续添加？[y/n]")

                break
            elif select_item == '2':
                module.show_all_questions()
                break

            elif select_item == '3':
                item_number = input("请输入要修改的问题序号：")
                question = input("请输入要修改为的内容：")
                module.change_question(item_number, question)
                break

            elif select_item == '3':
                recommanded_diary = statistic.get_random_diary()
                print("推荐日记：" + recommanded_diary)

                diary.show(recommanded_diary)

                break

            else:
                print("输入序号不合法")
                select_item = input("请输入序号：")

    #statistic.update_statistic_file(path + "Diary/")

    print("[LOG] End of run")

def show_menu():

    print("1. 增加新问题")
    print("2. 展示所有问题")
    print("3. 修改问题")
    print("4. 推荐过去的日记")
    print("5. 修改密码（未实现）")
    print("6. 备份日记（未实现）")
    print("0. 退出程序")




