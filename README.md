# freenom-py

## 项目描述 🔑

一个 Freenom 自动续期域名的脚本


## 项目部署 🥳

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

关于如何配置以及启动 可以查看我的掘金文章 [ Github Action 的简单使用 ](https://juejin.cn/post/6969119163293892639)

### 4. 查看收件箱 📮

不出意外会收到一封关于域名续期的邮件


## 写在最后 🔚

关于如何 申请域名以及小伙伴如何绕开限制可以查看 [ 程序员，申请个域名 ](https://juejin.cn/post/6979411782674677790)

核心代码见 ` utils/freenom.py`

此项目核心接口参考 [Freenom-PHP](https://github.com/shuai93/freenom) 。
