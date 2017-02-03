
3d_milling_workflow
Coding standards for 3D milling

The FABtotum personal FABricator is a RepRap-derived device, and as such shares a common set of CNC standards.

Some Gcodes are not supported, so if your code fails be aware:

    Each line must have a command (G0, G1, etc)
    Comments start with ;
    Unrecognized Milling codes will lock the operation (T1, etc)
    unless changed all movements are in millimeters.

Required Start Gcode:

All 3D milling operations should start with:

M3 S10000 ; set starting speed
G4 S3  ;give it 3 seconds to start the brushless motor.

Required End Gcode:

all 3D milling operations should end with:

G4 S5 ; five seconds before stopping the mill
M5 ; stop the milling motor

3d_milling_workflow.txt · Last modified: 2015/03/09 17:26 by fabtotum
