#!/bin/bash
cat shodan_log.txt | while read line
do
ping -c 1 $line
done
