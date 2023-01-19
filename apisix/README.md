# APISIX

apisix部署相关脚本，利用 `apisix ingress controller`做为K8S集群的流量入口。

## 目录结构

- apisix-etcd：etcd部署脚本
- apisix：apisix部署脚本
- apisix-dashboard：控制面板部署脚本
- apisix-ingress-controller：ingress部署脚本

## etcd 部署

利用Helm安装etcd集群，helm配置在etcd文件下的values.yaml文件中。

```shell
# 安装etcd集群
helm install vod-etcd -f values.yaml bitnami/etcd
```

## apisix 部署

## apisix 控制台部署

## apisix 流量入口部署
