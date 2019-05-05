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
    result = get_dir + '/结果输出/' + d1 + '_show lldp neighbor.txt'
    if os.path.exists(result):
        os.remove(result)
    with open(result, 'a') as w:
        w.write('本端设备\t' + '本端接口\t' + '对端设备\t' + '对端接口\n')
    total = 0
    for d2 in dir2:
        os.chdir(pwd2 + '/' + d2)
        pwd3 = os.getcwd()
        dir3 = os.listdir(pwd2 + '/' + d2)
        hostname = d2
        for file in dir3:
            if 'show lldp neighbor.txt' in file:
                with open(file, 'r') as r:
                    total = total + 1
                    show_file = r.read()
                    temp = show_file.replace('\n       ', '\t').replace('120        BR', '\t').replace('121        BR', '\t')
                    lines = temp.split('\n')
                    hostname_temp = hostname.split('_')                        # 分割IP地址和Hostname
                    module_temp = hostname_temp[1].split('-')                  # 分割hostname，提取前两个字段
                    module = module_temp[0] + '-' + module_temp[1] + '-'
                    print(module)
                    for line in lines:
                        if '#' in line:
                            pass
                        elif module in line:
                            l_2_r = line.split('\t')
                            remote_dev = l_2_r[0].replace(' ', '')
                            local_port = l_2_r[1].replace('Eth', 'Ethernet').replace(' ', '')
                            remote_port = l_2_r[2].replace(' ', '')
                            with open(result, 'a') as w:
                                w.write(hostname_temp[1] + '\t' + local_port + '\t' + remote_dev + '\t' + remote_port + '\n')
                        elif 'Total entries displayed:' in line:
                            with open(result, 'a') as w:
                                w.write(hostname_temp[1] + '\t\t\t\t' + line.replace('Total entries displayed','LLDP邻居合计') + '\n')
    with open(result, 'a') as w:
        w.write('成功处理' + str(total) + '台设备。')
