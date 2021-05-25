# -----------------------------------------------------------------
# T O  G I V E  F A B I A N  H I S  R N D  M O N E Y
# -----------------------------------------------------------------
import random
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


def log_in_paypal():
    # login to paypal account
    oauth = authenticator()
    user = oauth.__user_name__
    authenticate(user)

log_in_paypal()

