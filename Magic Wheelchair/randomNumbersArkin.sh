#!/bin/bash
RANGE=7

echo

number=$RANDOM
let "number %= RANGE"
echo "Random number less than $RANGE --- $number"

echo 

if [ $number -eq 0 ]; then
	cvlc /home/pi/Documents/smash.mp3
else
	if [ $number -eq 1 ]; then
	cvlc /home/pi/Documents/roar.mp3
	elif [ $number -eq 2 ]; then
	cvlc /home/pi/Documents/hulk1.mp3
	elif [ $number -eq 3 ]; then
	cvlc /home/pi/Documents/hulk2.mp3
	elif [ $number -eq 4 ]; then
	cvlc /home/pi/Documents/hulk3.mp3
	elif [ $number -eq 5 ]; then
	cvlc /home/pi/Documents/hulk4.mp3
	elif [ $number -eq 6 ]; then
	cvlc /home/pi/Documents/hulk5.mp3
	elif [ $number -eq 7 ]; then
	cvlc /home/pi/Documents/hulk6.mp3
	fi
fi

echo $number
