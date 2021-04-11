# OpenHome
Security-First Digital Voice Assistant

## To Run NSQ:
./run.sh build

./run.sh start

./run.sh stop

In separate terminal, check that containers are running: sudo docker ps -a

If one isn't running: sudo docker start {{ container_id }}

### Hardware Interface Notes:
To enable mp3 files to be played, install mpg321:

sudo apt install mpg321