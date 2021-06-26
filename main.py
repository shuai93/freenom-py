from utils.settings import *
from utils.exception import CustomException
from utils.freenom import FreeNom
from utils.mail import EmailPoster


def main():
    print("配置信息")
    print([MAIL_TO, MAIL_PORT, MAIL_HOST, MAIL_ADDRESS, MAIL_PASSWORD, MAIL_USER, FM_USERNAME, FM_PASSWORD])
    if not all([MAIL_TO, MAIL_PORT, MAIL_HOST, MAIL_ADDRESS, MAIL_PASSWORD, MAIL_USER, FM_USERNAME, FM_PASSWORD]):
        raise CustomException("参数缺失")

    to = [MAIL_TO]

    body = {
        'subject': "FreeNom 自动续期",
        'to': to,
    }
    try:
        results = FreeNom().run()
        body['payload'] = {
            "results": results,
            "user": FM_USERNAME
        }
    except CustomException as e:
        body['body'] = e.message

    EmailPoster().send(data=body)


if __name__ == "__main__":
    main()

