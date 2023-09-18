# 使用官方 Python 轻量级镜像
# https://hub.docker.com/_/python
FROM python:3.8-alpine

#RUN apk add tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo Asia/Shanghai > /etc/timezone

#这里主要是添加一下作者信息
MAINTAINER 1152508446@qq.com

# 将本地代码拷贝到容器内
ENV APP_HOME /app
WORKDIR /app
ADD . /app

# 安装依赖
#RUN pip install --upgrade pip setuptools==57.5.0
#RUN pip install pip==23.2.1
RUN pip install --user -r requirements.txt


#RUN pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple \
#&& pip config set global.trusted-host mirrors.cloud.tencent.com \
#&& pip install --upgrade pip \
## pip install scipy 等数学包失败，可使用 apk add py3-scipy 进行， 参考安装 https://pkgs.alpinelinux.org/packages?name=py3-scipy&branch=v3.13
#&& pip install --trusted-host pypi.python.org -r requirements.txt


EXPOSE 80 8000

RUN chmod +x /app/start.sh
# 启动 Web 服务
# 这里我们使用了 gunicorn 作为 Server，1 个 worker 和 8 个线程
# 如果您的容器实例拥有多个 CPU 核心，我们推荐您把线程数设置为与 CPU 核心数一致
CMD ["bash", "start.sh"]