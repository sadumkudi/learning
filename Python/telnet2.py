import getpass
import sys
import telnetlib
import time

Host=”192.168.43.10?

user=input(“Enter User name”)
password=getpass.getpass()

tn = telnetlib.Telnet(Host)
tn.read_until(b”Username: “)
tn.write(user.encode(‘ascii’) + b”\n”)

if password:
tn.read_until(b”Password: “)
tn.write(password.encode(‘ascii’)+b”\n”)
time.sleep(2)
tn.write(b”enable\n”)
time.sleep(2)
tn.write(b”admin\n”)
time.sleep(2)
tn.write(b”config t\n”)
time.sleep(2)
tn.write(b”int vlan 10\n”)
time.sleep(2)
tn.write(b”ip add 10.10.10.10 255.255.255.0\n”)

tn.write(“end\n”)
tn.write(“exit\n”)
line=tn.read_all()
 print (line)
