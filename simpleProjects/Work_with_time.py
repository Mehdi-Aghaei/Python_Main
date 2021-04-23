from datetime import datetime
from time import time, sleep
import os
class Battery:
    def __init__(self,battery):
        self.battery = battery
        
    def check_date():
        x = datetime.now()
        
        with open("/tmp/battery_check.txt", mode='a') as file:
            file.write(f"\n record is {x}")
            return file
    def run_long():
        if os.path.exists("/tmp/battery_check.txt"):
            os.remove("/tmp/battery_check.txt")
        else:
            while True:
                sleep(60 - time() % 60)
            # thing to run
                x = datetime.now()
                file = open("/tmp/battery_check.txt",mode='a')
                file.write(f"\n record is {x}")
                file.close()
                break

