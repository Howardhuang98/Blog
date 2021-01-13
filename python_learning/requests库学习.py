from http import cookiejar
import requests
my_logindata = "username=%E9%BB%84%E6%B5%A9&password=huanghao123&logout=7days&returnto=torrents.php"
r = requests.post(url=r"https://www.tjupt.org/takelogin.php",data=my_logindata)
mycookies = r.cookies
headers = {'user-agent': r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
'cookies':mycookies}
r = requests.get(url=r"https://www.tjupt.org/index.php",headers=headers)
print(r.text)