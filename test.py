#!/usr/bin/python3


archive_path = 'versions/web_static_20170315003959.tgz'
path = '/data/web_static/releases/'
file_name = archive_path.split('/')[1]
no_extention = file_name.split('.')[0]
where_to_unzip = ('{}' + '{}/').format(path, no_extention)
tmp_path = ('/tmp/{}/').format(file_name)

print(file_name)
print(no_extention)
print(where_to_unzip)
print(tmp_path)
