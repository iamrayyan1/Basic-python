# 3. Write a program in which a class named Account has private member variables named
# account_no ,account_bal ,security_code. Use a public function to initialize the variables and
# print all data. [2 marks]


class Account:
        def __init__(self,acc_no,acc_bal,sec_code):
                self.__acc_no = acc_no
                self.__acc_bal = acc_bal
                self.__sec_code = sec_code

        def print(self):
                print(f"account number: {self.__acc_no}\nbalance: {self.__acc_bal}\nsecurity code: {self.__sec_code}")

acc= Account(12345, 100000,3110)
acc.print()
