import psutil, platform
from datetime import timedelta

def getCPU():
    return psutil.cpu_percent(interval=0.1)
    
def getMEM():
    virt_mem = psutil.virtual_memory().used
    virt_mem = virt_mem / 1024 # Converts to KiB
    virt_mem = virt_mem / 1024 # Converts to MiB
    
    return round(virt_mem, 2)

def uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    return uptime_seconds
    
def name():
    return platform.node()

def main():
    mem = getMEM()
    cpu = getCPU()
    up = uptime()

    print("CPU - {}%\tMEM - {}MiB\tUP - {}".format(cpu, mem, up))
    

if __name__ == "__main__":
    main()
    
