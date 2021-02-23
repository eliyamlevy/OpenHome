#!/bin/bash

case $1 in

	start)

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
		echo "Done!, you can run (tail -f /tmp/nsqd*.log) to view log output"
		;; 

	stop)
		for p in nsqd nsqadmin nsqlookupd ; do 
			echo "Stopping $p"
			killall -9 $p
		done
		echo "Done!"
		;;

	build) 
		echo "Updating apt-get"
		sudo apt-get update
		
		echo "Installing golang"
		sudo apt-get install golang

		echo "Installing py nsq"
		pip install pynsq

		echo "Cloning Repo"
		git clone git@github.com:bitly/nsq.git

		cd nsq
		echo "Making build"

		make
		echo "done"

		
		;;

	*)
		echo "Unknown option, please use one of the following:"
		echo "start: starts all nsq processes"
		echo "stop: stops all nsq processes"
		echo "build: instals golang, nsq py module and build nsq binaries from github"
		;;

esac

