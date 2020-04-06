import sys, time

def main():
    if sys.platform == "linux":
        import linux_monitor as monitor
    else:
        print("OS not supported")
        return 1
        
    while(True):
        mem_used = monitor.getMEM()
        cpu_used = monitor.getCPU()
        up_time = monitor.uptime()

        print(str(cpu_used) + "\t" + str(mem_used) + "\t" + str(up_time))
        time.sleep(5)


if __name__ == "__main__":
    main()
