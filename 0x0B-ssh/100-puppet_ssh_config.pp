#!/usr/bin/env bash
# seeting up ssh config for client

# Setting up ssh config for client
file_line { 'turn of pass auth':
  ensure => present,
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}

file_line { 'declare identity file (pub key)':
  ensure => present,
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school',

}
