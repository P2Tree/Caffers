
from InterfaceManager import Interface
from ModuleManager import Module

def run():
    print("[LOG] Begin to run")
    interface = Interface()

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
                interface.go_add_question()
                res = input("继续添加？[y/n]")
                while res == 'y':
                    interface.go_add_question()
                    res = input("继续添加？[y/n]")

                break
            else:
                print("输入序号不合法")
                select_item = input("请输入序号：")

    print("[LOG] End of run")

def show_menu():

    print("1. 增加新问题")
    print("2. 修改密码（未实现）")
    print("3. 备份日记（未实现）")
    print("0. 退出程序")




