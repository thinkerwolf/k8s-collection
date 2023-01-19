# AES-EKS

亚马逊EKS基础设施构建脚本，包括持久化、日志收集等。

## 目录结构

- cloudwatch：fluentd日志收集到AWS Cloudwatch
- ebs：AWS EBS实现持久化
- efs：AES EFS实现持久化
- metrics：容器指标收集服务（用于POD动态扩容和指标检测）


## EFS

[使用 Amazon EKS 中的持久性存储](https://aws.amazon.com/cn/premiumsupport/knowledge-center/eks-persistent-storage/)
