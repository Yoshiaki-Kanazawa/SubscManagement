FROM mysql:5.7
RUN apt-get clean && apt-get update && apt-get install -y locales locales-all \
    && locale-gen ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:en
ENV LC_ALL ja_JP.UTF-8
RUN ln -sf /usr/share/zoneinfo/Japan /etc/localtime