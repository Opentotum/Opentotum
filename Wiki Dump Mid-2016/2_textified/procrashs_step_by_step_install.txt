

procrashs_step_by_step_install

  

Table of Contents


•Installing from a Windows environment.


•Installing On linux ( debian or a derivative)


•Installing On a Mac.


•

 
The following Guide was kindly provided by Procrash for the Fabtotum Community. 
 You Will need an ssh client installed on your machine. There are several ways to do it but I use the console for it. 

Automatic install 

You can download the Advanced Bed leveling plugin here 

Extract files into the /var/www/fabui/application/plugins folder or use the FAB UI plugin uploader tool.

 Then with an SSH client connect to your fabtotum and enter the following:

cd /var/www/fabui/application/plugins/assets

 ./flashFirmware.sh 

This will install the custom Firmware needed by the plugin. 

Installing from a Windows environment.


Putty and winscp would probably be more the preferred solution. 

If you're using putty copy the unpacked dist.zip folder via winscp as a whole folder into /var/www on your fabtotum printer.
 Then use putty to ssh into your fabtotum printer 

on the fabtotum command line enter the following 

cd /var/www/dist 

apt-get install sshpass 

./install.sh YOUR_PRINTERS_IP_ADRESS 


 That's it. Note that sshpass could be perhaps avoided and that you need to reset your control board after the flashing was done. You can do this in the jog menu of the fabtotutum web UI.
 You notice that the installation is working as the ambient light changed when starting to print for the bed height measurement. Also feedrates for the measurement are reduced. And the bed calibration lowers down even for a single screw measurement always the probe several times. 

Installing On linux ( debian or a derivative)


If your a linux or a mac user you need to install sshpass first.
 just unpack the folder anywhere, then do a 

apt-get install sshpass
 ./install.sh YOUR_PRINTERS_IP_ADRESS 

directly on your linux machine and everything is fine.
 Also don't forget to reset your control board after the flash process. 

Installing On a Mac.




you need to install sshpass as well but the installation process is different. Search for brew or install macports first.
 After installation go into your terminal and install sshpass via 

sudo ports install sshpass  

For this you have to enable the admin user first. I think you can do this via preference menus.
 Then follow the linux installation procedure. 
  
procrashs_step_by_step_install.txt · Last modified: 2014/12/16 01:08 by fabtotum
 
--------------------------------------------------------------------------------
