import os

# qq mail
MAIL_TO = os.getenv("MAIL_TO", "")
MAIL_HOST = os.getenv("SMTP_HOST", "")
MAIL_PORT = int(os.getenv("SMTP_PORT", 0))
MAIL_USER = os.getenv("MAIL_USER", "")
MAIL_ADDRESS = os.getenv("MAIL_ADDRESS", "")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "")


# free nom
FM_USERNAME = os.getenv("FM_USERNAME", "")
FM_PASSWORD = os.getenv("FM_PASSWORD", "")

