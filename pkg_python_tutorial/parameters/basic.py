import rclpy
from rclpy.node import Node

class BasicParams(Node):
    def __init__(self):
        super().__init__('basic_param')

        self.declare_parameter('my_str', value="string")
        self.declare_parameter('my_int', value=10)


def main(args=None):
    rclpy.init(args=args)
    node = BasicParams()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()