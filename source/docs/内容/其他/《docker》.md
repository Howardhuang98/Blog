# 《docker》

虚拟化技术，docker 容器技术。

## 文档

https://docs.docker.com/get-started/

### 镜像：类

### container：实例

都是用容器来提供服务的，一个镜像可以实例化出多个容器

### 仓库：存放镜像

有国内镜像源

## docker 安装

就按docs用apt安装

结果：

![image-20211017163244626](image-20211017163244626.png)

## 默认资源路径

/var/lib/docker

## run的流程

![image-20211017163713007](image-20211017163713007.png)

我们在client docker 上与 server docker daemon交互。

![image-20211017163808801](image-20211017163808801.png)

docker daemon就是我们的守护进程

守护进程（daemon）是生存期长的一种进程，没有控制终端。它们常常在系统引导装入时启动，仅在系统关闭时才终止

## docker 基本命令

```shell
docker version
docker info # 可以查看server的情况
docker 命令 --help
```

### image

```shell
docker images 查看本地主机上的镜像
docker search mysql 搜索mysql镜像
docker pull mysql:5.7  下载镜像，申明版本一定要supported，分层下载
docker rmi -f 容器id
docker rmi -f $(docker images -aq) 全部删除
```

### container

```shell
docker run [可选参数] image
# 参数
--name = "name"
-d 以后台方式运行
-it 使用交互方式运行
-p 指定容器端口 -p 主机8080:容器8080

docker run -it centos /bin/bash

docker ps 列出所有运行容器
			-a 所有容器

# 在交互模式下，退出容器
ctrl + p +q 退出容器不关闭
exit 退出并关闭

dock rm 容器id

docker start 容器id
docker restart id
docker stop 容器id
docker kill 容器id
```

### 其他命令

```shell
docker run -d 容器
```

容器使用后台运行，就必须要有一个前台进程，docker 发现该容器未提供服务，就会自动停止。

```shell
# 显示日志
docker logs -ft 容器id

# 查看容器中进程
docker top 容器id

# 查看元数据
docker inspect 容器id

# 进入正在运行的容器，进入容器后开启一个新的终端
docker exec -it 容器id /bin/bash

# 进入容器正在执行的终端
docker attach 容器id 

# 从容器内拷贝文件
docker cp 容器id:/地址 /地址
```



## 可视化

portainer 是一个docker 图形化管理界面

没有ssl证书的安装方法

```shell
docker run -d -p 9000:9000 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data  portainer/portainer-ce:latest

```



Rancher

## commit 镜像

```shell
docker commit -m="message" -a="author" 容器id 目标镜像:tag
```

用容器生成镜像

## 容器数据卷

容器的持久化和同步操作，容器间数据也是可以共享的。

```shell
docker run -v 主机目录:容器内目录
```

![image-20211018111914456](image-20211018111914456.png)

查看元文件的结果。

* 容器内部加文件--主机也会添加

* 主机添加--容器内部也添加

双向绑定

## 具名挂载，匿名挂载



```shell
# 匿名挂载 -v 只写容器内路径
docker run -d -P --name nginx01 -v etc/nginx nginx
# 具名
-v 卷名:
-v 

```

只指定容器内的路径的话，数据都被存在了 var/lib/docker/volumes/ 下

```shell
docker volume ls
```

## dockerfile

通过脚本生成image

```shell
docker build -f dockerfile
```

## 数据卷容器

--volumes-from 

实现两个容器数据同步

## dockerfile 命令

```dockerfile
FROM   #基础镜像
MAINTAINER #维护者信息
RUN
ADD
WORKDIR

CMD 只执行最后一个
ENTRYPOINT 追加执行
ENV #环境变量
```

![image-20211018114922567](image-20211018114922567.png)

```shell
docker bulit -f /file -t name:tag .
```

## docker网络

![image-20211018121930689](image-20211018121930689.png)

三个网络

### linux可以ping容器内部

每次启动一个容器，主机就会多一个docker0 网卡

主机中的docker0网卡 对应容器中的网卡

evth-pair 是一对虚拟设备接口，成对出现。相当于一个桥梁

比如：

![image-20211018122639634](image-20211018122639634.png)

### 容器之间可以相互ping通

![image-20211018122919196](image-20211018122919196.png)

![image-20211018123109219](image-20211018123109219.png)

docker0 是容器的网桥

### --link

 --link 容器 

本质上就是在host中将ip与容器名绑定

## 《docker-compose》

高效管理多个容器

1. 定义dockerfile

2. 定义服务，组织app docker-compose.yml
3. docker-compose up

## yaml 规则

```yaml
version:
service:
	nginx:
	
	redis:
	
volumes:
neworks:
configs:


```



