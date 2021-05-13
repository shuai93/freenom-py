import os

# qq mail
MAIL_ADDRESS = os.getenv("MAIL_ADDRESS", "")
MAIL_HOST = os.getenv("SMTP_HOST", "")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "")
MAIL_PORT = int(os.getenv("SMTP_PORT", 0))
MAIL_TO = os.getenv("MAIL_TO", "")
MAIL_USER = os.getenv("MAIL_USER", "")


# free nom
FM_USERNAME = os.getenv("FM_USERNAME", "")
FM_PASSWORD = os.getenv("FM_PASSWORD", "")

