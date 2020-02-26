from time import sleep


class A:

    def __init__(self, num1):
        self.num1 = num1

    def run(self):
        while True:
            print(f"num {self.num1}")
            sleep(3)
