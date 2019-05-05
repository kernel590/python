import os
get_dir = os.path.abspath(os.path.dirname(os.getcwd()))
os.chdir(get_dir)
if os.path.exists("结果输出"):
    pass
else:
    os.mkdir("结果输出")
os.chdir(get_dir + '/巡检信息')
pwd1 = os.getcwd()
dir1 = os.listdir(pwd1)
for d1 in dir1:
    os.chdir(pwd1 + '/' + d1)
    pwd2 = os.getcwd()
    dir2 = os.listdir(pwd2)
    result = get_dir + '/结果输出/' + d1 + '_show module.txt'
    if os.path.exists(result):
        os.remove(result)
    with open(result, 'a') as w:
        w.write('管理地址_设备名称\t模块\t状态\t检查结论\n')
    total = 0
    for d2 in dir2:
        os.chdir(pwd2 + '/' + d2)
        pwd3 = os.getcwd()
        dir3 = os.listdir(pwd2 + '/' + d2)
        hostname = d2
        for file in dir3:
            if 'show module.txt' in file and 'slot' not in file:
                with open(file, 'r') as r:
                    total = total + 1
                    with open(result, 'a') as w:
                        for line in r.readlines():
                            if 'N9K-' in line:
                                str1 = line.replace('\n', '').replace('*', '').split(' ')
                                str2 = list(filter(None, str1))                                 # 过滤空字符('')和None
                                w.write(hostname + '\t' + str2[-2] + '\t' + str2[-1] + '\n')
    with open(result, 'a') as w:
        w.write('成功处理' + str(total) + '台设备。')
