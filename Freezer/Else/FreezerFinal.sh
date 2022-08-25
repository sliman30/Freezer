#!/bin/bash
read -p "Enter you username : " username
stty -echo
read -p "Enter your password : " password; echo
stty echo

#username=slim
#password=sss
hostname=10.125.24.56

lftp -u $username,$password $hostname << EOF
set ssl:verify-certificate no
dir -Cl /
exit
EOF
while true
do
	read -p "What do you want you listen to ? " song

	checksong=$(lftp -c "open -u $username,$password $hostname; set ssl:verify-certificate no; find / | grep $song")

	if [ "$checksong" == "" ];
	then
		echo "does not exist : Download from youtube initiated !"
		spotdl $song -p "/home/imane/Musique/{title}-{artist}.{ext}"
		sshpass -p $password ssh $username@$hostname spotdl $song -p "/home/'$username'/Music/{title}-{artist}.{ext}"
		#lftp -c "open -u $username,$password $hostname; set ssl:verify-certificate no; put -O /home/$username/Musique/ /home/imane/Musique/$song.mp3";
	else
		echo "song exists"

		var=$(lftp -c "open -u $username,$password $hostname; set ssl:verify-certificate no; find ~/Music | grep $song" )
		echo $var
		cd /home/imane/Musique
		lftp -c "open -u $username,$password $hostname; set ssl:verify-certificate no; get $var" 
	fi
done
