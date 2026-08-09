import socket
import argparse
from colorama import Fore, Style,init
init(autoreset=True)
parser = argparse.ArgumentParser(description="port scanner")
parser.add_argument("--target",
                    metavar="IP",
                    dest="target_host",
                    help="target host"
                    )
args = parser.parse_args()
if args.target_host:
    https = args.target_host
else:
    https = input("entry url:")
    print("need few second,type ctrl+c to exit")
try:
    target_host =socket.gethostbyname(https)
    print(Style.BRIGHT + Fore.GREEN + f"url = {https}")
    for s in range(1,200):
        netport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        netport.settimeout(0.2)
        result = netport.connect_ex((target_host, s))
        if result == 0:
            print(Style.BRIGHT + Fore.GREEN+f"port{s} are open")
        netport.close()
except KeyboardInterrupt:
    print("process has been terminated by user")
except socket.gaierror as e:
    error_code,error_message = e.args
    print(f"connect fail:{error_code}")
    print(f"error message:{error_message}")
except Exception as e:
    print(f"other error:{e}")