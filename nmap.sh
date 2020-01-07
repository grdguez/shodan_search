#!/bin/bash
cat shodan_log.txt | while read line
do
nmap -sS $line
done
