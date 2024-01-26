#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.


sudo apt-get update
sudo apt-get install -y nginx
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/


config=\
"server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location / {
        return 301 /hbnb_static/index.html;
    }

    error_page 404 /404.html;
    location /404.html {
      root /var/www/html;
      internal;
    }
}"

echo "$config" | sudo dd status=none of=/etc/nginx/sites-enabled/default
service nginx restart
exit 0
