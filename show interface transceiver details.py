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
    result = get_dir + '/结果输出/' + d1 + '_show interface transceiver details.txt'
    if os.path.exists(result):
        os.remove(result)
    with open(result, 'a') as w:
        w.write('管理地址_设备名称\t接口\t收发光是否正常\t当前值(dBm)\t检查结论\n')
    total = 0
    for d2 in dir2:
        os.chdir(pwd2 + '/' + d2)
        pwd3 = os.getcwd()
        dir3 = os.listdir(pwd2 + '/' + d2)
        hostname = d2
        for file in dir3:
            if 'show interface transceiver details.txt' in file:
                with open(file, 'r') as r:
                    total = total + 1
                    with open(result, 'a') as w:
                        str1 = r.read()                                      
                        str2 = str1.replace('\nEthernet', '_#\nEthernet')    
                        str3 = str2.split('_#')                              
                        for str4 in str3:
                            if 'transceiver is present' in str4:             
                               str5 = str4.split('\n')                       
                               for str6 in str5:
                                   if 'Ethernet' in str6:                    
                                       interface = str6
                                   elif 'Tx Power' in str6 and 'N/A' not in str6:  
                                       str7 = str6.replace('Power', 'Power dBm').replace(' ', '')
                                       str8 = str7.split('dBm')
                                       if float(str8[5]) < float(str8[1]) < float(str8[4]):
                                           w.write(hostname + '\t' + interface + '\t发光正常\t' + str8[1] + '\t通过\n')
                                       else:
                                           w.write(hostname + '\t' + interface + '\t发光异常\t' + str8[1] + '\t未通过\n')
                                   elif 'Rx Power' in str6 and 'N/A' not in str6:  
                                       str7 = str6.replace('Power', 'Power dBm').replace(' ', '')
                                       str8 = str7.split('dBm')
                                       if float(str8[5]) < float(str8[1]) < float(str8[4]):
                                           w.write(hostname + '\t' + interface + '\t收光正常\t' + str8[1] + '\t通过\n')
                                       else:
                                           w.write(hostname + '\t' + interface + '\t收光异常\t' + str8[1] + '\t未通过\n')
                                   elif 'Tx Power' in str6 and 'N/A' in str6:      
                                       w.write(hostname + '\t' + interface + '\t收光异常\tN/A' + '\t未通过\n')
                                   elif 'Rx Power' in str6 and 'N/A' in str6:       
                                       w.write(hostname + '\t' + interface + '\t发光异常\tN/A' + '\t未通过\n')
    with open(result, 'a') as w:
        w.write('成功处理' + str(total) + '台设备。')
