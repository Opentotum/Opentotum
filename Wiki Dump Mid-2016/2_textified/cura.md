
craftware
Slicing with CraftWare

(this wiki articles is a work in progress, see the forum thread)

Slicing with CraftWare by Craftunique

From their website:

CraftWare is a FREE, fast, easy-to-use slicer software that converts your digital 3D object into a .gcode toolpath format understood by most 3D printers.

It's available for Windows 7+ and MAC OSX 10.7+

This document was written using version Craftware.13 beta #25088 which was the most recent beta version at the time of writing (dec 2015). It is rough guide to get you started using this slicer for the Fabtotum.

It will walk you through all options I needed to set for a successfull print. By all means add information or make corrections to this wiki page! Thanks!

Options:

* Options > General: The general tab contains a few settings that are privacy sensitive: I unchecked 'm all; so no checks for updates, or sharing statistics. If ET wants to phone home he'll have to wait.

* Options > Graphics: All left their default settings.

* Options > Printer:

    0,0 at front left corner
        0 at both offsets (left tot right, front to back)
        Width(x) 214mm
        Depth(y) 234mm
        Height(z) 230mm

I have lowered the height slighty to avoid triggering the Z-stop, though I never print this high. Change this if you need to.

Obviously do not check the checkbox for 'circular platform'.

You could fill in pricing information of your filament. As the units are in meters, it's rather difficult as the filament I buy is priced per weight/roll, and I would not have a clue how many meters are on there.

For a time estimation the slicer wants to know the acceleration of the Fabtotum. The Fablin source on github yields these numbers:

#define DEFAULT_MAX_ACCELERATION   {10000,10000,50,100}
// X, Y, Z, E maximum start speed for accelerated moves.E default values are good for Skeinforge 40+,
for older versions raise them a lot. //

Ofcourse there's an easier way to find the acceleration used by the Fabtotum:
A simple M503 in the JOG gcode console shows:

echo: Maximum Acceleration (mm/s2):
echo: M201 X10000 Y10000 Z50 E100
echo: Acceleration: S=acceleration, T=retract acceleration
echo: M204 S4000.00 T80.00

I used the settings given by M503, as these are the active ones I pressume.

    Max. acceleration : 4000 mm/s 2
    Corner coefficient : 4.000 ( left at default)
    Min speed : 10 mm/s ( left at default)
    Time step : 40 ms ( left at default)

That's all you can fill in here. Press OK to confirm and store these settings.

Now load a simple test object, I used a simple 20x20x~10mm test cube-like object.
The button is at the top of the interface +ADD.

It gets placed at the middle of the virtual build platform.
If you want it somewhere else, rotated, bigger or smaller, use the tools at the top.
When you're happy with it, press the Slice … button at the right.

Bang! Lots and Lots of tabs and options.
But … don't feel overwhelmed, quite a few have a handy preview or hint.

Slice > Basic

Slice > Advanced

Slice > Foundation

Slice > Temperature

Slice > Gcode
craftware.txt · Last modified: 2016/01/11 16:35 by jj
