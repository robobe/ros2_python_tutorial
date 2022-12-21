"""
ros2 run pkg_python_tutorial param_basic --ros-args -p my_str:="new string data"
"""
import rclpy
from rclpy.node import Node

class BasicParams(Node):
    def __init__(self):
        super().__init__('basic_param')
        self.get_logger().info("start basic param")
        self.declare_parameter('my_str', value="string data")
        self.declare_parameter('my_int', value=10)
        
        self.my_str = self.get_parameter("my_str").value
        self.my_int = self.get_parameter("my_int").value

        self.get_logger().info(f"my_str: {self.my_str}")


def main(args=None):
    rclpy.init(args=args)
    node = BasicParams()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()