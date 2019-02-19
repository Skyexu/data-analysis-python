# -*- coding: utf-8 -*-

# @Author  : Skye
# @Time    : 2019/2/19 13:11
# @desc    : 简明 python 教程最后的练习题。

import pickle
import os
"""
编写一款你自己的命令行地址簿程序，你可以用它浏览、添加、编辑、删除或搜索你的
联系人，例如你的朋友、家人、同事，还有他们诸如邮件地址、电话号码等多种信息。
这些详细信息必须被妥善储存以备稍后的检索。
"""


class Person:
    def __init__(self,name,email,phone,relationship):
        self.name = name
        self.email = email
        self.phone = phone
        self.relationship = relationship

filename = 'address'

address = dict()

if os.path.exists(filename) :
    f = open(filename, 'rb')
    try:
        address = pickle.load(f)
    except EOFError:
        print("Address is empty")
    f.close()
else:
    f = open(filename, 'wb')
    f.close()

while True:
    choose = int(input("""Please choose a number: \n \
1. 查看所有人\n 2. 按姓名查找\n 3. 添加联系人\n 4. 删除联系人\n 5. 退出\n"""))

    if choose == 5:
        break
    elif choose == 1:
        for name,p in address.items():
            print('{} {} {} {}'.format(name,p.email,p.phone,p.relationship))
    elif choose == 2:
        name = input('Please input name:')
        while not name in address:
            name = input('There\'s no person named {}.Please input right name.'.format(name))
        p = address.get(name)
        print('{} {} {} {}'.format(name, p.email, p.phone, p.relationship))
    elif choose == 3:
        name = input('Please input name:')
        email = input('Please input email:')
        phone = input('Please input phone:')
        relationship = input('Please input relationship:')
        p = Person(name,email,phone,relationship)
        address[name] = p
        f = open(filename, 'wb')
        pickle.dump(address,f)
        f.close()
        print('Save successfully.')
    elif choose == 4:
        name = input('Please input name:')
        while not name in address:
            name = input('There\'s no person named {}.Please input right name.'.format(name))
        address.pop(name)
        f = open(filename, 'wb')
        pickle.dump(address,f)
        f.close()
        print('Delete successfully.')
