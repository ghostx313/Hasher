#this tool ia an open source tool for educational purpuses 
import hashlib 
import os 
import time

#created by ghost
class Colours:
    BLACK = "\033[30m"
    GREEN = "\033[32m"
    RESET = "\033[0m"
    YELLOW = "\033[33m"

    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"


def banner():
    print(f"""{Colours.BRIGHT_RED}
               

 ██░ ██  ▄▄▄        ██████  ██░ ██ ▓█████  ██▀███  
▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒███   ▓██ ░▄█ ▒
░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  
░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓░▒████▒░██▓ ▒██▒
 ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
 ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░   ░     ░░   ░ 
 ░  ░  ░      ░  ░      ░   ░  ░  ░   ░  ░   ░     
                     ATHOUR: GHOST
                [!]NOTE THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY!\n                                                                                           
                                                                                                                             
    {Colours.RESET}""")


def clear_screens():
    os.system("clear ")
def show_option():
    print(f"{Colours.YELLOW}==== OPTIONS ====\n{Colours.RESET}")
    print(f"{Colours.GREEN} 1. SHA256 HASHING{Colours.RESET}")
    print(f"{Colours.GREEN} 2. MD5 HASHING{Colours.RESET}")
    print(f"{Colours.GREEN} 3. BLAKE2B HASHING{Colours.RESET}")
    print(f"{Colours.GREEN} 4. SHA3_256{Colours.RESET}")
    print(f"{Colours.GREEN} 5. SHA512{Colours.RESET}")
    print(f"{Colours.GREEN} 6. SHAKE_128{Colours.RESET}")
    print(f"{Colours.GREEN} 7. SHA384{Colours.RESET}")
    print(f"{Colours.GREEN} 8. HASHING A FILE{Colours.RESET}")
    print(f"{Colours.BRIGHT_RED} 0. EXIT ")

def sha256_banner():
    print(f"""{Colours.BRIGHT_GREEN}

███████╗██╗  ██╗ █████╗       ██████╗ ███████╗ ██████╗ 
██╔════╝██║  ██║██╔══██╗      ╚════██╗██╔════╝██╔════╝ 
███████╗███████║███████║█████╗ █████╔╝███████╗███████╗ 
╚════██║██╔══██║██╔══██║╚════╝██╔═══╝ ╚════██║██╔═══██╗
███████║██║  ██║██║  ██║      ███████╗███████║╚██████╔╝
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝      ╚══════╝╚══════╝ ╚═════╝ 
                        
    
    {Colours.RESET}""")

def sha256_hashing():
    clear_screens()
    sha256_banner()
    sha = input(f"{Colours.YELLOW}[+]ENTER TXT YOU WANT TO HASH: {Colours.RESET}")
    HASHER = hashlib.sha256()
    HASHER.update(sha.encode())
    print(f"{Colours.BRIGHT_RED}hash: {Colours.RESET}", HASHER.hexdigest())
    time.sleep(1.5)
    main()

def md5_banner():
    print(f"""{Colours.YELLOW}
    
    
    
    

 _____ ______   ________  ________                   
|\   _ \  _   \|\   ___ \|\   ____\               
\ \  \\\__\ \  \ \  \_|\ \ \  \___|_  
 \ \  \\|__| \  \ \  \ \\ \ \_____  \ 
  \ \  \    \ \  \ \  \_\\ \|____|\  \ 
     \ \  \ \  \ \  \|____|\  \ \  \ \  
   \ \__\    \ \__\ \_______\____\_\  \              
    \|__|     \|__|\|_______|\_________\              
                            \|_________|                          
    {Colours.RESET}""")


def  md5_hashing():
    clear_screens()
    md5_banner()
    RANDOM = input(f"{Colours.BLACK} [+]ENTER TEXT YOU WANT TO HASH: {Colours.RESET}")
    USR =hashlib.md5()
    USR.update(RANDOM.encode())
    print(f"{Colours.BRIGHT_RED}hash: {Colours.RESET}", USR.hexdigest())
    time.sleep(1.5)
    main()

def sha512_banner():
    print(f"""{Colours.BRIGHT_GREEN}




 ________  ___  ___  ________  ________    _____    _______     
|\   ____\|\  \|\  \|\   __  \|\   ____\  / __  \  /  ___  \    
\ \  \___|\ \  \\\  \ \  \|\  \ \  \___|_|\/_|\  \/__/|_/  /|   
 \ \_____  \ \   __  \ \   __  \ \_____  \|/ \ \  \__|//  / /   
  \|____|\  \ \  \ \  \ \  \ \  \|____|\  \   \ \  \  /  /_/__  
    ____\_\  \ \__\ \__\ \__\ \__\____\_\  \   \ \__\|\________
   |\_________\|__|\|__|\|__|\|__|\_________\   \|__| \|_______|
   \|_________|                  \|_________|                   
                                                        

  

     
    {Colours.RESET} """)

