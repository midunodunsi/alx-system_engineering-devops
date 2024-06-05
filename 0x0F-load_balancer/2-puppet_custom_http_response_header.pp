# setup new ubuntu server with nginx
# add custom http header

exec { 'update sysytem':
	command => '/usr/bin/apt-get update",
}

package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https:\/\/github.com\/midunodunsi permanent;" /etc/nginx/sites-enabled/default',
	provider => 'shell'
}

exec {'HTTP header':
	command => 'sed -i "25i\	add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default',
	provider => 'shell'
}

service {'nginx':
	ensure => 'running'
	require => Package['nginx']
}
