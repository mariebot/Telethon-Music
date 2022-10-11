import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5545963604:AAFyeZDxieUOq1mmz6khwuSzTvvf8JiBJcU")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIkBuw7FSpkcGqW7gL7CmA02Zls38Az-XIHggV_l1z1iOm-dror57c_Dp_YnnS_liJ-8MaYkt3MFLnTWFFZweFLnRH5MGa70T29UX-hw9TQXTPiES--fn06xUaNMTtE9APBn7zwllfDhVJSTsS_wPMAUpKjpgIrMymA_Hzv0Yn6haXBrLABzJVNiAmRfRwsfNTTWxGz0uxrvbAuiuqxcqyb9WRGq6WGrGB1ePxjHLEA3UcrpCRM4_kxb2BrkuGGGacu8AVGjlLV87SU3VMp8KP97Y_cnk-YQmkQdjwIQaBeaVAtc7oFi6TavwDR66DbGaO5AKV9M2hHUVs7zUnMLaC2MyEw=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", "ENABLE")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "miselisarobot")
    SUPPORT = os.environ.get("SUPPORT", "elisha_support") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "denvil_bots") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5569127950")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
