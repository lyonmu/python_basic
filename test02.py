from tkinter import *
from tkinter import messagebox
import requests


# 翻译功能函数
def transfor():
    # 获取用户输入内容
    txt = label_into1.get()
    # 检测并去掉多余空格
    txt = txt.strip()
    if txt == '':
        messagebox.showinfo('提示', message='输入为空，请重新输入！')
    else:
        # 爬取有道翻译网站数据
        url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        date = {
            'i': txt,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'bv': 'c2cc50f037b42cb4f36a2ee57addfff2',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        result = requests.post(url, date)
        res = result.json()
        res_Return = res['translateResult'][0][0]['tgt']
        # 显示返回文本
        res_txt.set(res_Return)
        return res_Return


# 窗口界面设计
window = Tk()
window.geometry('500x100+400+200')
window.title('翻译器')

label_txt1 = Label(window, text='请输入翻译内容：', font=('微软雅黑', 15))
label_txt1.grid(row=0, column=0)

label_into1 = Entry(window, font=('宋体', 15), width=30)
label_into1.grid(row=0, column=1)

label_txt2 = Label(window, text='翻译内容：', font=('微软雅黑', 15))
label_txt2.grid(row=1, column=0)

res_txt = StringVar()  # 文本实时变化
label_into2 = Entry(window, font=('宋体', 15), width=30, textvariable=res_txt)  # 使翻译内容显示在框内
label_into2.grid(row=1, column=1)

label_button1 = Button(window, text='转译', width=10, command=transfor)
label_button1.grid(row=2, column=0, sticky=W)

label_button2 = Button(window, text='退出', width=10, command=window.quit)
label_button2.grid(row=2, column=1, sticky=E)

if __name__ == '__main__':
    # 显示窗口
    window.mainloop()
