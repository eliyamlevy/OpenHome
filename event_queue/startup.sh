#!/bin/bash

read -p "Please enter IP address: " ip 

cd nsq/build

echo "Starting lookup"

./nsqlookupd > /tmp/nsqlookupd.log 2>&1 &

sleep 1

echo "Starting admin"

./nsqadmin --lookupd-http-address localhost:4161 > /tmp/nsqadmin.log 2>&1 &

sleep 1

echo "Starting nsq on $ip" 

./nsqd -broadcast-address $ip -lookupd-tcp-address localhost:4160 > /tmp/nsqd.log 2>&1 &