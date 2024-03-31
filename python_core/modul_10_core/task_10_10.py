from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        price = sum(value for value in self.data if value > 0)
        return price
    
payment = AmountPaymentList([1, -3, 4])
total_amount = payment.amount_payment()
print(f"Total amount to be paid: {total_amount}")