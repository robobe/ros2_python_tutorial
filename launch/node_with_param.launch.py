from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import LogInfo

def generate_launch_description():
    ld = LaunchDescription()

    sim_node =  Node(
            package='pkg_python_tutorial',
            namespace='',
            executable='param_basic',
            name='basic',
            parameters=[
                {"my_str": "data from launch"}
            ]
        )

    log_launch = LogInfo(msg="---- log launch file ------")

    ld.add_action(log_launch)
    ld.add_action(sim_node)
    return ld