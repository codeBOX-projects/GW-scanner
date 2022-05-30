#!/bin/env python3

import socket, termcolor, subprocess, netifaces, time

# [code]Box | Andrei A.Abd 2022.
# Source : https://github.com/codeBOX-projects

#clear output terminal
subprocess.call('clear', shell=True)
info = """
░█▀▀█ ░█──░█ 　 ░█▀▀▀█ █▀▀ █▀▀█ █▀▀▄ █▀▀▄ █▀▀ █▀▀█ 
░█─▄▄ ░█░█░█ 　 ─▀▀▀▄▄ █── █▄▄█ █──█ █──█ █▀▀ █▄▄▀ 
░█▄▄█ ░█▄▀▄█ 　 ░█▄▄▄█ ▀▀▀ ▀──▀ ▀──▀ ▀──▀ ▀▀▀ ▀─▀▀
\n
[*] Gateway Scanner - vol 1.0
[*] By Anonymose - (C)opy right for all coders in the world!
[*] This tool scaned 65535 deferent port type and will give you report of results with name & number port. 
"""
print(info)
#get defulte gateway and auto start scan
defulte_gate_way = netifaces.gateways()
gateway = defulte_gate_way['default'][netifaces.AF_INET][0]
#setup socket IP4, TCP protocol type
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#setup Time variable
end = time.time()
start = time.time()
print(f"[>] Found defulte gateway: {termcolor.colored(gateway,'green')}")
print("[>] Setup port scan range ("+termcolor.colored("1,65535", 'white') + ").")
time.sleep(1.5)
print("\n[*] Start Scan:\n")
try:
    for port in range(1,65535):
        #closed ports result:
        if sock.connect_ex((gateway, port)):
            pass
        #opend ports result:
        else:
            print(termcolor.colored("\t* " +  str(port) + " " + socket.getservbyport(port) + " open", 'green'))
            print(termcolor.colored("\n\t[+] Scaning for 65535 ports.\n\t" + f"[+] Time taken {end-start:.2f} seconds",'green'))
except:
    print(termcolor.colored("[!] Error: check ip adress and try again...", 'red'))