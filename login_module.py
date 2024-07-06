import instaloader
from instaloader.exceptions import TwoFactorAuthRequiredException


def login(username, password):
    L = instaloader.Instaloader()
    try:
        L.login(username, password)  # (login)
    except TwoFactorAuthRequiredException:
        num = int(input("Enter 2FA code: "))
        L.two_factor_login(num)

    except Exception as e:
        print(f"An error occurred during login: {e}")
        return None
