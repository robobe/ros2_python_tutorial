import rclpy
from rclpy.node import Node
from diagnostic_updater import (Updater, 
    DiagnosticStatusWrapper, 
    DiagnosticTask,
    FunctionDiagnosticTask,
    CompositeDiagnosticTask,
    HeaderlessTopicDiagnostic,
    FrequencyStatusParam
    )
from diagnostic_msgs.msg import DiagnosticStatus
from std_msgs.msg import Bool
from rclpy.qos import qos_profile_system_default

time_to_launch = 0


def dummy_diagnostic(state: DiagnosticStatusWrapper):
    if time_to_launch < 10:
        # summary for formatted text.
        state.summary(DiagnosticStatus.ERROR,
            "Buckle your seat belt. Launch in %f seconds!" % time_to_launch)
    else:
        # summary for unformatted text. It's just the same ;)
        state.summary(DiagnosticStatus.OK,
            "Launch is in a long time. Have a soda.")

    return state

class DummyClass:
    def produce_diagnostics(self, stat: DiagnosticStatusWrapper):
        stat.summary(DiagnosticStatus.WARN, "This is a silly updater.")
        stat.add("Stupidity of this updater", "1000.")
        return stat

def check_lower_bound(stat):
    if time_to_launch > 5:
        stat.summary(DiagnosticStatus.OK, "Lower-bound OK")
    else:
        stat.summary(DiagnosticStatus.ERROR, "Too low")
    stat.add("Low-Side Margin", str(time_to_launch - 5))
    return stat


def check_upper_bound(stat):
    if time_to_launch < 10:
        stat.summary(DiagnosticStatus.OK, "Upper-bound OK")
    else:
        stat.summary(DiagnosticStatus.WARN, "Too high")
    stat.add("Top-Side Margin", str(10 - time_to_launch))
    return stat

class DummyTask(DiagnosticTask):
    def __init__(self):
        super().__init__(self,"Updater Derived from DiagnosticTask")

    def run(self, stat):
        stat.summary(DiagnosticStatus.WARN,
            "This is another silly updater.")
        stat.add("Stupidicity of this updater", "2000.")
        return stat

class SimpleNode(Node):
    def __init__(self):
        super().__init__('diag_updater')
        self.get_logger().info("updater diagnostic")
        self.pub1 = self.create_publisher(Bool, "topic1", qos_profile=qos_profile_system_default)

        

def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    updater = Updater(node)
    updater.setHardwareID("none")
    updater.add("function updater", dummy_diagnostic)
    dc = DummyClass()
    updater.add("method updater", dc.produce_diagnostics)
    lower = FunctionDiagnosticTask("Lower-bound check",
        check_lower_bound)
    upper = FunctionDiagnosticTask("Upper-bound check",
        check_upper_bound)
    bounds = CompositeDiagnosticTask("Bound check")
    bounds.addTask(lower)
    bounds.addTask(upper)
    updater.add(bounds)
    updater.broadcast(b"0", "Doing important initialization stuff.")

    freq_bounds = {'min':0.5, 'max':2}
    pub1_freq = HeaderlessTopicDiagnostic("topic1", updater, FrequencyStatusParam(freq_bounds, 0.1, 10))
    pub1_freq.addTask(lower)
    updater.force_update()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()