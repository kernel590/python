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
    result = get_dir + '/结果输出/' + d1 + '_show cores.txt'
    if os.path.exists(result):
        os.remove(result)
    total = 0
    with open(result, 'a') as w:
        w.write('管理地址_设备名称\t是否存在cores文件\t检查结论\n')
    for d2 in dir2:
        os.chdir(pwd2 + '/' + d2)
        pwd3 = os.getcwd()
        dir3 = os.listdir(pwd2 + '/' + d2)
        hostname = d2
        for file in dir3:
            if 'show cores.txt' in file:
                with open(file, 'r') as r:
                    total = total + 1
                    flag = False
                    for line in r.readlines():
                        if 'core' in line and 'show' not in line:
                            flag = True
                        else:
                            pass
                    if flag is False:
                        with open(result, 'a') as w:
                            w.write(hostname + '\t否\t通过\n')
                    else:
                        with open(result, 'a') as w:
                            w.write(hostname + '\t是\t未通过\n')
    with open(result, 'a') as w:
        w.write('成功处理' + str(total) + '台设备。')
