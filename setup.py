from setuptools import setup
import os
from glob import glob

package_name = 'pkg_python_tutorial'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, "launch"), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, "config"), glob('config/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='robo2020@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "rate_demo=pkg_python_tutorial.rate_demo:main",
            "param_basic=pkg_python_tutorial.parameters.basic:main",
            "param_demo=pkg_python_tutorial.parameters.param_demo:main",
            "param_array=pkg_python_tutorial.parameters.param_array:main",
            "param_monitor=pkg_python_tutorial.parameters.param_monitor:main",
            "param_update=pkg_python_tutorial.parameters.param_update_client:main",
            "param_client=pkg_python_tutorial.parameters.param_client:main",
            "diag_basic=pkg_python_tutorial.diagnostics.simple:main",
            "diag_updater=pkg_python_tutorial.diagnostics.updater_with_task:main",
            "diag_updater_monitor=pkg_python_tutorial.diagnostics.updater_with_freq_task:main"
        ],
    },
)
