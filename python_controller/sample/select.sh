#!/usr/bin/bash
#1)item1
#2)item2
#3)item3
#4)item4
#5)exit
select VAR in item1 item2 item3 item4 exit
do 
	echo 'your selected item is '$VAR
	if [ $VAR = 'exit' ];then
		break
	fi
done