def black_banner():
    print(f"""{Colours.BRIGHT_RED}
    
    
    

 ________  ___       ________   _______  ________     
|\   __  \|\  \     |\   ____\ /  ___  \|\   __  \    
\ \  \|\ /\ \  \    \ \  \___|/__/|_/  /\ \  \|\ /_   
 \ \   __  \ \  \    \ \  \   |__|//  / /\ \   __  \  
  \ \  \|\  \ \  \____\ \  \____  /  /_/__\ \  \|\  \ 
   \ \_______\ \_______\ \_______\\________\ \_______
    \|_______|\|_______|\|_______|\|_______|\|_______|
    
    
    
    
    {Colours.RESET}""")

def BLACK2B():
    clear_screens()
    black_banner()
    chioce = input(f"{Colours.BRIGHT_RED}[+]ENTER TEXT YOU WANT TO HASH: {Colours.RESET}")
    SND = hashlib.blake2b()
    SND.update(chioce.encode())
    print(f"{Colours.BRIGHT_RED}hash: {Colours.RESET}", SND.hexdigest())
    time.sleep(5)
    main()

def  SHA3_256():
    clear_screens()
    print(f"{Colours.BRIGHT_GREEN}======= SHA3_256\n ======{Colours.RESET}")
    CMD = input(f"{Colours.BRIGHT_RED}[+]ENTER TEXT YOU WANT TO HASH: {Colours.RESET}")
    OPO = hashlib.sha3_256()
    OPO.update(CMD.encode())
    print(f"{Colours.BRIGHT_RED}hash: {Colours.RESET}", OPO.hexdigest())
    print(f"{Colours.BRIGHT_GREEN}EXITING..........{Colours.RESET}")
    time.sleep(5)
    main()
    


    
    pass


def SHA512():
    clear_screens()
    sha512_banner()

    stats = input(f"{Colours.BLACK} [+]ENTER TEXT YOU WANT TO HASH: {Colours.RESET}")
    fat = hashlib.sha512()
    fat.update(stats.encode())
    print(f"{Colours.BRIGHT_RED}hash: {Colours.RESET}", fat.hexdigest())
    print(f"{Colours.BRIGHT_GREEN}EXITING..........{Colours.RESET}")
    time.sleep(1.6)
    main()

def SHAKE_12():
    clear_screens()
    print(f"{Colours.BRIGHT_GREEN}======= SHAKE_12\n ======{Colours.RESET}")
    STATS = input(f"{Colours.BRIGHT_RED}[+]ENTER TEXT YOU WANT TO HASH: {Colours.RESET}")
    HOME = hashlib.sha3_256()
    HOME.update(STATS.encode())
    print(f"{Colours.BRIGHT_RED}hash: {Colours.RESET}", HOME.hexdigest())
    print(f"{Colours.BRIGHT_GREEN}EXITING..........{Colours.RESET}")
    print(f"{Colours.BRIGHT_GREEN}EXITING..........{Colours.RESET}")
    time.sleep(5)
    main()

def SHA384():
    clear_screens()
    print(f"{Colours.BRIGHT_GREEN}======= \nSHAKE_12 ======{Colours.RESET}")
    sta = input(f"{Colours.BRIGHT_RED}[+]ENTER TEXT YOU WANT TO HASH: {Colours.RESET}")
    op = hashlib.sha3_256()
    op.update(sta.encode())
    print(f"{Colours.BRIGHT_RED}hash: {Colours.RESET}", op.hexdigest())
    print(f"{Colours.BRIGHT_GREEN}EXITING..........{Colours.RESET}")
    time.sleep(5)   
    main()
def HASHING_file():
    clear_screens()
    banner()
    print(f"{Colours.BRIGHT_GREEN} hash_file  OPTION {Colours.RESET}")
    print("""
    
    1. md5
    2. sha384
    3. sha256\n
    """)

    inj = input("enter your choice: ")
    if inj == "1":
        alogrith = hashlib.md5
    elif inj == "2":
        alogrith = hashlib.sha384
    elif inj == "3":
        alogrith = hashlib.sha256
    else:
        print(f"{Colours.BRIGHT_RED} INVAILD INPUT, defaulting for shake_12 algo{Colours.RESET}")
        alogrith = hashlib.shake_12
        
    print("enter the file you want to hash: ")
    os.system("ls")
    file_path = input("~#: ")
    try:
        with open(file_path, 'rb') as f:
            hash_object = alogrith()
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                hash_object.update(chunk)
            print(f"hash value {hash_object.hexdigest()}")
            time.sleep(5)
            main()
    except FileNotFoundError:
        print("the file was not found")
    pass




def main():
    clear_screens()
    banner()
    show_option()
    while True:
        user = input(f"{Colours.BRIGHT_RED}[!]user pick your hash method: {Colours.RESET}")
        if user == "1":
            sha256_hashing()
        elif user == "2":
            md5_hashing()
        elif user == "3":
            BLACK2B()
        elif user == "4":
            SHA3_256()
        elif user == "5":
            SHA512()
        elif user == "6":
            SHAKE_12()
        elif user == "7":
            SHA384()
        elif user == "8":
            HASHING_file()
        elif user == "0":
            print(f"{Colours.BRIGHT_GREEN}EXITING,THANKS FOR USING HASHER V.2 {Colours.RESET}")
            time.sleep(5)
            exit()
             
            break 
        else:
            print(f"{Colours.BRIGHT_RED} INVAILD INPUT {Colours.RESET}")
            exit()

if __name__ =="__main__":
    main()

        