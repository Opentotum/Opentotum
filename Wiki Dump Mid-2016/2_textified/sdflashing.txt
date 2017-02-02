sdflashing

 
Flashing the SD Card


The Latest stable Raspbian image containing the FAB UI ready to be written.
 You can use this image to flash a new SD card with Win32DiskImager or restore the FABtotum SD to factory standard.
 If you have problem flashing the SD card you can try formatting it with https://www.sdcard.org/downloads/formatter_4/ 

Make sure to check for available updates once installed. 

FABUI V 0.953 (LATEST) Official Download (Download.fabtotum.com) ( MD5 ) 

Instructions:


1. Insert the SD card into your SD card reader and check which drive letter was assigned to it. You can easily see the drive letter (for example G: by looking in the left column of Windows Explorer. You can use the SD Card slot (if you have one) or a cheap SD adaptor in a USB port.


2. Download the Win32DiskImager utility from the Sourceforge Project page (it is also a zip file); you can run this from a USB drive.


3. Extract the executable from the zip file and run the Win32DiskImager utility; you may need to run the utility as administrator. Right-click on the file, and select Run as administrator.


4. Select the image file you extracted above.


5. Select the drive letter assigned to the SD card in the device box. Be careful to select the correct drive; if you get the wrong one you can destroy data on the computer's hard disk! If you are using a SD card slot in your computer and can't see the drive in the Win32DiskImager window, try using a cheap SD adaptor in a USB port.


6. Click Write and wait for the writing process to complete.


7. Exit the imager and eject the SD card, put it back in the Raspberry inside the FABtotum.


8. Once the FABtotum is ready, the light will turn solid white and a beep sound will play. You can now conect to the default FABtotum IP (169.254.1.2)



 NOTE: versions older than 0.875 may have troubles working out of the box with the latest hardware (i.e: wifi dongle). 
 If you are unable to use the wifi dongle or are unable to access wifi, make sure to have the latest FABUI image installed. 

NOTE 2: if, looking at the HDMI output, you are being redirected to the recovery mode (i.e the Raspbian NOOBS installer wizard) then reflash the SD and move the carriage to one side, usually on the right. Make sure to not damage the endstops by doing this. The issue is caused by both endstops being normally close in conjunction with an outdated Firmware installed on the FABtotum. 

When the installation ends make sure to update the FABlin firmware and you'll be able to move the carriage. 
  
sdflashing.txt · Last modified: 2016/05/09 15:38 by fabtotum