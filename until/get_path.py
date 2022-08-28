import os
import sys


def get_project_path():
    p_name = os.path.realpath(sys.argv[0])
    # p_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.dirname(p_name)
    # return p_path[:p_path.index(p_name) + len(p_name)]
    return path


if __name__ == '__main__':
    print(get_project_path())