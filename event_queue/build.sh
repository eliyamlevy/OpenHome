#!/bin/bash

echo "Installing golang"

sudo apt-get install golang

echo "Cloning Repo"

git clone git@github.com:bitly/nsq.git

cd nsq

echo "Making build"

make

echo "done"