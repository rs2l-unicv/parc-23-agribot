#!/usr/bin/env python3
import os

from robot_agent import UcvRobotAgent

DEBUG = False

try:
    DEBUG = bool(os.getenv('DEBUG', DEBUG))
except:
    pass

if __name__ == '__main__':
    agent = UcvRobotAgent(debug=DEBUG)
    agent.run()
