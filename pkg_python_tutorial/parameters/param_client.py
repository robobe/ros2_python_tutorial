import rclpy
from rclpy.node import Node
from rcl_interfaces.srv import GetParameters
from rcl_interfaces.srv._get_parameters import GetParameters_Request, GetParameters_Response

TOPIC = "/basic_param/get_parameters"

class MinimalClientAsync(Node):
    def __init__(self):
        super().__init__('minimal_client_async', allow_undeclared_parameters=True, automatically_declare_parameters_from_overrides=True)

        self.cli = self.create_client(GetParameters, TOPIC)
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = GetParameters.Request()

    def send_request(self):
        self.req.names.append("my_array")
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClientAsync()
    response: GetParameters_Response
    response = minimal_client.send_request()
    minimal_client.get_logger().info(
        'Result: for {} '.format(
            response.values
            )
        )

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()