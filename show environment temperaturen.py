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
    result = get_dir + '/结果输出/' + d1 + '_show environment temperature.txt'
    if os.path.exists(result):
        os.remove(result)
    total = 0
    with open(result, 'a') as w:
        w.write('管理地址_设备名称\tOK出现次数\t检查结论\n')
    for d2 in dir2:
        os.chdir(pwd2 + '/' + d2)
        pwd3 = os.getcwd()
        dir3 = os.listdir(pwd2 + '/' + d2)
        hostname = d2
        for file in dir3:
            if 'show environment temperature.txt' in file or 'show env temperature.txt' in file:
                with open(file, 'r') as r:
                    total = total + 1
                    i = 0
                    for line in r.readlines():
                        if 'Ok' not in line:
                            i = i + 1
                        else:
                            pass
                    with open(result, 'a') as w:
                        w.write(hostname + '\t' + str(i) + '\n')
    with open(result, 'a') as w:
        w.write('成功处理' + str(total) + '台设备。')

