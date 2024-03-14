# Increase the ULIMIT
 file_line { 'increase_ulimit_for_nginx':
  ensure => present,
   path   => '/etc/default/nginx',
    line   => 'ulimit -n 4096',
     match => '^ulimit -n',
     } ->

     # Restart Nginx
     exec { 'nginx-restart':
      command => 'nginx restart',
       path    => '/usr/sbin:/usr/bin:/sbin:/bin', # Adjust the path as necessary
        require => File_line['increase_ulimit_for_nginx'],
        }
