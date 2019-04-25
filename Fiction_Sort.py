import os
import sys
from PyQt5 import QtWidgets
from Fiction_Form import Ui_MainWindow

class Fiction_Sort_Form(QtWidgets.QWidget,Ui_MainWindow):
    def __init__(self):
        super(Fiction_Sort_Form, self).__init__()
        self.setupUi(self)

    def pushButton_click(self):
        fpath=self.txt_fpath.toPlainText()
        fiction_sort=Fiction_Sort(fpath)
        reg=fiction_sort.judge_format()
        self.lbl_Error.setText(reg)
        self.lbl_new_path.setText(fiction_sort.new_path)

class Fiction_Sort(object):
    def __init__(self,path):
        self.__path=path
        self.__common_used_numerals = {'零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
                                '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}
        self.__error=""
        self.new_path=""
    #检验文件
    def judge_format(self):
        # 检验路径是否真实存在
        if not os.path.exists(self.__path):
            self.__error="路径不存在，请重新输入。。。"
        #检验给出的路径是否是一个文件
        elif not os.path.isfile(self.__path):
            self.__error="该路径下没有发现文件，请确认路径是否正确"
        #检验是否是txt
        elif not os.path.splitext(os.path.split(self.__path)[1])[1] == ".txt":
            self.__error="该文件不是txt，不符合要求"
        else:
            self.__error=self.sorted()
        return self.__error

    def sorted(self):
        try:
            fr = open(self.__path, 'r', encoding="utf-8")
            txts = fr.readlines()
            # 暂时存放每一章节内容的列表
            l = []
            # 存放章节序号的列表
            s = []
            # 列表元素为各个章节内容
            m = []
            # num :判断一章节内容读取完毕标志
            # str_ :过渡的字符串

            for x in txts:
                if "第" and "章" in x and x[0] == "第":
                    num = True
                    l.append(x)
                    # 获取章节号
                    s.append(x.split("第")[1].split("章")[0])
                else:
                    num = False
                    l.append(x)

                if num:
                    # 对暂存的内容进行处理，得到各个章节内容
                    str_ = ""
                    for x in l[:-1]:
                        str_ += x
                    l[0] = l[-1]
                    l = l[0:1]
                    m.append(str_)
                # 由于处理算法原因，导致最后一章节无法获取，故加此条件进行处理，存储最后一章节
                elif x == txts[-1]:
                    str_ = ""
                    for x in l:
                        str_ += x
                    m.append(str_)
            # 对章节编号为汉字的进行处理 转换为数字
            i = 0
            while i < len(s):
                s[i] = self.chinese2digits(s[i])
                i += 1
            # 由于最初读取第一章时，进入了处理算法，而其章节内容此时为空，故列表s新增一位才可与m生成相对应的dict
            s.insert(0, "0")
            # 生成dict,s为key,m为value   由于字典key的唯一性，再进行dict生成时自动剔除了重复的章节
            d = dict(zip(s, m))
            # 对dict安装key进行排序，reverse:排序规则，bool值（默认为升序排列（False））
            # item[0]表示按键排序，item[1]则表示按值排序   而单独使用item[0]，测试发现排序逻辑和期望不符，故此使用int(item[0])
            # 返回值为元组列表的形式 eg:[('no', 2), ('ok', 1)]
            by_key = sorted(d.items(), key=lambda item: int(item[0]), reverse=False)
            # 返回一个路径的目录名和文件名
            p = os.path.split(self.__path)
            # 新建排序完成的txt文件（在提供的该目录下-->文件名_新.txt）
            self.new_path = p[0] + "\\" + os.path.splitext(p[1])[0] + '_新.txt'
            # 写入文件
            fw = open(self.new_path, 'w', encoding="utf-8")
            for x in by_key:
                #print(x[0])
                fw.write(x[1])
        finally:
            fr.close()
            fw.close()

        reg="重组成功"
        return reg

    #将中文章节表达转换为阿拉伯数字表达
    def chinese2digits(self,uchars_chinese):
        total = 0
        r = 1  # 表示单位：个十百千...
        if uchars_chinese.isdigit():
            total = uchars_chinese
        else:
            for i in range(len(uchars_chinese) - 1, -1, -1):
                val = self.__common_used_numerals.get(uchars_chinese[i])
                if val >= 10 and i == 0:  # 应对 十三 十四 十*之类
                    if val > r:
                        r = val
                        total = total + val
                    else:
                        r = r * val
                elif val >= 10:
                    if val > r:
                        r = val
                    else:
                        r = r * val
                else:
                    total = total + r * val

        return total


if __name__ =="__main__":
    app=QtWidgets.QApplication(sys.argv)
    fiction_sort_form=Fiction_Sort_Form()
    fiction_sort_form.show()
    sys.exit(app.exec_())
