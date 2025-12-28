import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    talker = launch_ros.actions.Node(
        package='mypkg',
        executable='ping_talker',
        )

    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='ping_listener',
        output='screen'
        )

    return launch.LaunchDescription([ping_talker, ping_listener])
