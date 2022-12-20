import rclpy
from rclpy.node import Node
from rcl_interfaces.srv import SetParameters
from rcl_interfaces.msg import Parameter, ParameterValue, ParameterType
from rcl_interfaces.srv._set_parameters import SetParameters_Response
from rclpy.parameter_service import SetParameters

TOPIC = "/basic_param/set_parameters"

class MinimalClientAsync(Node):
    def __init__(self):
        super().__init__('minimal_client_async')

        
        self.cli = self.create_client(SetParameters, TOPIC)
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = SetParameters.Request()

    def send_request(self):
        param_value = ParameterValue(string_value="new string")
        param_value.type = ParameterType.PARAMETER_STRING
        param = Parameter(name="my_str", value=param_value)
        params = [param]
        self.req.parameters = params
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClientAsync()
    response: SetParameters_Response
    response = minimal_client.send_request()
    minimal_client.get_logger().info(
        'Result: for {} {}'.format(
            response.results[0].successful,
            response.results[0].reason
            )
        )

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()