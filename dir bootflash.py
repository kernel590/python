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
    result = get_dir + '/结果输出/' + d1 + '_dir bootflash.txt'
    if os.path.exists(result):
        os.remove(result)
    total = 0
    with open(result, 'a') as w:
        w.write('管理地址_设备名称\tbootflash可用空间\t是否大于500M\t检查结论\n')
    for d2 in dir2:
        os.chdir(pwd2 + '/' + d2)
        pwd3 = os.getcwd()
        dir3 = os.listdir(pwd2 + '/' + d2)
        hostname = d2
        for file in dir3:
            if 'dir bootflash.txt' in file:
                with open(file, 'r') as r:
                    total = total + 1
                    with open(result, 'a') as w:
                        for line in r.readlines():
                            if 'bytes free' in line:
                                temp = line.split(' ')
                                free = int(temp[0])
                                mb = free / 1024 / 1024 // 1
                                if free < 500 * 1024 * 1024:
                                    w.write(hostname + '\t' + str(mb) + 'MB\t否\t未通过\n')
                                else:
                                    w.write(hostname + '\t' + str(mb) + 'MB\t是\t通过\n')
    with open(result, 'a') as w:
        w.write('成功处理' + str(total) + '台设备。')
