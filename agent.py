import sys, time

def main():
    if sys.platform == "linux":
        import linux_monitor as monitor
    else:
        print("OS not supported")
        return 1
        
    while(True):
        print(monitor.getCPU())
        time.sleep(5)


if __name__ == "__main__":
    main()
