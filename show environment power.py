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
    result = get_dir + '/结果输出/' + d1 + '_show environment power.txt'
    if os.path.exists(result):
        os.remove(result)
    total = 0
    with open(result, 'a') as w:
        w.write('管理地址_设备名称\t电源总数量\t故障数量\t检查结论\n')
    for d2 in dir2:
        os.chdir(pwd2 + '/' + d2)
        pwd3 = os.getcwd()
        dir3 = os.listdir(pwd2 + '/' + d2)
        hostname = d2
        for file in dir3:
            if 'show environment power.txt' in file or 'show env power.txt' in file:
                with open(file, 'r') as r:
                    total = total + 1
                    power_number_ok = 0
                    power_number_fail = 0
                    for line in r.readlines():
                        if 'N9K-PUV-' in line and 'Ok' not in line:
                            power_number_fail = power_number_fail + 1
                        elif 'N9K-PUV-' in line and 'Ok' in line:
                            power_number_ok = power_number_ok + 1
                        elif 'NXA-P' in line and 'Ok' not in line:
                            power_number_fail = power_number_fail + 1
                        elif 'NXA-P' in line and 'Ok' in line:
                            power_number_ok = power_number_ok + 1
                        else:
                            pass
                    with open(result, 'a') as w:
                        if power_number_fail == 0:
                            w.write(hostname + '\t' + str(power_number_ok) + '\t0\t通过\n')
                        else:
                            w.write(hostname + '\t' + str(power_number_ok + power_number_fail) + '\t' + str(power_number_fail) + '\t未通过\n')
    with open(result, 'a') as w:
        w.write('成功处理' + str(total) + '台设备。')

