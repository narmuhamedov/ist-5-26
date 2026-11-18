from lesson5 import Customer, CreditCardPayment, CryptoPayment, OrderManager

buyer = Customer(name=str(input('Как вас зовут?')), initial_balance=float(input('сколько у вас денег')))
visa_card = CreditCardPayment('4212334412218778')

OrderManager.checkbox(buyer, card_sum=4000, payment_method=visa_card)

crypto_wallet = CryptoPayment("0x51C..3a9")
OrderManager.checkbox(buyer, card_sum=1500, payment_method=crypto_wallet)