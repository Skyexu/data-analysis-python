# -*- coding: utf-8 -*-

# @Author  : Skye
# @Time    : 2017/11/17 13:58
# @desc    : 科技工作者心理健康数据分析 (Mental Health in Tech Survey)
#            统计不同国家男女人数

import csv

data_path = './survey.csv'


def run():
    male_set = {'male','m'} # 男性的取值集合
    female_set = {'female','f'} # 男性的取值集合

    # 结果存储字典 如 {'United States': [20, 50], 'Canada': [30, 40]}
    #  [20, 50] 分别表示男，女数量
    result_dic = {}

    with open(data_path, 'r') as csvfile:
        rows = csv.reader(csvfile)

        for i,row in enumerate(rows):
            if i == 0:
                continue

            if i % 50 == 0:
                print('正在处理第{}行数据...'.format(i))

            gender = row[2]
            country = row[3]

            # 去掉可能存在的空格，并转小写
            gender = gender.replace(' ','')
            gender = gender.lower()

            # 如果结果字典中不存在当前国家，则加入
            if country not in result_dic:
                result_dic[country] = [0,0]

            if gender in male_set:
                result_dic[country][0] += 1
            elif gender in female_set:
                result_dic[country][1] += 1

    # 存入统计结果
    with open('./gender_country.csv', 'w',newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(['国家','男性','女性'])

        for k, v in result_dic.items():
            csv_writer.writerow([k, v[0], v[1]])

if __name__ == '__main__':
    run()
