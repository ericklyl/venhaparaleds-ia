
import os
import sys


in_docker = os.path.exists('/.dockerenv')


if in_docker:
    sys.path.insert(0, '/app')
else:
    
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))