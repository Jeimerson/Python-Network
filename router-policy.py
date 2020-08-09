import re
import os

def routepolicy(J):
    arq = open('Juniper-Policy.txt','w')
    count = 0
    file = open('asn-list.txt', 'r')
    t = []
    for line in file.readlines():
        line = line.rstrip()
        t.append(line)
    for i in range(len(t)):
           if 'AS' in t[i]:   
                count = count + 1
                print('set policy-options policy-statement eBGP-DOWNSTREAM-ASN-1234-SPO-IN term {}-V4'.format(t[i]),'from route-filter {} upto /24'.format(t[i+1]),file=arq) 
                print('set policy-options policy-statement eBGP-DOWNSTREAM-ASN-1234-SPO-IN term {}-V4'.format(t[i]),'then local-preference 700',file=arq)
                print('set policy-options policy-statement eBGP-DOWNSTREAM-ASN-1234-SPO-IN term {}-V4'.format(t[i]),'then community set COSTOMER-ISP',file=arq)
                print('set policy-options policy-statement eBGP-DOWNSTREAM-ASN-1234-SPO-IN term {}-V4'.format(t[i]),'then community add EXPORT-ONLY-ISP2',file=arq)
                print('set policy-options policy-statement eBGP-DOWNSTREAM-ASN-1234-SPO-IN term {}-V4'.format(t[i]),'then accept''\n',file=arq)
                print('------------------------------------------------------------------------------------------------',file=arq)
    print('Junos OS')        
    print('Foram configuradas',count,'Routing Policy')

def routemap(C_XE):
    arq = open('Cisco-XE-Route-Map.txt','w')
    count = 0
    file = open('asn-list.txt', 'r')
    t = []
    for line in file.readlines():
        line = line.rstrip()
        t.append(line)
    for i in range(len(t)):
           if 'AS' in t[i]:   
                count = count + 1
                print('ip prefix-list PL-{}-V4'.format(t[i]),'seq 1 permit {} le 24''\n'.format(t[i+1]),file=arq) 
                print('route-map eBGP-DOWNSTREAM-ASN-{}-V4-IN'.format(t[i]),'permit 100',file=arq)
                print('match ip address prefix-list PL-{}-V4'.format(t[i]),file=arq)
                print('set local-preference 700',file=arq)
                print('set community 1234:200 1234:243 1234:1023 1234:1043 additive''\n',file=arq)
                print('------------------------------------------------------------------------------------------------',file=arq)
    print('Cisco IOS-XE')
    print('Foram configuradas',count,'Route Map')
    
def route_policy_xr(C_XR):
    arq = open('Cisco-XR-Route-Policy.txt','w')
    count = 0
    file = open('asn-list.txt', 'r')
    t = []
    for line in file.readlines():
        line = line.rstrip()
        t.append(line)
    for i in range(len(t)):
           if 'AS' in t[i]:   
                count = count + 1
                print('prefix-set PL-{}-V4 \n'.format(t[i]),' {} ge 22 le 24'.format(t[i+1]),file=arq) 
                print('end-set\n',file=arq)
                print('route-policy eBGP-DOWNSTREAM-ASN-{}-V4-IN'.format(t[i]),file=arq)
                print('  if destination in PL-{}-V4 then'.format(t[i]),file=arq)
                print('    set local-preference 700',file=arq)
                print('    set community COSTOMER-ISP additive',file=arq)
                print('    set community EXPORT-ONLY-ISP2 additive',file=arq)
                print('    done \n',' ''endif',file=arq)
                print('------------------------------------------------------------------------------------------------',file=arq)
    print('Cisco IOS-XR')
    print('Foram configuradas',count,'Route Policy')


def route_policy(H):
    arq = open('Huawei-Route-Policy.txt','w')
    count = 0
    file = open('asn-list.txt', 'r')
    t = []
    for line in file.readlines():
        line = line.rstrip()
        t.append(line)
    for i in range(len(t)):
           if 'AS' in t[i]:   
                count = count + 1
                print('ip ip-prefix PL-{}-V4'.format(t[i]),'index 10 permit {}  24''\n'.format(t[i+1]),file=arq) 
                print('route-policy eBGP-DOWNSTREAM-ASN-{}-V4-IN'.format(t[i]),'permit node 100',file=arq)
                print('if-match ip-prefix PL-{}-V4'.format(t[i]),file=arq)
                print('apply local-preference 700',file=arq)
                print('apply community 1234:200 1234:243 1234:1023 1234:1043 additive''\n',file=arq)
                print('------------------------------------------------------------------------------------------------',file=arq)
    print('Huawei VRP')
    print('Foram configuradas',count,'Route Policy')

opcao = -1
while opcao != 0:
    print('Escolha a Policy a ser configurada: ')
    print()
    print('1 - Juniper')
    print('2 - Cisco-XE')
    print('3 - Cisco-XR')
    print('4 - Huawei')
    print('0 - Sair')
    print()
    opcao = int(input('Entre com o número da opção desejada: '))
    if (opcao == 1):
        J = ''
        routepolicy(J)
    elif (opcao == 2):
        C_XE = ''
        routemap(C_XE)
    elif (opcao == 3):
        C_XR = ''
        route_policy_xr(C_XR)
    elif (opcao == 4):
        H = ''
        route_policy(H)



