# Using Puppet, install flask from pip3

package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'pip3',
}
