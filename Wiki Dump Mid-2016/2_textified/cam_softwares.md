
cam_softwares
Table of Contents

    CAM Software
            List of CAM software
            Required Start Gcode:
            Required End Gcode:

CAM Software

CAM software (Computer Aided Manufacturing) are software to generate gcode.
List of CAM software

-MakerCAM Web based software (MakerCAM tutorial)- A MakerCAM postprocessor can be found here

-Jscut Web based software (Jscut tutorial)

-Openscam Gcode simulator (Openscam tutorial). This program allows you to verify whether your gcode is valid

- Autodesk Fusion 360

For more resources check this site.
Required Start Gcode:

All the milling operations should start with the commands that start the brushless motor:

M3 S10000 ; set starting speed
G4 S3  ;give it 3 seconds to start the brushless motor.

Required End Gcode:

all the milling operations should end with:

G4 S5 ; five seconds before stopping the mill
M5 ; stop the milling motor

If your CAM editor doesn't add those commands, open it with a text editor (ex: notepad, textedit) and add previous codes.
cam_softwares.txt · Last modified: 2016/05/23 21:52 by alessio.cavalieri
