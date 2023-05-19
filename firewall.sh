#! /bin/bash 
iptables -F 

iptables -t filter  -A OUTPUT -p TCP --dport 443 -d www.geeksforgeeks.com -j DROP
iptables -t filter -A INPUT -p TCP -s 192.168.104.247 -j ACCEPT