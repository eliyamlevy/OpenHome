#!/bin/bash

cd nsq/build

echo "Starting lookup"

./nsqlookupd 

echo "Starting admin"

./nsqadmin --lookupd-http-address localhost:4161

echo "Starting nsq"

./nsqd -lookupd-tcp-address localhost:4160