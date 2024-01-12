#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.

from os.path import exists
from fabric.api import put, run, env
env.hosts = ['35.168.2.211', '34.207.58.222']
env.user = "ubuntu"


def do_deploy(archive_path):
    """function do_deploy"""

    path = '/data/web_static/releases/'
    """spliting the archived path at /.
    removing versions dir example:
    versions/web_static_20170315003959.tgz
    """
    file_name = archive_path.split('/')[1]

    " remove .tgz "
    no_extention = file_name.split('.')[0]

    "Set destination path for unziping"
    where_to_unzip = ('{}' + '{}/').format(path, no_extention)

    "Set destination path for storing zipped file"
    tmp_path = ('/tmp/{}').format(file_name)

    if not exists(archive_path):
        return False
    try:
        "Store zipped file in /tmp/"
        put(archive_path, '/tmp/')

        "Create the destination directory"
        run('sudo mkdir -p {}'.format(where_to_unzip))

        "Unzipped the zipped file to the directory created"
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