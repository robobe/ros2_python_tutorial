import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
from rcl_interfaces.msg import ParameterDescriptor, IntegerRange, ParameterType
from rclpy.parameter import Parameter
from typing import List

class BasicParams(Node):
    def __init__(self):
        super().__init__('basic_param')
        self.get_logger().info("param array")
        my_int_descriptor = ParameterDescriptor(
            description="my int array param",
            type=ParameterType.PARAMETER_INTEGER_ARRAY
        )
        self.declare_parameter('my_array', value=[10, 20], descriptor=my_int_descriptor)
        
        self.my_array = self.get_parameter("my_array").value
        for item in self.my_array:
            self.get_logger().info(str(item))

        self.add_on_set_parameters_callback(self.__parameters_handler)

    def __parameters_handler(self, params: List[Parameter]):
        success = True
        for param in params:
            self.get_logger().info(param.name)
            self.get_logger().info(str(param.value))
        return SetParametersResult(successful=success)

def main(args=None):
    rclpy.init(args=args)
    node = BasicParams()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()