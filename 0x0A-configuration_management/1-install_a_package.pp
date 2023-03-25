# Using Puppet, install flask from pip3

package { 'puppet-lint':
  ensure   => 'flask2.1.1',
  provider => 'pip3',
}
