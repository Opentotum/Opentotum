slic3r

  

Table of Contents


•Slicing with Slic3r

◦FABtotum Slic3r Profiles


◦Fill patterns


◦


 
Slicing with Slic3r


Slic3r is a free 3D slicing engine for 3D printers. It generates Gcode from 3D files (STL or OBJ). Once finished, an appropriate G- code file for the production of the 3D modeled part or object Is uploaded to the FABUI Object Manager Interface and can be 3D printed. 

Slic3r is an open source project run by Alessandro Ranellucci.
 Binaries can be found here: https://github.com/alexrj/Slic3r 

Windows, MAC OSX, and Linux versions can be downloaded here: slic3r.org/download 

Official Slic3r manual can be found here: manual.slic3r.org/ 

FABtotum Slic3r Profiles


The FABteam has prepared a few preconfigured profiles to help you getting started with slicing on Slic3r. 
 Be aware that a profile might be perfect in some cases but could be just a starting point for more refinements in others. 

You can Download all the FABtotum Configs from Github: 
github.com/FABtotum/FAB_Configs/archive/master.zip 

The names are self explanatory: 
set_1_Fast_Draft.ini
set_2_Slow_High_Quality.ini
set_3_Bracelets.ini
set_4_Vases.ini
set_5_Generic_PLA.ini
set_6_Generic_ABS_small_parts.ini
Fill patterns


With Slic3r you chan choose different fill patterns, here you have different patterns, by choosing this you can decide both printing speed and strength. They are all printed without fill top and bottom layers, using 20% infill. 

fill_patterns.jpg 

From left you have faster prints: 

• Rectilinear


• Hilbert curve 5:29 min


• Archimedean chords 5:30 min


• Line 5:38 min


• 3D honeycomb 6:37 min


• Octagram spiral 7:01 min


• Honeycomb 7:12 min


• Concentric 8:08 min



  
slic3r.txt · Last modified: 2016/05/09 14:01 by jj