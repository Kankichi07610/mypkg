# ネットワーク接続確認・配信ROS2パッケージ

[![test](https://github.com/kankichi07610/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/kankichi07610/mypkg/actions/workflows/test.yml)
![License](https://img.shields.io/badge/License-BSD--3--Clause-green.svg)
![Ubuntu 22.04](https://img.shields.io/badge/Ubuntu-22.04-E95420?style=flat&logo=ubuntu&logoColor=white)
![Python 3.10](https://img.shields.io/badge/Python-3.10-F9DC3E?style=flat&logo=python&logoColor=blue)
![ROS2 Humble](https://img.shields.io/badge/ROS2-Humble-3399FF?style=flat&logo=ros)

本パッケージは、インターネット接続状況(Google Public DNS: 8.8.8.)8を一秒間隔でチェックし、応答速度(Ping値)を監視する ROS 2 パッケージです。

通信遅延が発生した場合や接続が切断された場合に、ログのレベルをユーザーに表示します。

## 実行方法

### 以下のコマンドで実行します。
```
$ ros2 launch mypkg talk_listen.launch.py
```

### 実行結果の例

本パッケージは、ネットワークの状態に応じて以下のように出力します。

**正常時**  
応答速度が50ms以下の場合,INFOログで応答時間を表示します。  
`[ping_listener-2] [INFO] [1767191976.971079533] [ping_listener]: Connection Ok | Time: 11.2 ms`


**遅延発生時**  
応答速度が50ms以上の場合、WARNログで応答時間を表示します。  
`[ping_listener-2] [WARN] [1767191982.948914955] [ping_listener]: Connection Bad | slow: 52.7 ms`


**切断時**  
インターネット接続が切断された場合、ERRORログで表示します。  
`[ping_listener-2] [ERROR] [1767191990.922695832] [ping_listener]: Network error | Time out`


## ノードの役割  
### ping_talker  
- **役割**:外部サーバー(8.8.8.8)に対して、ネットワークの通信確認を行い、pingを取得します。  
- **パブリッシュするトピック**: `test_talker`


### ping_listener
- **役割**: Ping の実行結果を受信し、応答時間を処理しログ出力を行います。
- **サブスクライブするトピック**: `test_talker`


## トピックの説明

| トピック名 | 型 | 内容 |
|:---|:---|:---|
| `test_talker` | `std_msgs/String` | Pingコマンドの出力|
