#!/bin/bash

coproc bluetoothctl 
echo -e 'connect 12:75:58:C7:D5:4E' >&${COPROC[1]}
