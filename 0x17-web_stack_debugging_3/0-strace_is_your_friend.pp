# File: 0-strace_is_your_friend.pp

file { '/etc/httpd/conf/httpd.conf':
  ensure  => file,
  content => template('path/to/httpd.conf.erb'),
  notify  => Service['httpd'],
}

service { 'httpd':
  ensure  => running,
  enable  => true,
  require => File['/etc/httpd/conf/httpd.conf'],
}
