# ネットワーク接続確認・配信ROS2パッケージ

[![test](https://github.com/kankichi07610/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/kankichi07610/mypkg/actions/workflows/test.yml)
![License](https://img.shields.io/badge/License-BSD--3--Clause-green.svg)
![Ubuntu 22.04](https://img.shields.io/badge/Ubuntu-22.04-E95420?style=flat&logo=ubuntu&logoColor=white)
![Python 3.10](https://img.shields.io/badge/Python-3.10-F9DC3E?style=flat&logo=python&logoColor=blue)
![ROS2 Humble](https://img.shields.io/badge/ROS2-Humble-3399FF?style=flat&logo=ros)

本パッケージは、インターネット接続状況(Google Public DNS: 8.8.8.)8を定期的にチェックし、応答速度(Ping値)を監視する ROS 2 パッケージです。

通信遅延が発生した場合や接続が切断された場合に、ログのレベルをユーザーに表示します。

## 実行方法

### 監視ノードの起動
```
$ ros2 launch mypkg talk_listen.launch.py
```

