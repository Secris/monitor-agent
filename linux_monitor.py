import psutil

def getCPU():
    return psutil.cpu_percent(interval=0.1)
    
def getMEM():
    return psutil.virtual_memory()

def main():
    print("linux monitor")
    

if __name__ == "__main__":
    main()
    
