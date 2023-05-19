#! /usr/bin/env python

def append_new_rule(new_rule):
    new_rule = "iptables -t filter"
    with open('run.sh', 'a') as rsh:
        print(new_rule)
        rsh.write(f"\ echo  {new_rule} ")
    #     rsh.write('''\
    # echo "I ran this"
    # echo "more lines"
    # echo "appending the rules"
    # ''')

