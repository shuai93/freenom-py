import os

# qq mail
MAIL_HOST = os.getenv("SMTP_HOST", 'smtp.qq.com')
MAIL_PORT = int(os.getenv("SMTP_PORT", 465))
MAIL_USER = os.getenv("MAIL_USER", "785363268@qq.com")
MAIL_ADDRESS = os.getenv("MAIL_ADDRESS", "785363268@qq.com")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "")
