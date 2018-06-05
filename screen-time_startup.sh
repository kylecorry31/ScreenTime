#! /bin/bash
mkdir -p /screen-time/
touch /screen-time/usage.txt
chmod 777 /screen-time/usage.txt
screen-time daemon /screen-time/usage.txt