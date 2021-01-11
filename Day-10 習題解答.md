# Day-9 習題解答

在 docker 安裝 mongodb

$sudo docker pull mongo:latest

$sudo docker image

使用以下命令來運行 mongo 容器：
$docker run -itd --CupoyTest mongo -p 27017:27017 mongo --auth

參數說明：
(1)-p 27017:27017 ：映射容器服務的 27017 埠到宿主機的 27017 埠。外部可以直接通過主機 ip:27017 訪問到 mongo 的服務。
(2)--auth：需要密碼才能訪問容器服務。
#確認執行的Docker 程式

$docker ps


db.createUser( {
    user: "root",
    pwd: "<password>",
    roles: [
        { role: "userAdminAnyDatabase", db: "admin" },
        { role: "hostManager", db: "admin" },
        { role: "__system", db: "admin" }
    ]
});
