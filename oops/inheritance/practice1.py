class PaymentMethod:
    def __init__(self, amount):
        # TODO: Initialize base attribute 'amount'
        pass

    def print_receipt(self):
        # TODO: Print receipt message showing total bill amount
        pass

class CashPayment(PaymentMethod):
    def __init__(self, amount, cash_given):
        # TODO: Pass 'amount' to parent class using super().__init__()
        # TODO: Initialize child attribute 'cash_given'
        pass

    def calculate_change(self):
        # TODO: Calculate and print change to return
        pass

class CardPayment(PaymentMethod):

    def __init__(self, amount, card_number_last4):
        # TODO: Pass 'amount' to parent class using super().__init__()
        # TODO: Initialize child attribute 'card_number_last4'
        pass

    def swipe_card(self):
        # TODO: Print card processing message
        pass

cash_order = CashPayment(amount=450, cash_tendered=500)
cash_order.print_receipt()
cash_order.calculate_change()

