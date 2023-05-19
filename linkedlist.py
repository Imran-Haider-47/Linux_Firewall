import ipaddress
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def search(self, index,data):
        current = self.head
        while current is not None:
            if current[index] == data:
                return current.data
            current = current.next
        return None

    def delete(self, index,data):
        if self.head is None:
            return
        if self.head.data[index] == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data[index] == data:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current is not None:
            
            Query = ""
            if current.data[0] == "None" or current.data[0] == "FILTER":
                Query = "iptables -t filter"
            else:
                Query = "iptables -t " + str(current.data[0] )+" "
            if current.data[1] != "None":
                Query = Query + " -A " + str(current.data[1])
            if str(current.data[2] )!= "None":
                Query = Query + " -p " + str(current.data[2])

            # port validity
            port_validity = False
            if str(current.data[3]) != "":
                if int(current.data[3]) <= 1 or int(current.data[3]) > 65535:
                    port_validity = False
                else:
                    port_validity = True
            if port_validity == True:
                Query = Query + " --dport " + current.data[3]

            # ip address validity
            ipValidity = False
            if current.data[4] != "":
                ip_validity = self.validate_ip_address(current.data[4])
                if ip_validity == False:
                    ipValidity = False

                else:
                    ipValidity == True
            if current.data[4] != "" and self.validate_ip_address(current.data[4]) == True:
                Query = Query + " -s " + current.data[4]

            if current.data[5] != '':
                Query = Query + " -d " + current.data[5]
            if current.data[6] != 'None':
                Query = Query + " -j " + current.data[6]

            print(Query)
            self.append_new_rule(Query)
            current = current.next

    def validate_ip_address(self, ip_string):
        try:
            ip_object = ipaddress.ip_address(ip_string)
            return True
        except ValueError:
            return False

    def append_new_rule(self, new_rule):
        with open('firewall.sh', 'a') as rsh:
            rsh.write("\n" + new_rule)


# # Example usage:
# llist = LinkedList()
# llist.insert(["1", "data1"," 2.5",'', "extra1", '', "more data1"])
# llist.insert(["2", "data2", "3.5", '', "extra2", '', "more data2"])
# llist.insert(["3", "data3", "4.5", '', "extra3", '', "more data3"])

# llist.print_list()
# llist.print_list()
# print(llist.search("data1"))  # Output: [2, 'data2', 3.5, False, 'extra2', None, 'more data2']
#
#llist.delete(4,"extra3")
# print(llist.search(2))  # Output: None

# def validate_ip_address(self, ip_string):
#     try:
#         ip_object = ipaddress.ip_address(ip_string)
#         return True
#     except ValueError:
#         return False

# def append_new_rule(self,new_rule):
#     with open('firewall.sh', 'a') as rsh:
#         rsh.write("\n"+new_rule)

# for data in llist:
#
#     Query = ""
#     if current.data[0] == "None" or current.data[0] == "FILTER":
#         Query = "iptables -t filter"
#     else:
#         Query = "iptables -t " + current.data[0]
#     if current.data[1] != "None":
#         Query = Query + " -A " + current.data[1]
#     if current.data[2] != "None":
#         Query = Query + " -p " + current.data[2]
#
#     #port validity
#     if current.data[3] != "":
#         if int(current.data[3]) <= 1 or int(current.data[3]) > 65535:
#             msg = msg + f"Port '{current.data[3]}' is invalid. "
#         else:
#             port_validity = True
#
#     if port_validity == True:
#         Query = Query + " --dport " + current.data[3]
#
#     #ip address validity
#     ipValidity = False
#     if current.data[4] != "":
#         ip_validity = validate_ip_address(current.data[4])
#         if ip_validity == False:
#             msg = msg + f"The IP address '{current.data[4]}' is not valid"
#
#         else:
#             ipValidity == True
#     if ipaddress != "" and validate_ip_address(current.data[4]) == True:
#         Query = Query + " -s " + current.data[4]
#
#
#     if current.data[5] != '':
#         Query = Query + " -d " + current.data[5]
#     if current.data[6] != 'None':
#         Query = Query + " -j " + current.data[6]
#
#     print(Query)
#     # if llist.search(3,4,5) is not None:
#     #     llist.delete(3,4,5)




