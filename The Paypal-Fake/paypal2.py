import time

def make_load_bar(func):
    """
    make it look like the program of your choice is processing something\n
    :param :
    :return:
    """
    def wrapper(*args):
        progress = 0
        waiting_line = 10

        for i in range(waiting_line):
            progress += 1
            waiting_line -= 1
            print(
                "[" +
                "|" * progress +
                "." * waiting_line +
                "]")
            time.sleep(1.5)

        func("d.grollmusz@********")

    return wrapper


def authenticator():
    setattr(authenticator, "__user_name__", "d.grollmusz@********")
    return authenticator


@make_load_bar
def authenticate(user):
    print(f"Logged in user: {user}")
