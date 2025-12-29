import rclpy #クライアントのためのライブラリ
from rclpy.node import Node
from std_msgs.msg import String   #テキストを送るのでString

class pingtalker(Node):
    def __init__(self):
        super().__init__('ping_talker')
        self.pub = self.create_publisher(String, 'test_talker', 10) #テスト用
        self.create_timer(1.0, self.cb)

    def cb(self):
        msg = String()
        msg.data = "test"
        self.pub.publish(msg)
        self.get_logger().info('test')

def main():
    rclpy.init()
    node = pingtalker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
