# create a manifest that kills a process.

exec { 'killmenow':
  command  => 'pkill -f killmenow',
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell,
}
