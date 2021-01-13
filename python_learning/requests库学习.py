from http import cookiejar
import requests
headers = {'user-agent': r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

# 访问登陆页面
r0 = requests.get(url=r"https://www.tjupt.org/login.php",headers=headers)
print("登陆页面访问",r0.status_code)

# 登录账号
r1 = requests.post(url=r"https://www.tjupt.org/takelogin.php",data="username=%E9%BB%84%E6%B5%A9&password=huanghao123&logout=7days")
a = r1.cookies.get_dict()
print(r1.status_code)
print(r1.text)