import psutil, platform
from datetime import timedelta
from uptime import uptime

def getCPU():
    return psutil.cpu_percent(interval=0.1)
    
def getMEM():
    virt_mem = psutil.virtual_memory().used
    virt_mem = virt_mem / 1024 # Converts to KiB
    virt_mem = virt_mem / 1024 # Converts to MiB
    
    return round(virt_mem, 2)

def system_uptime():
    return uptime()
    
def name():
    return platform.node()

def main():
    mem = getMEM()
    cpu = getCPU()
    up = uptime()

    print("CPU - {}%\tMEM - {}MiB\tUP - {}".format(cpu, mem, up))
    

if __name__ == "__main__":
    main()
    
