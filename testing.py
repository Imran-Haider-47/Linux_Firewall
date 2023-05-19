from array import *
query = "iptables"
table = "filter"
chain = "Input "
query = query + " " + table + " " + chain
#print(query)

ip = "127.0.0.1"
dots=0
for letter in ip:
    if letter == '.':
       dots+=1


def fetch_rules_test():
    rule = []
    with open('firewall.sh', 'r') as rsh:
        i= 0
        while(rsh):
            line = rsh.readline()
            if line=="\n":
                continue
            if line == "":
                break
            line = line.split()
            table = ""
            chain = ""
            port = ""
            website = ""
            ip_add = ""
            traffic = ""
            action = ""
            for e in line:

                if e == '-t':
                    table= line[line.index(e)+1]
                    #print(table)
                if e=='-A':
                    chain = line[line.index(e)+1]
                    #print(chain)
                if e=='-p':
                    traffic= line[line.index(e)+1]
                    #print(traffic)
                if e=='--dport':
                    port= line[line.index(e)+1]
                    #print(port)
                if e =='-s':
                    ip_add = line[line.index(e)+1]
                    #print(ip_add)
                if e == '-j':
                    action = line[line.index(e)+1]
                    #print(action)
            if table=="" and action!="":
                table="filter"
            if action!="":
                rule.append([table,chain,traffic,port,website,ip_add,action])
        print(rule)


fetch_rules_test()


