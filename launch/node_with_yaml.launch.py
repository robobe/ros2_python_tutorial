import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch.actions import LogInfo

def generate_launch_description():
    ld = LaunchDescription()

    config = os.path.join(
        get_package_share_directory('pkg_python_tutorial'),
        'config',
        'params.yaml'
        )

    sim_node =  Node(
            package='pkg_python_tutorial',
            namespace='',
            executable='param_basic',
            name='basic',
            parameters=[config]
        )

    log_launch = LogInfo(msg="---- log launch file ------")

    ld.add_action(log_launch)
    ld.add_action(sim_node)
    return ld