"""
ros2 run \
    diagnostic_aggregator \
    aggregator_node \
    --ros-args \
    --params-file /home/user/ros2_ws/src/pkg_python_tutorial/config/diag.yaml
"""
import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    ld = LaunchDescription()

    config = os.path.join(
        get_package_share_directory('pkg_python_tutorial'),
        'config',
        'group_diag.yaml'
        )


    diag_node = ExecuteProcess(
        cmd=[
            "ros2",
            "run",
            "diagnostic_aggregator",
            "aggregator_node",
            "--ros-args",
            "--params-file",
            config
            ],
        name='aggregator_node',
        emulate_tty=True,
        output='screen')


    ld.add_action(diag_node)
    return ld