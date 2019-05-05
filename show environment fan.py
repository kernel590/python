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
    result = get_dir + '/结果输出/' + d1 + '_show environment fan.txt'
    if os.path.exists(result):
        os.remove(result)
    total = 0
    with open(result, 'a') as w:
        w.write('管理地址_设备名称\tOK出现次数\t故障数量\t检查结论\n')
    for d2 in dir2:
        os.chdir(pwd2 + '/' + d2)
        pwd3 = os.getcwd()
        dir3 = os.listdir(pwd2 + '/' + d2)
        hostname = d2
        for file in dir3:
            if 'show environment fan.txt' in file or 'show env fan.txt' in file:
                with open(file, 'r') as r:
                    total = total + 1
                    fan_number_ok = 0
                    fan_number_fail = 0
                    for line in r.readlines():
                        if 'front-to-back' in line and 'Ok' not in line:
                            fan_number_fail = fan_number_fail + 1
                        elif 'front-to-back' in line and 'Ok' in line:
                            fan_number_ok = fan_number_ok + 1
                        elif 'back-to-front' in line and 'Ok' not in line:
                            fan_number_fail = fan_number_fail + 1
                        elif 'back-to-front' in line and 'Ok' in line:
                            fan_number_ok = fan_number_ok + 1
                        else:
                            pass
                    with open(result, 'a') as w:
                        if fan_number_fail == 0:
                            w.write(hostname + '\t' + str(fan_number_ok) + '\t0\t通过\n')
                        else:
                            w.write(hostname + '\t' + str(fan_number_ok + fan_number_fail) + '\t' + str(fan_number_fail) + '\t未通过\n')
    with open(result, 'a') as w:
        w.write('成功处理' + str(total) + '台设备。')

