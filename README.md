# freenom-py

## 项目描述

模仿 [Freenom-PHP](https://github.com/shuai93/freenom) 实现python的版本


## 项目部署

目前仅实现了 Github Action 的部署方式，因为我觉得这种方式最适合这个项目。

### 1. Fork 项目 🔗



### 2. Github Action Secrets 配置  🕹

| 变量 | 描述 |  示例 |
| --- | --- |  --- | 
| MAIL_USER | 发件人邮箱用户名 |  xxx.qq.com | 
| MAIL_ADDRESS | 发件人邮箱地址 | xxx.qq.com |
| MAIL_HOST | 发件人邮箱服务器 | smt.qq.com |
| MAIL_PASSWORD | 发件人邮箱密码 | xxxxxx |
| MAIL_PORT | 邮箱服务器端口 |  465 |
| MAIL_TO | 收信邮箱 | xxx.qq.com |
| FM_USERNAME | Freenom 用户名 | xxx.qq.com |
| FM_PASSWORD | Freenom 密码 | xxxxxx |

### 3. 运行  Github Action ▶️


### 4 查看收件箱 📮

不出意外会收到一封自动续费的邮件