import random
import os

class Statistic():
    def __init__(self, path, filename):
        self.statistic_path = path
        self.statistic_name = filename
        if not os.path.exists(self.statistic_path + self.statistic_name):
            print("[LOG] Statistic file is not existed")
            raise FileNotFoundError

    def add_diary(self, diary_data):

        try:
            with open(self.statistic_path + self.statistic_name, 'a+') as st:
                if 0 == os.path.getsize(self.statistic_path + self.statistic_name):
                    print("[DEBUG] Statistic file is empty")
                    st.write(diary_data)
                else:
                    for existed_data in st.readline():
                        if existed_data != diary_data:
                            st.write(diary_data)
                            st.write('\n')
        except IOError:
            print("[ERROR] Write Statistic file failed")


    def get_random_diary(self):


        existed_data = []

        with open(self.statistic_path + self.statistic_name, 'r') as st:
            if 0 == os.path.getsize(self.statistic_path + self.statistic_name):
                print("[DEBUG] Statistic file is empty")
            else:
                for line in st.readlines():
                    existed_data.append(line.replace('\n', ''))

        ret = random.choice(existed_data)
        return ret


    def update_statistic_file(self, diary_path):
        (root, dirs, files) = os.walk(diary_path)
        # TODO: 对统计文件和已有日记文件做双向同步







