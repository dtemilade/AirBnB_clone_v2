#!/usr/bin/python3

# Fabric script that generates a .tgz

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """ This function generates a.tgz archive from the contents
    of the web_static folder, using the function do_pack.
    """
    local('mkdir -p versions')
    time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(time)
    try:
        local('tar -czvf {} web_static'.format(file_path))
        return file_path
    except Exception:
        return None

