# -----------------------------------------------------------------
# T O  G I V E  F A B I A N  H I S  R N D  M O N E Y
# -----------------------------------------------------------------
import random
import time

from paypal2 import *


def randomise_amount(start, stop):
    """
    Returns the amount of money I need to send Fabian\n
    :param start: int
    :param stop: int
    :return: int
    """
    rnd_amount = random.randint(start, stop)
    return rnd_amount


def login_paypal():
    time.sleep(1)
    print("Logging in to Paypal:")
    time.sleep(1)

def auth_paypal():
    # login to paypal account
    oauth = authenticator()
    user = oauth.__user_name__
    authenticate(user)

def ask_for_amount():
    """
    Prompts the user to specify the upper and lower bound
    """
    time.sleep(3)
    start, stop = input("Range of your financial aid?\n").split(",")
    return int(start), int(stop)


def ask_for_person():
    name = input("Receiver?\n")
    return name

@make_load_bar
def send_money(*args):
    print("\n")
    print(f"{args[0]}€ send successfully!\nDont send more, for the sake of your bank account.")

def main():
    login_paypal()
    auth_paypal()

    p_from, p_to = ask_for_amount()
    amount = randomise_amount(p_from, p_to)

    # who is the receiver?
    receiver = ask_for_person()

    # send the money
    send_money(amount)

if __name__ == "__main__":
    main()