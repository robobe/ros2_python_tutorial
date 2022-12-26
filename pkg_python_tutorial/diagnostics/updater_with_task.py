import rclpy
from rclpy.node import Node
from diagnostic_updater import (Updater,
    DiagnosticStatusWrapper,
    DiagnosticTask)
from diagnostic_msgs.msg import DiagnosticStatus

PERIOD = 2

class DummyTask(DiagnosticTask):
    def __init__(self):
        super().__init__("Simple_Task")
        self.__state = False

    def run(self, stat: DiagnosticStatusWrapper):
        if self.__state:
            msg = "RUNNING"
            level = DiagnosticStatus.OK
        else:
            msg = "BROKEN"
            level = DiagnosticStatus.ERROR
        stat.summary(level, msg)
        return stat

    
    def set_state(self, state):
        self.__state = state


class MyNode(Node):
    def __init__(self):
        node_name="minimal"
        super().__init__(node_name)
        self.__state = False
        self.dummy_task = DummyTask()
        self.create_timer(PERIOD, self.time_handler)
        self.get_logger().info("Hello ROS2")

    def time_handler(self):
        self.__state = not self.__state
        self.dummy_task.set_state(self.__state)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    updater = Updater(node)
    updater.add(node.dummy_task)
    updater.setHardwareID("none")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()