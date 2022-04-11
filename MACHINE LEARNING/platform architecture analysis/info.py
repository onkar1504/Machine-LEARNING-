import platform
from time import sleep
import psutil
from os_information import get_size

# machine = platform.machine()
# print(machine)
# uname = platform.uname()
# print(uname)


print("-----------check Ram information---------------")
svmem = psutil.virtual_memory()
print(f"Total:{get_size(svmem.total)}")
print(f"Availabel:{get_size(svmem.available)}")
print("usages:",get_size(svmem.used))
print("PErcent:",get_size(svmem.percent,"%"))

print("--SWAP---")

swap = psutil.swap_memory()
print(f"Total:{get_size(swap.total)}")
print(f"Free:{get_size(swap.free)}")
print(f"used:{get_size(swap.used)}")
print(f"PErcent:{get_size(swap.percent)}")

print("-----------check Cpu information---------------")

print("physical Cores:",psutil.cpu_count(logical=False))
print("Total Cores:",psutil.cpu_count(logical=True))

print("cpu usage per Cores:")
for i,percentage in enumerate(psutil.cpu_percent(percpu=True)):
    print(f"Core{i}:{percentage}%")
print(f"total cpu usage:{psutil.cpu_percent()}%")


