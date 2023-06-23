#ProjectFor AmirHossein Dindar
import threading
import time
import random


class Philosopher(threading.Thread):
    def __init__(self, number, left_chopstick, right_chopstick):
        threading.Thread.__init__(self)
        self.number = number
        self.left_chopstick = left_chopstick
        self.right_chopstick = right_chopstick

    def run(self):
        while True:
            # قبل از برداشتن اولين چاپستيک مفداري زمان تصادفي صبر مي کنيم
            time.sleep(random.uniform(0, 1))

            # روي هر دو چاپستيک قفل ميگيريم 
            if self.left_chopstick.acquire(timeout=1):
                if self.right_chopstick.acquire(timeout=1):
                    # براي مدت زمان تصادفي غذا مي خوريم
                    print(f"Philosopher {self.number} is eating.")
                    time.sleep(random.uniform(0, 1))

                    self.right_chopstick.release()
                else:
                    # اگر چاپستیک سمت راست در دسترس نیست، قفل چاپستیک چپ را آزاد می کنیم
                    self.left_chopstick.release()
            else:
                # اگر چاپستیک چپ در دسترس نیست، بعداً دوباره امتحان می کنیم
                print(f"Philosopher {self.number} is hungry.")


if __name__ == "__main__":
    # 5 فیلسوف و 5 چاپستیک می سازیم 
    philosophers = [Philosopher(i, threading.Lock(), threading.Lock()) for i in range(5)]

    # همه فیلسوفان را شروع می کنیم
    for philosopher in philosophers:
        philosopher.start()

    # منتظر تمام فیلسوفان می شویم
    for philosopher in philosophers:
        philosopher.join()
