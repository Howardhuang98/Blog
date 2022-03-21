# mysql 安装

直接用包管理器进行安装

可以理解为mariadb = mysql

一般安装mysql 5.7.30 

直接用包管理器进行安装

```shell
apt install mariadb-server

apt install mariadb-client
```

然后进行密码设置

```
mysql_secure_installation
```



## 命令

mysql 是client 用于操作数据库

mysqld 是server，监听3306端口



mysqld的启动用systemctl来进行控制