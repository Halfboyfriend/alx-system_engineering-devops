# Using Puppet, install flask from pip3

package { 'puppet-lint':
  ensure   => 'Flask 2.1.1',
  provider => 'pip3',
}
