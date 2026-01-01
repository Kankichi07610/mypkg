#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Kanta Ogasawara
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class pinglistener(Node):
    def __init__(self):
        super().__init__('ping_listener')
        self.create_subscription(String, 'test_talker', self.cb, 10)

    def cb(self, msg):
        error = msg.data

        if 'time=' in error:
            # 前半の文章を切る
            first = error.split('time=')[1]

            # 後半の文章を切る
            finish = first.split(' ms')[0]

            if float(finish) > 50.0:
            
                self.get_logger().warn(f"Connection Bad | slow: {finish} ms")
            else:
            
                self.get_logger().info(f"Connection Ok | Time: {finish} ms")

        else:
            
            self.get_logger().error(f"Network error | {error}")

def main():
    rclpy.init()
    node = pinglistener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
