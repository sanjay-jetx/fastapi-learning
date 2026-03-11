import instaloader
from instaloader.exceptions import TwoFactorAuthRequiredException

loader = instaloader.Instaloader()

username = "ft.sanjyy"
password = "&Anjay2512___?<>"

try:
    loader.login(username, password)

except TwoFactorAuthRequiredException:
    code = input("Enter 2FA code: ")
    loader.two_factor_login(code)

loader.download_profile("cristiano", profile_pic_only=True)