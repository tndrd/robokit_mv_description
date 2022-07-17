#!/usr/bin/env python

import os
import yaml

def load_joint_names(filename='joint_names.yaml'):
    DESCRIPTION_PATH = os.environ['ROBOKIT_DESCRIPTION']
    joint_names = None
    path = f'{DESCRIPTION_PATH}/config/{filename}'
    try:
        with open(path) as yaml_file:
            yaml_content = yaml.load(yaml_file.read(), Loader=yaml.Loader)
            joint_names = yaml_content['controller_joint_names']
    except FileNotFoundError:
        print(f"Error: joint names file not found at {path})")
    return joint_names


for joint in load_joint_names():
    print(f'      <xacro:configure_joint joint_name="{joint}" initial_position="0.0"/>')


