import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        while self.enemies > 0:
            self.enemies -= self.power
            days += 1
            print(f'\t{self.name} сражается {days} день(дня), осталось {self.enemies} врагов\t')
            time.sleep(1)
        if self.enemies == 0:
            print(f'\t{self.name} одержал победу спустя {days} дней(дня)!\t')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')
