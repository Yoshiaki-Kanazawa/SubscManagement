FROM centos:centos7

RUN yum install zlib-devel libffi-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel libuuid-devel xz-devel
RUN curl -O https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
RUN tar xf Python-3.7.3.tgz
RUN cd Python-3.7.3
RUN ./configure
RUN make
RUN make altinstall
RUN mkdir /var/app

COPY /Users/kanazawayoshiaki/workspace/subscManagement /var/app
