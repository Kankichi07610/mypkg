import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class pinglistener(Node):
    def __init__(self):
        super().__init__('ping_listener')
        self.create_subscription(String, 'test_talker', self.cb, 10)

    def cb(self, msg):
        self.get_logger().info(f" {msg.data}")

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
