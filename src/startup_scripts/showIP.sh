#cd ../../boot/
#hostname > this_is_the_ip.txt
#sudo hostname -I > this_is_the_ip.txt


if nmcli general | grep "^connected" >/dev/null
then
   echo "nmcli connected. IP has been written to ../../boot/this_is_the_ip.txt"
   cd ../../boot/
   sudo hostname -I > this_is_the_ip.txt
fi
