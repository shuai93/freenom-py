import smtplib
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from . import settings


class EmailPoster(object):
    """
    邮件发送基础类
    """

    def send(self, data: dict):
        content = data.get('body', '')
        subject = data.get('subject', '')
        mail_to = data.get('to', [])
        mail_from = data.get('from', settings.MAIL_ADDRESS)
        self._send(content, subject, mail_from, mail_to)

    @staticmethod
    def _send(content: str, subject: str, mail_from: str, mail_to: list):
        msg_root = MIMEMultipart('related')
        msg_text = MIMEText(content, 'html', 'utf-8')
        msg_root.attach(msg_text)
        msg_root['Subject'] = subject
        msg_root['From'] = mail_from
        msg_root['To'] = ";".join(mail_to)

        print("settings.MAIL_PASSWORD = ", settings.MAIL_PASSWORD)
        try:
            smtp = smtplib.SMTP_SSL(settings.MAIL_HOST, settings.MAIL_PORT)
            # smtp.set_debuglevel(1)
            smtp.ehlo()
            smtp.login(settings.MAIL_USER, settings.MAIL_PASSWORD)
            smtp.sendmail(settings.MAIL_ADDRESS, mail_to, msg_root.as_string())
            smtp.quit()
        except Exception as e:
            print(traceback.format_exc(e))
