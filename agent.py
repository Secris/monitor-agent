import sys, time, json
import monitor

def main():
    data = {}

    while(True):
        data["mem_used"] = monitor.getMEM()
        data["cpu_used"] = monitor.getCPU()
        data["up_time"] = monitor.uptime()
        data["hostname"] = monitor.name()

        data_json = json.dumps(data)

        print(data_json)
        time.sleep(1)


if __name__ == "__main__":
    main()
