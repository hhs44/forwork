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

+ 获取ubuntu.tar 作为基础镜像

