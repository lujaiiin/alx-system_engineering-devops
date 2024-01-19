# Using Puppet, create a manifest that ki
exec { 'pkill':
command => '/usr/bin/pkill -f killmenow'
}
