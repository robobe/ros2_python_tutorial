import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterEvent
from rclpy.parameter import Parameter
from rclpy import qos

TOPIC = "/parameter_events"

class MyNode(Node):
    def __init__(self):
        node_name="param_monitor"
        super().__init__(node_name)
        self.__sub = self.create_subscription(ParameterEvent, 
            TOPIC,
            self.__param_event_handler, 
            qos_profile=qos.qos_profile_parameter_events)
        self.get_logger().info("start param monitor")

    def __param_event_handler(self, msg: ParameterEvent):
        param: Parameter
        self.get_logger().info("Change params for node: {}".format(msg.node))
        for param in msg.changed_parameters:
            self.get_logger().info(param.name)
            self.get_logger().info(str(param.value))

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()