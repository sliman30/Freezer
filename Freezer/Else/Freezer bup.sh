#!/bin/bash
clear
#read -p "Enter you username : " username
#stty -echo
#read -p "Enter your password : " password; echo
#stty echo

username=guest
password=guest
hostname=localhost

lftp -u $username,$password $hostname << EOF
set ssl:verify-certificate no
dir -Cl ~/Musique
exit
EOF

read -p "What do you want you listen to ? " song

checksong=$(lftp -c "open -u $username,$password $hostname; set ssl:verify-certificate no; find ~/Musique/ | grep $song")

if [ "$checksong" == "" ];
then
	echo "does not exist : Telechargement de youtube initié !"
	spotdl $song -p "/home/$username/Musique/{title} {artist}.{ext}"
	spotdl $song -p "/home/imane/Musique/{title} {artist}.{ext}"
	#$(lftp -c "open -u $username,$password $hostname; set ssl:verify-certificate no; cd /home/imane/Musique; put /home/$username/Musique/$song ")
else
	echo "song exists"
	stty echo
	lftp -c "open -u $username,$password $hostname; set ssl:verify-certificate no; cd /home/imane/Musique; put /home/$username/Musique/$song "; echo
	stty echo
fi

