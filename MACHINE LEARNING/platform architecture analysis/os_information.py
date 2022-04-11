import psutil
import os
import platform
from datetime import datetime

def Cpu_info_os():
    print("---Marvellous infosystem CPU Information os----")
    if platform.system() == 'Windows':
        return platform.processor()
    elif platform.system() == "Darwin":
        command = '/usr/sbin/sysctl-n machdep.cpu.brand_string'
        return os.popen(command).read().strip()
    
    a = 2
    print(a)
def get_size(bytes ,suffix="B"):
    factor =1024

    for unit in ["","K","M","G","P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes/=factor

def platform_info():
    print("---Marvellous infosystem SYstem information----")
    uname = platform.uname()
    print(f"System:{uname.system}")
    print(f"node name:{uname.node}")
    print(f"relese name:{uname.release}")
    print(f"version:{uname.version}")
    print(f"machine:{uname.machine}")
    print(f"processor:{uname.processor}")

def main():
    Cpu_info_os()

if __name__ == "__main__":
    main()