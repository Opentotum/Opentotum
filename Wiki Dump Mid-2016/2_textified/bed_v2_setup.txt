
bed_v2_setup
Table of Contents

    FABtotum BED V2 Update
        Purpose
        What you need:
        Procedure:

FABtotum BED V2 Update
Purpose

The FABtotum hybrid bed has arrived after few months of developements: with an improved connection pcb, stronger pogo pins and an improved heat transmission that reduces the time of heating and guarantees a more uniform heating.

Check the specs here.

This tutorial is intended to help you change the plate connection pcb to be used with the new bed.

You can buy the new bed an plate connection pcb in the FABtotum shop: store.fabtotum.com/eu/store/hybrid-bed-v2-91.html
What you need:

    New hybrid bed V2;
    New plate connection PCB, also called relay PCB (plateconn in this tutorial from now on);
    3D printed spacer (Supplied with the new bed);

T8 Torx Key;

    FABtotum M3 Printable tool; (You can find the .stl file on thingiverse);
    Flat screwdriver.
    bed_update_1.jpg

Procedure:

    Raise the Z axis using the command “G28” in FABUI, “JOG”.
    Locate the old plateconn on your FABtotum (see image below).



    Disconnect the two connectors form the old plateconn, the wires lenght are different, so you can recognize them easily.
    If you have bad memory, you can mark one with a sticker.




    Using the M3 Printed tool and the T8 Torx Key, remove the old plateconn from your FABtotum.


    Insert the 3D printed spacer supplied with the bed, being careful to position the red line on the top and the red dot looking at you.

    bed_update_5x.jpg

    Replace the old plateconn with the new one. Start to screw the new plateconn using the M3 printed tool and the T8 Torx key. Don’t fasten the plateconn too much. Make sure the plateconn sits at the spacer angle.



    Place the new bed in position and check the connection between the plateconn and the bed’s pogo pins.
    see: quick setup guide



    The plateconn can now be fastened so that the heated bed connection pins are touching the plateconn consistently. Do not fasten the plateconn too much, otherwise the space between the plateconn and the heated bed will become increasingly small, making the insertion of the heated bed very tricky and potentially damage the pins. The ideal gap should be as shown below:


    When you are satisfied, remove the bed and connect the plateconn back with the two connectors you previously disconnected.

    To test the connection in the FABUI go to “JOG” (1), Raise the bed temp (example: 50°C ) (2), wait until the bed reach the target temperature and digit “G27” (3). Press Run to execute. This will home the bed to the max Z position (lower end).
    You should start seeying the temperature in the bed temperature bar (5).
    The value should not fluctuate.




    At this point the setup is done, but the bed is still not calibrated. Follow the Bed calibration tutorial to calibrate the printing bed.
    You are now ready to use the FABtotum.

bed_v2_setup.txt · Last modified: 2016/04/26 16:30 by jj
