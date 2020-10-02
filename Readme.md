
# DEPRICATED - RFE - #1810


# Relicense BIGIP

## Purpose

This repo demonstrates relicensing a BIG-IP using ansible

## Pre-req's

Docker

## Steps

* ### clone the repo

* ### modify hosts file to point to the IP of your BIG-IP

* ### build and run the container

``` docker-compose run relicense```

* ### Once in the container, run the playbook using the following command.

``` ansible-playbook relicense.yml -i hosts ```

It will ask you for username, password. Username and password can be any read only user on the big-ip. 
