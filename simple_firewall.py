# Form implementation generated from reading ui file 'simple_firewall.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import subprocess

from PyQt6 import QtCore, QtGui, QtWidgets
from addRule import add_rule_Dialog
from addRule2 import add_rule_Dialog


class Simple_Firewall_Dialog(object):
    llist = add_rule_Dialog.llist
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(584, 394)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 561, 341))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setStyleSheet("QTabWidget{\n"
                                           "    background-color:rgb(144, 238, 144)\n"
                                           "}")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.layoutWidget = QtWidgets.QWidget(self.tab_1)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 50, 551, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_web_address = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_web_address.setFont(font)
        self.label_web_address.setObjectName("label_web_address")
        self.horizontalLayout.addWidget(self.label_web_address)
        self.lineEdit_web_address = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_web_address.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_web_address.setObjectName("lineEdit_web_address")
        self.horizontalLayout.addWidget(self.lineEdit_web_address)
        self.widget = QtWidgets.QWidget(self.tab_1)
        self.widget.setGeometry(QtCore.QRect(20, 160, 531, 101))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_block = QtWidgets.QPushButton(self.widget)
        self.pushButton_block.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.pushButton_block.setFont(font)
        self.pushButton_block.setAutoDefault(False)
        self.pushButton_block.setDefault(True)
        self.pushButton_block.setObjectName("pushButton_block")

        #connect signal
        self.pushButton_block.clicked.connect(self.block_website)

        self.horizontalLayout_2.addWidget(self.pushButton_block)
        self.pushButton_unblock = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_unblock.sizePolicy().hasHeightForWidth())
        self.pushButton_unblock.setSizePolicy(sizePolicy)
        self.pushButton_unblock.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_unblock.setFont(font)
        self.pushButton_unblock.setAutoDefault(False)
        self.pushButton_unblock.setDefault(True)
        self.pushButton_unblock.setObjectName("pushButton_unblock")

        #connect signal
        self.pushButton_unblock.clicked.connect(self.unblock_website)

        self.horizontalLayout_2.addWidget(self.pushButton_unblock)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_web_block_msg = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_web_block_msg.setFont(font)
        self.label_web_block_msg.setObjectName("label_web_block_msg")
        self.verticalLayout.addWidget(self.label_web_block_msg)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget1 = QtWidgets.QWidget(self.tab_2)
        self.widget1.setGeometry(QtCore.QRect(10, 160, 531, 101))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_block_ip = QtWidgets.QPushButton(self.widget1)
        self.pushButton_block_ip.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.pushButton_block_ip.setFont(font)
        self.pushButton_block_ip.setAutoDefault(False)
        self.pushButton_block_ip.setDefault(True)
        self.pushButton_block_ip.setObjectName("pushButton_block_ip")

        #connect signal
        self.pushButton_block_ip.clicked.connect(self.block_ip_address)

        self.horizontalLayout_4.addWidget(self.pushButton_block_ip)
        self.pushButton_unblock_ip = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_unblock_ip.sizePolicy().hasHeightForWidth())
        self.pushButton_unblock_ip.setSizePolicy(sizePolicy)
        self.pushButton_unblock_ip.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_unblock_ip.setFont(font)
        self.pushButton_unblock_ip.setAutoDefault(False)
        self.pushButton_unblock_ip.setDefault(True)
        self.pushButton_unblock_ip.setObjectName("pushButton_unblock_ip")

        #connect signal
        self.pushButton_unblock_ip.clicked.connect(self.unblock_ip_address)

        self.horizontalLayout_4.addWidget(self.pushButton_unblock_ip)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label_ip_block_msg = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_ip_block_msg.setFont(font)
        self.label_ip_block_msg.setObjectName("label_ip_block_msg")
        self.verticalLayout_2.addWidget(self.label_ip_block_msg)
        self.widget2 = QtWidgets.QWidget(self.tab_2)
        self.widget2.setGeometry(QtCore.QRect(130, 50, 331, 41))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_ipaddress = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_ipaddress.setFont(font)
        self.label_ipaddress.setObjectName("label_ipaddress")
        self.horizontalLayout_3.addWidget(self.label_ipaddress)
        self.lineEdit_ip_address = QtWidgets.QLineEdit(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ip_address.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip_address.setSizePolicy(sizePolicy)
        self.lineEdit_ip_address.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_ip_address.setFont(font)
        self.lineEdit_ip_address.setObjectName("lineEdit_ip_address")
        self.horizontalLayout_3.addWidget(self.lineEdit_ip_address)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(150, 40, 221, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_ipaddress_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_ipaddress_2.setFont(font)
        self.label_ipaddress_2.setObjectName("label_ipaddress_2")
        self.horizontalLayout_5.addWidget(self.label_ipaddress_2)
        self.lineEdit_port = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_port.sizePolicy().hasHeightForWidth())
        self.lineEdit_port.setSizePolicy(sizePolicy)
        self.lineEdit_port.setMaximumSize(QtCore.QSize(70, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_port.setFont(font)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.horizontalLayout_5.addWidget(self.lineEdit_port)
        self.widget3 = QtWidgets.QWidget(self.tab)
        self.widget3.setGeometry(QtCore.QRect(9, 140, 531, 131))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_block_port = QtWidgets.QPushButton(self.widget3)
        self.pushButton_block_port.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.pushButton_block_port.setFont(font)
        self.pushButton_block_port.setAutoDefault(False)
        self.pushButton_block_port.setDefault(True)
        self.pushButton_block_port.setObjectName("pushButton_block_port")

        #connect signal
        self.pushButton_block_port.clicked.connect(self.block_port)

        self.horizontalLayout_6.addWidget(self.pushButton_block_port)
        self.pushButton_unblock_port = QtWidgets.QPushButton(self.widget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_unblock_port.sizePolicy().hasHeightForWidth())
        self.pushButton_unblock_port.setSizePolicy(sizePolicy)
        self.pushButton_unblock_port.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_unblock_port.setFont(font)
        self.pushButton_unblock_port.setAutoDefault(False)
        self.pushButton_unblock_port.setDefault(True)
        self.pushButton_unblock_port.setObjectName("pushButton_unblock_port")

        #connect signal
        self.pushButton_unblock_port.clicked.connect(self.unblock_port)

        self.horizontalLayout_6.addWidget(self.pushButton_unblock_port)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.label_port_block_msg = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_port_block_msg.setFont(font)
        self.label_port_block_msg.setObjectName("label_port_block_msg")
        self.verticalLayout_3.addWidget(self.label_port_block_msg)
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def block_website(self):

        query = ""
        website = self.lineEdit_web_address.text()
        data = add_rule_Dialog.llist.search(5,website)
        if data is not None:
            if data[6]=="DROP":
                self.label_web_block_msg.setText("The "+website+" is already blocked.")
        elif data is None and website!="":
            query = "iptables -t filter -A OUTPUT -p tcp --dport 443 -d " + website + " -j DROP"
            self.llist.insert('filter','OUTPUT','tcp','443','', website,'DROP')
            self.llist.print_list()
        if website!="":
            add_rule_Dialog.append_new_rule(self,query)
            subprocess.call(['bash', 'firewall.sh'])
            self.label_web_block_msg.setText("Website " + website + " is blocked")
            self.lineEdit_web_address.setText("")
        else:
            print("Error")
    def unblock_website(self):

        website = self.lineEdit_web_address.text()
        query = "iptables -t filter -A OUTPUT -p tcp --dport 443 -d " + website + " -j ACCEPT"
        if website!="":
            add_rule_Dialog.append_new_rule(self,query)
            subprocess.call(['bash', 'firewall.sh'])
            self.label_web_block_msg.setText("Website " + website + " is unblocked")
            self.lineEdit_web_address.setText("")
        else:
            self.label_web_block_msg.setText("Error in unblocking the website")
    def block_ip_address(self):
        ipAddress = self.lineEdit_ip_address.text()
        if ipAddress!="":
            query = "iptables -A INPUT -s "+ ipAddress + " -j DROP"
            add_rule_Dialog.append_new_rule(self,query)
            self.label_ip_block_msg.setText("Ip address " + ipAddress + " is blocked")
            self.lineEdit_ip_address.setText("")
        else:
            self.label_ip_block_msg.setText("Error in blocking the ip address")

    def unblock_ip_address(self):
        ipAddress = self.lineEdit_ip_address.text()
        if ipAddress!="":
            query = "iptables -A INPUT -s "+ ipAddress + " -j ACCEPT"
            add_rule_Dialog.append_new_rule(self,query)
            self.label_ip_block_msg.setText("Ip address " + ipAddress + " is unblocked")
            self.lineEdit_ip_address.setText("")
        else:
            self.label_ip_block_msg.setText("Error in unblocking the ip address")

    def block_port(self):
        port = self.lineEdit_port.text()
        if port!="":
            if port!="53" and port!="68":
                query = "iptables -A INPUT -p tcp --dport "+ port + " -j DROP"
            else:
                query = "iptables -A INPUT -p udp --dport " + port + " -j DROP"
            add_rule_Dialog.append_new_rule(self,query)
            self.label_port_block_msg.setText("Port " + port + " is blocked")
            self.lineEdit_port.setText("")
        else:
            self.label_port_block_msg.setText("Error in blocking the port ")


    def unblock_port(self):
        port = self.lineEdit_port.text()
        if port!="":
            if port!="53" and port!="68":
                query = "iptables -A INPUT -p tcp --dport "+ port + " -j ACCEPT"
            else:
                query = "iptables -A INPUT -p udp --dport " + port + " -j ACCEPT"
            add_rule_Dialog.append_new_rule(self,query)
            self.label_port_block_msg.setText("Port " + port + " is unblocked")
            self.lineEdit_port.setText("")
        else:
            self.label_port_block_msg.setText("Error in unblocking the port ")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Firewall"))
        self.label_web_address.setText(_translate("Dialog", "Website Address"))
        self.lineEdit_web_address.setPlaceholderText(_translate("Dialog", "www.google.com"))
        self.pushButton_block.setText(_translate("Dialog", "Block"))
        self.pushButton_unblock.setText(_translate("Dialog", "Unblock"))
        self.label_web_block_msg.setText(_translate("Dialog", "Message"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Dialog", "Website"))
        self.pushButton_block_ip.setText(_translate("Dialog", "Block"))
        self.pushButton_unblock_ip.setText(_translate("Dialog", "Unblock"))
        self.label_ip_block_msg.setText(_translate("Dialog", "Message"))
        self.label_ipaddress.setText(_translate("Dialog", "IP ADDRESS"))
        self.lineEdit_ip_address.setPlaceholderText(_translate("Dialog", "192.168.104.104"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "IP Address"))
        self.label_ipaddress_2.setText(_translate("Dialog", " PORT # "))
        self.lineEdit_port.setPlaceholderText(_translate("Dialog", "47"))
        self.pushButton_block_port.setText(_translate("Dialog", "Block"))
        self.pushButton_unblock_port.setText(_translate("Dialog", "Unblock"))
        self.label_port_block_msg.setText(_translate("Dialog", "Message"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "PORT"))


