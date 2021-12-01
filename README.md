# forwork

# 1、部署场景
+ centos8.x
+ python 3.6.8
  + fastapi==0.70.0
    + starlette==0.16.0 
    + idna==3.3
    + anyio==3.4.0

  + uvicorn
+ nginx 
  + 前端静态页面

## 一、准备过程中的问题
- python3的安装：
```
# 本地挂载ios源进行安装
yum install python3
# 建立软连接
ln python3 /usr/bin/python
```
  + 第三方库的准备 

```
# 下载fastapi 和  uvicorn 到本地
进入目录后
python setup.py install


docker 方案：

+ 获取ubuntu.tar 作为基础镜像 已上传
+ 修改docker 并保存为images
$ docker commit -m "update index.html" --author='leeyunt' 13af96130e40 leeyunt/nginx:v1


参数-m是对创建的该镜像的一个简单描述。

--author表示该镜像的作者。

13af96130e40表示创建镜像所依据的容器的id。

leeyunt/nginx则表示仓库名，leeyunt是名称空间，nginx是镜像名。

v1表示仓库的tag。

创建完成后，通过docker images命令就可以查看到刚刚创建的镜像。

通过刚刚创建的镜像运行一个容器，访问该容器，发现nginx默认的首页已经发生改变。
