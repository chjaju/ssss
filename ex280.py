import random


class Account:
    # class variable
    account_count = 0
#입금과 출금이 될때마다 기록해주기 위해 self.deposit_log = [] ,self.withdraw_log = [] 라는 비어있는 리스트를 만든다.
    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            #입금내역을 입금이 일어날때마다 리스트로 저장해주기 위해 self.deposit_log.append(amount)를 이용해준다.
            self.deposit_log.append(amount)
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount):
        if self.balance > amount:
            #출금액을 리스트로 저장해주기 위해 self.withdraw_log.append(amount)를 이용해준다.
            self.withdraw_log.append(amount)
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)
#출금내역을 구현하기 위해 for amount in self.withdraw_log:를 이용해준후 프린트 해준다.
    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)
#입금액을 구현하기 위해 for amount in self.deposit_log:룰 이용해준후 프린트 해준다.
    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)



#deposit은 예금이고 k.deposit()을 이용하면 된다. 각각 100, 200, 300원을 예금 한것이고 k.deposit_history()를 이용하면 100, 200, 300이 출력된다.
k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

#withdraw는 출금이고 k.withdraw()를 이용하면 된다. 각각 100, 200원을 출금한 것이고 k.withdraw_history()룰 이용하면 100,200이 출력된다.
k.withdraw(100)
k.withdraw(200)
k.withdraw_history()