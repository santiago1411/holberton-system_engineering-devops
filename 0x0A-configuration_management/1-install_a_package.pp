# Check that your Puppet manifest conform to the style guide

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
