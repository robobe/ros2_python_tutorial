import threading
import rclpy
from rclpy.node import Node
from diagnostic_updater import (Updater,
    DiagnosticTask
)
from diagnostic_msgs.msg import DiagnosticStatus


class StateTask(DiagnosticTask):
    def __init__(self, name):
        super().__init__(self)
        self.state = False

    def run(self, stat):
        if self.state:
            level = DiagnosticStatus.OK
            msg = "RUNNING"
        else:
            level = DiagnosticStatus.ERROR
            msg = "BROKEN"
        
        stat.summary(level, msg)
        return stat

class GpsNode(Node):
    def __init__(self):
        super().__init__("GPS_NODE")
        self.state_task = StateTask("GPS_TASK")
        self.create_timer(1, self.timer_handler)

    def timer_handler(self):
        self.state_task.state = not self.state_task.state


def main(args=None):
    rclpy.init(args=args)
    node = GpsNode()
    updater = Updater(node)
    updater.setHardwareID("gps")
    updater.add("gps_state",node.state_task.run)
    thread = threading.Thread(target=rclpy.spin, args=(node,), daemon=True)
    thread.start()

    rate = node.create_rate(1)
    while rclpy.ok():
        updater.update()
        rate.sleep()
    thread.join()

if __name__ == "__main__":
    main()

