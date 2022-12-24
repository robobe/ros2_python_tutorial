"""
ros2 run rqt_runtime_monitor rqt_runtime_monitor 
"""
import rclpy
from rclpy.node import Node
from diagnostic_msgs.msg import DiagnosticStatus, DiagnosticArray
from rclpy.qos import qos_profile_system_default

class SimpleNode(Node):
    def __init__(self):
        super().__init__('basic_diag')
        self.get_logger().info("simple diagnostic")
        self.pub = self.create_publisher(DiagnosticArray, "/diagnostics", qos_profile=qos_profile_system_default)
        self.create_timer(1, self.timer_handler)

    def timer_handler(self):
        msg = DiagnosticArray()
        msg.status = [
            DiagnosticStatus(name="diag1", message="simple diag"),
            DiagnosticStatus(name="diag2", message="error diag", le)
        ]
        self.get_logger().info("send dia")
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()