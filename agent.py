import sys, time

def main():
    if sys.platform == "linux":
        import linux_monitor
    else:
        print("OS not supported")
        
    while(True):
        getCPU()
        time.sleep(5)


if __name__ == "__main__":
    main()
