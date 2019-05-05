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
    result = get_dir + '/结果输出/' + d1 + '_show interface description.txt'
    if os.path.exists(result):
        os.remove(result)
    total = 0
    with open(result, 'a') as w:
        w.write('本端设备\t' + '本端接口\t' + '对端设备\t' + '对端接口\n')
    for d2 in dir2:
        os.chdir(pwd2 + '/' + d2)
        pwd3 = os.getcwd()
        dir3 = os.listdir(pwd2 + '/' + d2)
        hostname = d2
        for file in dir3:
            if 'show interface description.txt' in file:
                with open(file, 'r') as r:
                    total = total + 1
                    hostname_temp = hostname.split('_')                        # 分割IP地址和Hostname
                    module_temp = hostname_temp[1].split('-')                  # 分割hostname，提取前两个字段
                    module = module_temp[0] + '-' + module_temp[1] + '-'
                    print(module)
                    for line in r.readlines():
                        with open(result, 'a') as w:
                            if '#' in line:
                                pass
                            elif 'mgmt0' in line:
                                desc = line.replace('\n', '').split(' ')
                                desc = list(filter(None, desc))
                                w.write(hostname_temp[1] + '\t' + desc[0] + '\t' + desc[1] + '\n')
                            elif module in line and 'MAN-'in line and 'Eth' in line:                         #  MAN设备
                                desc = line.replace('eth    100G', '_').replace('eth    40G', '_')
                                desc = desc.replace('MAN-01', 'MAN-01_').replace('MAN-02', 'MAN-02_')
                                desc = desc.replace('MAN-03', 'MAN-03_').replace('MAN-04', 'MAN-04_')
                                desc = desc.replace('MAN-05', 'MAN-05_').replace('MAN-06', 'MAN-06_')
                                desc = desc.replace('MAN-07', 'MAN-07_').replace('MAN-08', 'MAN-08_')
                                desc = desc.replace(' ', '')
                                desc = desc.split('_')
                                w.write(hostname_temp[1] + '\t' + desc[0] + '\t' + desc[1] + '\t' + desc[2])
                            elif module in line and 'TIX-' in line and 'Eth' in line:                         #  TIX设备
                                desc = line.replace('eth    100G', '_').replace('eth    40G', '_')
                                desc = desc.replace('TIX-01', 'TIX-01_').replace('TIX-02', 'TIX-02_')
                                desc = desc.replace('TIX-03', 'TIX-03_').replace('TIX-04', 'TIX-04_')
                                desc = desc.replace('TIX-05', 'TIX-05_').replace('TIX-06', 'TIX-06_')
                                desc = desc.replace('TIX-07', 'TIX-07_').replace('TIX-08', 'TIX-08_')
                                desc = desc.replace(' ', '')
                                desc = desc.split('_')
                                w.write(hostname_temp[1] + '\t' + desc[0] + '\t' + desc[1] + '\t' + desc[2])
                            elif module in line and 'AR-'in line and 'Eth' in line:                           # AR设备
                                desc = line.replace('eth    100G', '_').replace('eth    40G', '_')
                                desc = desc.replace('AR-01', 'AR-01_').replace('AR-02', 'AR-02_')
                                desc = desc.replace('AR-03', 'AR-03_').replace('AR-04', 'AR-04_')
                                desc = desc.replace('AR-05', 'AR-05_').replace('AR-06', 'AR-06_')
                                desc = desc.replace('AR-07', 'AR-07_').replace('AR-08', 'AR-08_')
                                desc = desc.replace('AR-09', 'AR-09_').replace('AR-10', 'AR108_')
                                desc = desc.replace(' ', '')
                                desc = desc.split('_')
                                w.write(hostname_temp[1] + '\t' + desc[0] + '\t' + desc[1] + '\t' + desc[2])
                            elif module in line and 'Eth' in line:                                        # IDC内思科设备
                                desc = line.replace('eth    100G', '_').replace('eth    40G', '_').replace('-Eth', '_Eth')
                                desc = desc.replace(' ', '')
                                desc = desc.split('_')
                                w.write(hostname_temp[1] + '\t' + desc[0] + '\t' + desc[1] + '\t' + desc[2])
                            elif module in line and 'Po' in line:
                                desc = line.replace('\n', '').split(' ')
                                desc = list(filter(None, desc))
                                w.write(hostname_temp[1] + '\t' + desc[0] + '\t' + desc[1] + '\n')
    with open(result, 'a') as w:
        w.write('成功处理' + str(total) + '台设备。')
