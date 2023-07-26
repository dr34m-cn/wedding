扫码预览：

![小程序码](./gh_60249ca18280_344.jpg)

## 前端

```shell
npm install
npm run serve
```

更多详见uniapp文档

## 后端

### 导入Sql

导入`server/sql/wedding.sql`文件

### 修改配置

项目根目录新建`conf.json`文件，并修改如下

```shell
vim conf.json
```

 **去掉注释，否则报错**

```js
{
    "server": {
        "port": 9014, // 启动端口
        "thread": 10 // 启动线程数
    },
    "mysql": { // mysql相关信息
        "host": "127.0.0.1",
        "port": 3306,
        "db": "wedding",
        "user": "root",
        "passwd": "root"
    },
    "wechat": {
        "appId": "xxxxx",
        "AppSecret": "xxxxx"
    }
}
```

### 安装依赖

```shell
python3 -m pip install --upgrade pip -i https://pypi.doubanio.com/simple/
pip3 install -r requirements.txt -i https://pypi.doubanio.com/simple/
```

### 运行

```shell
python3 main.py
```

### 注册成系统服务（可选）

```shell
vim /etc/systemd/system/wedding.service
```

```shell
[Unit]
Description=weddingServer

[Service]
Type=simple
User=root
Group=root

#设置应用的工作目录与Python3目录，注意修改为自己实际的
WorkingDirectory=/usr/local/app/wedding
ExecStart=/usr/local/svc/python3/bin/python3 /usr/local/app/wedding/main.py
Restart=always
ExecStop=/bin/kill -s TERM $MAINPID

[Install]
WantedBy=multi-user.target
```

#### 重载系统服务

```shell
systemctl daemon-reload
```

#### 启动/停止/查看

```shell
systemctl start wedding
systemctl stop wedding
systemctl status wedding
```

#### 开机自启

```shell
systemctl enable wedding
```