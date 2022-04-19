# docker_mysql

## 使い方

```
$ docker-compose build
$ docker-compose up
Ctrl + C
$ docker network ls
調べたIPアドレスをconfig.pyのhost部分に記入
$ docker exec -it linebot-python bash
root@[コンテナID]:/project#   flask db init
root@[コンテナID]:/project#   flask db migrate
root@[コンテナID]:/project#   flask db upgrade
```

## 参考
https://qiita.com/AndanteSysDes/items/a25acc1523fa674e7eda
