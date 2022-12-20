import rclpy
from rclpy.node import Node


class BasicParams(Node):
    def __init__(self):
        super().__init__('basic_param')
        self.get_logger().info("start basic param")
        self.declare_parameter('my_str', value="string")
        self.declare_parameter('my_int', value=10)
        
        self.my_str = self.get_parameter("my_str").value
        self.my_int = self.get_parameter("my_int").value

        


def main(args=None):
    rclpy.init(args=args)
    node = BasicParams()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()