import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5545963604:AAFyeZDxieUOq1mmz6khwuSzTvvf8JiBJcU")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIkBu6C730OcxKkY2zEP47T6RpeYXi9Agw_tb1t19zPrF-BRiQoPQl1wnkzApWKVEZsgBX4HoqxidHPKzcl8f2qlGnZ3IIGXn14C04Be5q-B07nEt5kZiUUEFLihqFULckOdfT63YDiFAAoIg8eiqejNJ9m1XrdWMLKWhrLBKlyp_30qdeSaaqms9HcORz6Q9E-yJlGV5WJ3nGBd1goQQatL0Z23rAWHYE4AlII5Wt5bdeXoBNLfMi3jquHwVkREfFjD2sDNDS3kPRO-t612BhTCCZB62dQj7PBvpsFa1Y3uhphQGyPzfGL_YDSOrBOA_06ejYGtNd8Cv6o1aQj3vQi3eDs=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "miselisarobot")
    SUPPORT = os.environ.get("SUPPORT", "elisha_support") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "denvil_bots") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5569127950")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
