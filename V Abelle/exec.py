try:
    import socket
except ImportError:
    print("Socket library is not installed. Please install it. CMD: pip install sockets")

try:
    import wmi
except ImportError:
    print("WMI library is not installed. Please install it. CMD: pip install WMI")

try:
    from getmac import get_mac_address as gma
except ImportError:
    print("Getmac library is not installed. Please install it. CMD: pip install getmac")


"""Records the computer data on variables"""
computer = wmi.WMI()
mysystem = computer.Win32_ComputerSystem()[0]
name = str(mysystem.Name)
systype = str(mysystem.SystemType)
hostname = str(socket.gethostname())
ipadrss = str(socket.gethostbyname(hostname))

"""Adds the data to a txt"""
with open('data/computer.txt','r+') as txt:
            txt.truncate(0)
            txt.close()
with open('data/computer.txt','w') as txt:
            txt.writelines(name)
            txt.writelines('\n')
            txt.writelines(systype)
            txt.writelines('\n')
            txt.writelines(ipadrss)
            txt.writelines('\n')
            txt.writelines(gma())
            txt.close()

"""Executes the GameMain or not if the hardware is banned (Actually, it needs a dictionary from banned mac adresses and has to be done by the server or host but I don't have one for the moment)"""
if gma() == '94:de:80:8e:5b:d4':
    print('You were banned from The Huergo Empires')
    exit()
else:
    exec(open('scripts/gamemain.py').read())