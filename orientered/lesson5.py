from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amout:float)->bool:
        pass

class CreditCardPayment(PaymentGateway):
    def __init__(self, card_number):
        super().__init__()
        self.__card_number = card_number

    def process_payment(self, amout: float)->bool:
        print(f'|Банк|Запрос к шлюзу Visa/MasterCard...')
        print(f'|Банк|Списание {amout}сом с карты ***{self.__card_number[-4:]}')
        return True

class CryptoPayment(PaymentGateway):
    def __init__(self, wallet_address:str):
        self.wallet_address = wallet_address

    def process_payment(self, amout: float)->bool:
        print(f'|Блокчейны|Проверка сети и смарт-контакта...')
        crypto_amount = amout / 100
        print(f'|Блокчейн|Перевод{crypto_amount}USDT на кошельке {self.wallet_address[:6]}....')


class Customer:
    def __init__(self, name:str, initial_balance: float):
        self.name = name
        self.__balance = initial_balance
        self.__discount = 0.05

    @property
    def balance(self) -> float:
        return self.__balance

    def top_up_balance(self, amount:float):
        if amount <=0:
            raise ValueError('Сумма должна быть положительной')
        self.__balance += amount
        print(f'Баланс пополнен на {amount} сом')
        print(f'Текущий баланс - {self.__balance}')

    def calculate_total(self, amount:float)->float:
        return amount * (1 - self.__discount)


    def calculate_internal_balance(self,amount: float)->bool:
        if self.__balance >= amount:
            self.__balance -= amount
        return False


class OrderManager:
    @staticmethod
    def checkbox(customer: Customer, card_sum: float, payment_method: PaymentGateway):
        print(f'\n---Оформление заказа для пользователя {customer.name}---')

        final_price = customer.calculate_total(card_sum)
        print(f'Исходная сумма: {card_sum} с учетом скидки {final_price} сом')

        payment_success = payment_method.process_payment(final_price)

        if payment_success:
            print('Заказ успешно оплачен')
        else:
            print('Ошибка оплаты')
    

    


