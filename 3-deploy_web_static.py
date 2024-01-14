#!/usr/bin/python3
# Fabric script to create and distribute an archive to a web server.

from datetime import datetime
from os.path import exists
from fabric.api import put, run, env, local
env.hosts = ['100.26.167.240', '3.83.227.79']
env.user = "ubuntu"


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


def do_deploy(archive_path):
    """function do_deploy"""

    path = '/data/web_static/releases/'
    """spliting the archived path and removing versions"""
    
    file_name = archive_path.split('/')[1]

    " to remove .tgz "
    no_extention = file_name.split('.')[0]

    "to set destination path for unziping"
    where_to_unzip = ('{}' + '{}/').format(path, no_extention)

    "to set destination path for storing zipped file"
    tmp_path = ('/tmp/{}').format(file_name)

    "Excemption output"
    if not exists(archive_path):
        return False
    try:
        "to store zipped file in /tmp/"
        put(archive_path, '/tmp/')

        "to create the destination directory"
        run('sudo mkdir -p {}'.format(where_to_unzip))

        "to Unzipped the zipped file to the directory created"
        run('sudo tar -xzf {} -C {}'.format(tmp_path, where_to_unzip))

        "Remove the zipped file in /tmp/"
        run('sudo rm {}'.format(tmp_path))

        "Transfer the file from <>/web_static/ to <> i.e rm /web_static/."
        run('sudo mv {}web_static/* {}'.format(where_to_unzip, where_to_unzip))

        "Finally removing web_static after file transfer"
        run('sudo rm -rf {}web_static'.format(where_to_unzip))

        "Remove the previous symbolic link"
        run('sudo rm -rf /data/web_static/current')

        "Create another symbolic link"
        run('sudo ln -s {} /data/web_static/current'.format(where_to_unzip))

        print('New version deployed!')
        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """Prototype: def deploy(): 
    Deploy function do_pack and do_deploy.
    """
    path = do_pack()
    if path:
        do_deploy(path)
    return False