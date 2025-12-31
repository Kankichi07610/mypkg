#!/bin/bash
# SPDX-FileCopyrightText: 2025 Kanta Ogasawara
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/ros2_ws/install/setup.bash

# ノード起動
timeout 15 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log 2>&1 &
sleep 5

# トピックがあるか
ros2 topic list | grep -q 'test_talker'

# トピックの型があってるか
ros2 topic info /test_talker | grep -q 'std_msgs/msg/String'

# ログが出ているか
grep -q 'ping_listener' /tmp/mypkg.log

# エラーが出ていないか
! grep -i 'error' /tmp/mypkg.log
