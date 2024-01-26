#Puppet script that sets up your web servers for the deployment of web_static.

# Define package and service
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Create directories
file { '/data/web_static/releases/test/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/shared/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create index.html
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test/',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Define Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'file',
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

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
}",
  require => File['/data/web_static/current'],
  notify  => Service['nginx'],
}

# Restart Nginx service
