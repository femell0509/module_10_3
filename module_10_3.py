import threading
import time
import random

class Bank:
    Operation_Lock = threading.Lock()

    def __init__(self, balans: int):
        self.balans = balans

    def deposit(self):
        for i in range(10):
            ran = random.randint(50, 500)
            self.balans += ran
            print(f'Пополнение:{ran}. Баланс:{self.balans}')
            if self.balans >= 500 and Bank.Operation_Lock.locked():
                Bank.Operation_Lock.release()
            time.sleep(0.1)
    def take(self):
        for i in range(10):
            ran = random.randint(50, 500)
            print(f'Запрос на {ran}')
            if ran <= self.balans:
                self.balans -= ran
                print(f'Снятие:{ran}. Баланс:{self.balans}.')
            else:
                print('Запрос отклонен, недостаточно средств.')
                Bank.Operation_Lock.acquire()
            time.sleep(0.1)
            
sber_bank = Bank(34)

th1 = threading.Thread(target=Bank.deposit, args=(sber_bank,))
th2 = threading.Thread(target=Bank.take, args=(sber_bank,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {sber_bank.balans}')