import requests
import time

class Led:
    WHITE = 1
    BLUE = 2
    GREEN = 3
    RED = 5

def flip(led):
    requests.get("http://localhost:5120/flip/%s" % led)

def alarm(led):
    requests.get("http://localhost:5120/alarm/%s" % led)

def timer(m, led):
    for _ in range(int(m * 60)):
        flip(led)
        time.sleep(1)

def alarm_and_wait(led=1):
    print("Ding ding ding!")
    while True:
        try:
            alarm(led)
        except KeyboardInterrupt:
            input("Press [enter] to continue, CTRL-C to exit...")
            break


if __name__ == "__main__":
    FOCUS_MIN = 20
    BREAK_MIN = 5
    while True:
        print("Start your focus period...")
        timer(FOCUS_MIN, Led.BLUE)
        alarm_and_wait(Led.WHITE)
        print("Take a break...")
        timer(BREAK_MIN, Led.RED)
        alarm_and_wait(Led.GREEN)
