import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
from rcl_interfaces.msg import ParameterDescriptor, IntegerRange, ParameterType

from rclpy.parameter import Parameter
from typing import List

class BasicParams(Node):
    def __init__(self):
        super().__init__('basic_param')
        self.get_logger().info("start basic param")
        
        my_int_range = IntegerRange(from_value=0, to_value=100, step=1)
        my_int_descriptor = ParameterDescriptor(
            description="my int parameter with type and limit",
            type=ParameterType.PARAMETER_INTEGER
        )
        my_int_descriptor.integer_range.append(my_int_range)

        my_bool_descriptor = ParameterDescriptor(
            description="my bool",
            type=ParameterType.PARAMETER_BOOL,
            read_only=True
        )
        
        self.declare_parameter('my_str', value="string")
        self.declare_parameter('my_int', value=10, descriptor=my_int_descriptor)
        self.declare_parameter('my_bool', value=False, descriptor=my_bool_descriptor)

        self.add_on_set_parameters_callback(self.__parameters_handler)

        self.my_str = self.get_parameter("my_str").value
        self.my_int = self.get_parameter("my_int").value
        self.my_bool = self.get_parameter("my_bool").value

        self.get_logger().info("my_str param value: {my_str}".format(my_str=self.my_str))

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