#!/bin/bash
case $1 in
	start)
		echo "Starting controller"
		python3 controller.py &
		cd speech_to_controller_integration
		echo "Starting docker containers"
		sudo docker-compose up -d
		echo "Starting intent parser"
		sudo python3 parse-intent.py & 
		cd ..
		for f in widgets/*.py; do
			echo "Starting $f"
			python3 $f &
		done
		echo "Done!, you can run (tail -f /tmp/*.log) to view log output"
		;; 
	stop)
		sudo killall python3
		cd speech_to_controller_integration
		sudo docker-compose stop
		cd ..
		echo "Done!"
		;;
	build) 
		echo "Updating apt-get"
		sudo apt-get update
		echo "Installing docker-compose"
		sudo apt-get install docker-compose
		echo "Installing mosquitto"
		sudo apt-get install mosquitto
		echo "Installing requests"
		sudo pip3 install requests	
		echo "Installing MQTT"
		sudo pip3 install paho-mqtt
		echo "done"
		;;
	*)
		echo "Unknown option, please use one of the following:"
		echo "start: starts all processes"
		echo "stop: stops all processes"
		echo "build: installs dependencies and starts docker containers"
		;;
esac
