import rclpy
from rclpy.node import Node
from diagnostic_updater import (Updater,
    HeaderlessTopicDiagnostic,
    FrequencyStatusParam)

PERIOD = 2

class TopicMonitorTask(HeaderlessTopicDiagnostic):
    def __init__(self, name, diag):
        freq = FrequencyStatusParam(freq_bound={
            "min": 0.5,
            "max": 2.5
        })
        super().__init__(name, diag, freq)

class MyNode(Node):
    def __init__(self):
        node_name="minimal"
        super().__init__(node_name)
        self.monitor_task = None
        self.create_timer(PERIOD, self.time_handler)
        self.get_logger().info("Hello ROS2")

    def time_handler(self):
        if self.monitor_task:
            self.get_logger().info("tick")
            self.monitor_task.tick()

    def set_topic_monitor(self, task):
        self.monitor_task = task
        

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    updater = Updater(node)
    monitor_freq_task = TopicMonitorTask("topic_name", updater)
    node.set_topic_monitor(monitor_freq_task)
    updater.setHardwareID("none")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()