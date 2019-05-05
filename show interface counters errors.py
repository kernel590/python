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
    result = get_dir + '/结果输出/' + d1 + '_show interface counters errors.txt'
    if os.path.exists(result):
        os.remove(result)
    total = 0
    with open(result, 'a') as w:
        w.write('管理地址_设备名称\t接口\t检查结论\n')
    for d2 in dir2:
        os.chdir(pwd2 + '/' + d2)
        pwd3 = os.getcwd()
        dir3 = os.listdir(pwd2 + '/' + d2)
        hostname = d2
        for file in dir3:
            if 'show interface counters errors.txt' in file:
                with open(file, 'r') as r:
                    total = total + 1
                    with open(result, 'a') as w:
                        for line in r.readlines():
                            if 'mgmt0' in line or 'Eth' in line:
                                str1 = line.replace('\n', '').split(' ')
                                str2 = list(filter(None, str1))         
                                interface = str2[0]
                                # w.write(hostname + '\t')
                                i = 0
                                for str3 in str2:
                                    if 'Eth' in str3 or 'mgmt0' in str3 or '--' in str3:
                                        pass
                                    elif int(str3) != 0:
                                        i = i + 1
                                    else:
                                        pass
                                if i != 0:
                                    w.write(hostname + '\t' + interface + '\t不通过\n')
                                else:
                                    w.write(hostname + '\t' + interface + '\t通过\n')
                            elif 'Po' in line and 'Port' not in line:
                                str1 = line.replace('\n', '').split(' ')
                                str2 = list(filter(None, str1))  
                                interface = str2[0]
                                for str3 in str2:
                                    if 'Po' in str3 or '--' in str3:
                                        pass
                                    elif int(str3) != 0:
                                        i = i + 1
                                    else:
                                        pass
                                if i != 0:
                                    w.write(hostname + '\t' + interface + '\t不通过\n')
                                else:
                                    w.write(hostname + '\t' + interface + '\t通过\n')
    with open(result, 'a') as w:
        w.write('成功处理' + str(total) + '台设备。')
