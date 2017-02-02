
bedscan
Table of Contents

    BedScan Plugin by imarin
        Features
        Installation
        Output
        Tips

BedScan Plugin by imarin

Warning! This page is a draft

The Bed Scan Plugin was developed by imarin and gives a false-color map of the planarity of the hybrid bed of the FABtotum.
Features

    It performs a probe scan of the bed approx each 18×18 mm
    It presents a false color graph indicating the Z axis variations.
    It is intended to be used to test how parallel the core XY and the heated bed are, as well as any dependency with respect to X and Y positions.

Installation

    Download the plugin here
    In the FABtotum dashboard go to “Plugins” (1) section and click “Add new” (2).

Select the path of your plugin file, then “Install now”.

The installing process will start, it will be finished in few seconds.

In the “plugins” page press the green button “ Activate”, now you will see “Bedscan” on the left column.

The installation process is complete.
Output

After launching a scan cycle you will see your FABtotum scanning the bed plane using the probe, after the scan cycle you will see the output like this:

Tips

    Remove every residue of tape or hair spray before launching the scan.
    Launch a bed calibration procedure before launching the scan (In the image upper here, you can notice the glass was flat, but the printing bed wasn't planar.
    Consider the range: you will always see colors varying from red to blue, but consider the scale used. In this case the difference is 0.63mm

You can continue developing this plugin on the GitHub repository.
bedscan.txt · Last modified: 2016/05/06 17:00 by jj
