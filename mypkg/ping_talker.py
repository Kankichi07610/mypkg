#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Kanta Ogasawara
# SPDX-License-Identifier: BSD-3-Clause

import rclpy #クライアントのためのライブラリ
from rclpy.node import Node
from std_msgs.msg import String   #テキストを送るのでString
import subprocess

class pingtalker(Node):
    def __init__(self):
        super().__init__('ping_talker')
        self.pub = self.create_publisher(String, 'test_talker', 10) #テスト用
        self.create_timer(1.0, self.cb)

    def cb(self):
        msg = String()

        google = ['ping', '-c', '1', '-W', '1', '8.8.8.8']
        
        pf = subprocess.run(google, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if pf.returncode == 0:
            msg.data = pf.stdout
        else:
            msg.data = "Time out"

        self.pub.publish(msg)
        #self.get_logger().info(f"Connect test: {msg.data}")

def main():
    rclpy.init()
    node = pingtalker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
