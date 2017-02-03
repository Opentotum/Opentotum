network

  

Table of Contents


•Network configuration

◦LAN


◦Wi-Fi


◦Connecting to hidden wifi WPA2-PSK network


 
Network configuration


Here you are a guide to how to configure the connection to your new FABtotum personal fabricator. 

LAN


When you connect your computer via ethernet, and you connect to the appropriate IP on your favourite browser, you will see a page like this: 

lan-1.jpg 

This is the FAB UI guided network configuration. 

Create your personal account, by adding name, surname, e-mail and password. 

lan-2.jpg 

Set the static IP in the network where are you connected: you can choose a value from 0 to 255, be careful not to type in an IP that is already in use in the network. 

lan-3.jpg 

Configuration complete! In order to connect to the FABtotum personal fabricator: go to your favourite browser and type the printer's IP in the address bar: in this case the IP is 169.254.1.2lan-4.jpg 

Wi-Fi


To configure the Wi-Fi connection you need to plug the USB Wi-Fi dongle in the USB port on the back of your FABtotum, then click on “Settings” and then “Network”. 

You will see the rank of available networks. 

wifi-1.jpg 

Select and click on your favourite network to access it. Insert your password to connect. 

wifi-2.jpg 

Confirm the selection, et voilà! Your FABtotum is now connected! You can see your IP address on the top-right corner of the screen, use it on your browser to connect to the printer. You can use it without any cable, and you can connect many different FABtotums at the same time. 

wifi-3.jpg 

Connecting to hidden wifi WPA2-PSK network


Connecting to a hidden network is possible but needs some hard coding of the FABtotum. 

First of all connect to your FABtotum by cable/ethernet and log in using putty or anything similar and enter the following details:
 Enter IP nr 169.254.1.2
 Login with user: root
 Default password: fabtotum (will not be shown during typing) 

To be better safe than sorry, backup the network control file.
 Type the following comandes and enter to execute after each line: 
cd /etc/network cp interfaces interfaces_original
(This copies the interface file to a new interfaces_original file) 

The following instructions on how to create a hex version of your Wi-Fi password can be skipped but create an additional layer of security. To create a hex version of it enter the following command: 
wpa_passphrase UR_SSID UR_KEY
(Replace UR_SSID with your network name and UR_KEY with your wifi password) 

The shell will return a long numerical code. You should copy it by selecting the returned code with your cursor (it's now copied to your clipboard). Paste it in a text file as you will need to copy this later on. 

After this preparation we can now finally modify Wi-Fi settings to setup a connection with a hidden wireless network.
 To edit the interfaces configuration file, type the following command (it will open the nano editor): 
nano /etc/network/interfaces
Copy the following code and replace your wlan configuration: 
allow-hotplug wlan0
auto wlan0
iface wlan0 inet dhcp
wpa-ap-scan 2
wpa-scan-ssid 2
wpa-ssid "UR_SSID"
wpa-proto RSN
wpa-pairwise CCMP
wpa-key-mgmt WPA-PSK
wpa-psk UR_HEX_CODE
Replace “UR_SSID” with your network SSID (name) by moving the cursor with your arrow keys, press delete to remove “UR_SSID” and type your network name. (Linux is capital sensitive, use quotation marks if your network name contains spaces) 

Replace UR_HEX_CODE by copying the code you stored in a txt file; paste in nano by moving your cursor into place, press delete to remove UR_HEX_CODE and press right mouse button to paste. 

Press Ctrl+x to close nano, save file without changing the name. 

You're now ready to activate your new settings.
 Restarting the network service should get you up and running, to do so type the following command and press enter to execute: 
service networking restart
If this was not sufficient you can restart your fabtotum by entering the following command and press enter to execute:
 shutdown –r now 

You should be ready to go. 
  
network.txt · Last modified: 2016/08/26 17:18 by fabtotum