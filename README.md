# kafka-learning

kafka 学习
## docker 版本,外网可访问

### 1.拉取镜像

拉取zookeeper镜像

```
docker pull wurstmeister/zookeeper  

```
拉取kafka镜像
```
docker pull wurstmeister/kafka  

```

### 2. 启动容器
启动zookeeper

```
docker run -d --name zookeeper -p 2181 :2181 -t wurstmeister/zookeeper  
```

启动kafka

```
docker run  -d --name kafka  -p 9092:9092  --link zookeeper  -e KAFKA_BROKER_ID=0  -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://139.226.179.239:9092  -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 -t wurstmeister/kafka 
```

### 3. kafka启动参数说明
   
`–link` 用于容器直接的互通。

`-e KAFKA_BROKER_ID=0` 一个 kafka节点 就是一个 broker。一个集群由多个 broker 组成。一个 broker可以容纳多个 topic

`-e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181` 配置zookeeper管理kafka的路径

`-e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://139.226.179.239:9092` 把kafka的地址端口注册给zookeeper，若远程访问要改成外网IP,千万注意是外网IP，很多文章只说是宿主机IP, 演示例子上写的是内网IP，很容易被误导

`-e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092` 配置kafka的监听端口

`-v /etc/localtime:/etc/localtime` 容器时间同步虚拟机的时间




## kafka-docker-compose

docker-compose 方式启动kafka
[docker-compose-kafka](https://github.com/conduktor/kafka-stack-docker-compose)



### 

 curl -X POST -H "Content-Type: application/json" localhost:9092/events -d '{"event" : "a test event"}'

## kafka-elk-docker-compose

docker-compose 方式启动kafka-elk


https://github.com/sermilrod/kafka-elk-docker-compose.git

## kafka 常规操作

### 查看zookeeper的状态
### 测试kafka

```
#创建topic
kafka-topics.sh --bootstrap-server IP:9092 --create --topic topic1 --partitions 8 --replication-factor 2

#列出所有topic
kafka-topics.sh --bootstrap-server IP:9092 --list

#列出所有topic的信息
kafka-topics.sh --bootstrap-server IP:9092 --describe

#列出指定topic的信息
kafka-topics.sh --bootstrap-server IP:9092 --describe --topic topic1

#生产者（消息发送程序）
kafka-console-producer.sh --broker-list IP:9092 --topic topic1

#消费者（消息接收程序）
kafka-console-consumer.sh --bootstrap-server IP:9092 --topic topic1
```

例如：

```
kafka-topics --create --zookeeper 192.168.42.200:2181,192.168.42.200:2182 --replication-factor 3 --partitions 1 --topic szy

```


### 查看所有topic

```
kafka-topics --list --zookeeper 192.168.42.200:2181,192.168.42.200:2182 

```

### 查看某个topic具体信息

```
 kafka-topics --describe --zookeeper 172.16.218.201:2181,172.16.218.202:2181,172.16.218.203:2181 --topic szy
```

### 删除topic (可直接删除的前提：delete.topic.enable=true)

```
# ./kafka-topics.sh --delete --zookeeper 172.16.218.201:2181,172.16.218.202:2181,172.16.218.203:2181 --topic test 
命令无法删除，topic被标记为删除时候，用下面命令删除
# cd /usr/local/zookeeper-node3/bin/
# ./zkCli.sh
ls /brokers/topics
rmr /brokers/topics/【topic name】
quit
```


### 生产消息

```
# ./kafka-console-producer.sh --broker-list 172.16.218.201:19092,172.16.218.202:19092,172.16.218.203:19092 --topic szy 

```
### 消费消息

```
# ./kafka-console-consumer.sh --zookeeper 172.16.218.201:2181,172.16.218.202:2181,172.16.218.203:2181  --topic szy --from-beginning


```
## kafka 配置远程访问

如果不配置远程访问的话，默认 kafka 只允许localhost进行访问的。

进入kafka的安装目录下的config目录，如下：
打开 `server.properties` 文件，如下：
```
#advertised.listeners=PLAINTEXT://your.host.name:9092
advertised.listeners=PLAINTEXT://主机IP:9092
```

配置好之后，重启服务即可。

