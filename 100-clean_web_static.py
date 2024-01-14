#!/usr/bin/python3
# Fabfile to delete out-of-date archives.

from fabric.api import *

env.hosts = ['100.26.167.240', '3.83.227.79']
env.user = "ubuntu"


def do_clean(number=0):
    """deletes out-of-date archives"""

    number = int(number)

    if number == 0:
        retval = 1
    else:
        retval = number

    local('cd versions ; ls -t | head -n -{} | xargs rm -rf'.format(retval))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | head -n -{} | xargs rm -rf'.format(path, retval))
