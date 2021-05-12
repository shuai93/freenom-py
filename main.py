from utils.mail import EmailPoster

if __name__ == "__main__":
    body = {
        'subject': "测试",
        'to': ["youngs@yeah.net"],
        'body': "测试邮件"
    }
    EmailPoster().send(data=body)
