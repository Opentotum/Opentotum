pcb_milling_workflow2

  

Table of Contents


•PCB Milling (without the PCB Mill plugin)

◦What you will need


◦The sacrificial layer


◦Creating Gerber and Excelon files from Eagle


◦Using FlatCAM to conver your files to G-code


◦Editing the G-code


◦Milling the board


 
PCB Milling (without the PCB Mill plugin)


This page is a work in progress, and not complete! 

What you will need


In order to properly mill a PCB, you will need a few tools in addition to your FABtotum. The short list of tools is : 

• An appropriate V-mill or endmill. – Different people have different options on what the best mill is. There is a pretty good discussion of various mills on the other PCB Milling page on this wiki. I suggest starting out with some cheap ones from eBay.


• Small drill bits. – If you plan to drill the holes in your PCB using the FABtotum, you will need some very small drill bits to do this. Again, eBay is a pretty good place to find a set of small drill bits.


• Copper clad board. – You have to have something to mill, right? One thing to be sure of is that the PCBs you get are thick enough to be milled! I accidentally ordered a bunch of PCBs off eBay that were the same thickness as the depth of the mill I was using!


• A “sacrificial layer” – This is fancy-speak for something like a piece of MDF that you don't mind drilling holes in and basically destroying. It is there to keep you from drilling in to the metal on the FABtotum's bed. I picked up an inexpensive piece of MDF at the local hardware store for around 6 USD. It is long and skinny, so I can cut smaller pieces out of it as I need to replace my layer.


• A board layout – You can design this using the free version of Eagle CAD, or something like KiCad. This page is all based on using the free version of Eagle CAD, but I suspect it wouldn't be too much different in other schematic design/board layout apps.


• A copy of FlatCAM – You can get it from flatcam.org.


The sacrificial layer


Grab the board that you purchased for your sacrificial layer. If you have not purchased one yet, you want to find a piece of wood that won't splinter a bunch when you cut or drill it. This piece of wood should probably be 1/2-3/4 of an inch in thickness, just to keep your bed safe. I am using an inexpensive piece of MDF, and it seems to work fairly well. Measure the bed in your FABtotum, and cut the piece of wood a bit smaller, so that it will easily fit inside the FABtotum. Then, drill some holes in the wood, and attach the wood to the bed of the FABtotum using the holes that are on the bed. (Note : If you are looking at your bed, and don't see any holes, then pull it out and flip it over. There should be a piece of glass on one side, and a piece of sheet metal with holes on the other.) 

You have probably already done your best to level the bed, but it still may not be quite level. So, you can use the milling head of the FABtotum to make sure the piece of wood has a perfectly level surface, from the perspective of the milling head. Put a mill in the head, and run a “bed leveling” G-code script. 

(Note : There is a way to create a bed leveling G-code script using FlatCAM, but it doesn't seem to create a fully leveled bed. I am working on an app that will create a G-code script for a fully leveled bed, and will add that here later.) 

Once the script has run, you should have a square space on your sacrificial layer that is large enough to fit one of the boards you plan to mill. 

Next, you want to drill the sacrificial layer so that you can put screws in place to hold copper clad board that you intend to mill. The screws will serve two purposes, one is to keep the board from slipping around while it is being milled, the other is to make sure it is properly aligned when you flip it over. 

I originally tried putting one screw on each side of the board, and while that did a fine job of holding the board steady, it didn't do a very good job of aligning it when I flipped it over. 

So, I ended up putting one screw on each of the short sides, and adding two additional screws (for a total of 3) on the each of the longer sides. (I believe you could use two on each of the longer sides, but since I already had a single screw in the middle of each long side, I decided to use 3 total.) 

The placement of the screws should be just off the side of the board so that when the screw is tightened, the head can press down on the board. To get those holes in the right place, I simply used the “Jog” screen on the FABtotum, and used a V-mill to bore in to the sacrificial layer about 5-6mm. This created a pilot hole that was large enough for me to put a #8 wood screw in to the sacrificial layer. You will probably want to use pan-head screws that are flat on the bottom so that you don't cause the board to warp as you tighten down the screws. As an additional advantage, using the milling head to drill the pilot holes, you will be pretty sure that the board is aligned along the long side (and, assuming your board has square edges, that will make you sure that you are aligned along the short side). 

**** NOTE **** – There is a *VERY* good chance that drilling these holes will break the fine tip off the end of the V-mill that you use. You should consider using an old one, and marking it as the bit you use for drilling such holes. (If you use different sizes of copper clad board, you will have to drill holes in different locations.) 

To drill the holes, I first put a piece of the copper clad board on the leveled portion of the sacrificial layer. I then used the “Jog” screen to move the head so that the V-mill would be just BARELY off the board when it was at its widest point. I then moved the Z-axis up until it was touching the sacrificial layer. Next, I set the Z-axis movement to 1mm, and moved the Z-axis so that there was about 1mm between the tip of the V-mill and the sacrificial layer. 

At this point, you just need to start the mill head spinning, and then slowly lower the mill in to the sacrificial layer as deep as you want the pilot hole to be. To get the mill spinning, you use the box in the bottom left corner of the jog screen, enter the G-code “M03 S15000” (to start the mill spinning at 15000 RPM), and then use the Z-axis controls to raise the bed 5-6mm (which will result in a hole 5-6mm deep). 

**** NOTE **** – Be sure you change the Z-axis movement to only move ~1mm at a time! If you attempt to use the default of 5mm there is a *VERY* good chance that you will stall the motor on the FABtotum head, or worse, snap the V-mill in half!! (Flying V-mills are known to be bad for your health!!) 

Once you have drilled as deep as you want to go, back the head out by lowering the board until the V-mill is completely exposed again. If you need to drill another hole on the same side of the board, use the jog controls to move the head alongn the Y-axis to the point you want to drill the next hole. Once you have drilled all of the holes for one side, enter the G-code “M05” in to the window in the bottom left corner of the jog screen to stop the head from spinning. 

Repeat the process above until you have drilled all of the holes you need to hold the board in place, and to align it properly when you flip it over. 

Creating Gerber and Excelon files from Eagle


There are a bunch of different ways to design a board. I elected to use the free version of Eagle CAD, so these instructions will work from the perspective of Eagle CAD. However, the steps for using other programs are likely to be very similar. (Note, this is not a tutorial on using Eagle CAD. There are some really good tutorials out there already, a quick search should turn up a few good ones.) 

Once you have your board layout done, save it and then go to “File | CAM Processor”. On the right hand side of the dialog that comes up, you will see a list of layers that are associated with the board. 

In the “Output” box, select “GERBER_RS274X”. Then, click the “File” button, and create a file that indicates this if the “front” of your board. On the right hand side, there is a list of layers. Select “Top”, “Pads”, and “Vias”, and make sure everything else is deselected. (You will need to scroll down, there are quite a few selected by default.) Once you make sure you only have the correct ones selected, click the “Process Job” button, and the Gerber file for the top of your board will be created. 

Next, click the “File” button, and create a file name that indicates it is the back of your board. In the right hand list, deselect the “Top”, select the “Bottom” and leave “Pads” and “Vias” selected. Finally, click the “Process Job” button again to generate the Gerber file for the bottom side of your board. 

Finally, if you are going to have the FABtotum drill holes in your board, you need to create an Excellon file that indicates where the holes should be drilled. In the “Output” box, select “EXCELON_24” as the Device type. Then, click the “File” button, and create a file name that indicates this is the drills for your board. Then, in the list on the right, unselected everything except “Drills”. You will get a warning dialog from Eagle suggesting you include “Holes” in addition to drills. Ignore it, and continue. 

You are now done working with Eagle. You can close it if you wish. 

Using FlatCAM to conver your files to G-code


Now that we have Gerber files and an Excelon file, we need to go through the process of converting those to a G-code file that the FABtotum can use to make our board. 

FlatCAM started for me in inches mode, but the FABtotum uses millimeter mode, so the first thing we need to do is change FlatCAM to use millimeters. To do that, start FlatCAM, select the “Options” tab, and change the “Units” from “inch” to “mm”. While we are at it, we should also set FlatCAM to understand the Excellon files that come out of Eagle. To do that, select the “Tool” menu, and then “Command Line”. This will open a small command line shell where we need to enter a command. In that window, enter the command “set_sys excellon_zeros T”. Once you enter that command, it will permanently change that setting. However, to keep FlatCAM in millimeter mode, we need to select the “File | Save Defaults” option. 

At this point, to get millimeter mode working, I had to close FlatCAM and restart it. So, it would be a good idea to do that now. 

Back in FlatCAM, select “File | Open Gerber..” and open the top and bottom files that you created with Eagle. Then, select “File | Open Excelon…” and open the drill file that you created with Eagle. As each file is opened, it should be drawn on the grid located on the right side of the application window. 

This is one of the first places that things can go horribly wrong if you don't know what you are doing. (I think I pretty much did everything wrong at some point, and butchered several copper clad boards in the process!) 

Before you do ANYTHING else with FlatCAM, you need to take *EXACT* measurements of the copper clad board you will be using. If your measurements are off by even a little, your board won't come out correctly!!! 

Once you know the measurements of your board, select the “Tool” tab in the box on the left. The tool tab allows you to specify which Gerber file is the front and which one is the back. (Or, the top and bottom, or however you want to name them.) What we are going to do with this tool is to mirror the back side of the board so that it is milled in the correct location on the copper clad board. When I mill a board, I tend to flip it across the X axis. (That is, the edge farthest to the back of the FABtotum becomes the edge closest to the front when I flip it.) So, I select the “X” radio button. I then set my Axis location to “Point”. Also, to remind myself to flip the board the right way, I used a sharpie marker to write “Flip” with arrows pointing the flip direction on the sacraficial layer. 

This is the first place that the EXACT size of your board will come in to play. Unless your design perfectly (and I mean PERFECTLY) fills your board, you will end up with the mirrored image of the back side of the board offset from the front. (If you think about this for a second, it will make sense. Consider where the milling marks will be when you flip the board. You want to align the top and bottom milling marks.) So, in the “Point/Box” field, you want to set the Y coordinate to be dead center of the physical size of the board. The X coordinate really doesn't matter if we are only mirroring across the X axis, but I usually try to get it somewhere near the middle of the board as well. 

As for the drill diameter, it should only be needed if you are going to use alignment holes. I generally don't, so I leave this at whatever the default value is. 

Once you have everything set, click on the “Mirror Object” button. Now, look closely at the mirrored image in the box on the right. Flip it over in your head, and make sure that when holes are drilled they will go through the right locations. I didn't do this at first, and ended up with a board that didn't line up! 

You should now select the “Project” tab, which should take you back to the list of files that you previously opened. I usually start by milling the bottom first, so select the file name for the bottom portion of your board. (The order here really doesn't matter, but work with me. ;) Once you have selected the file, change to the “Selected” tab. Leave all of the defaults alone, except for the values under “Isolation routing”. Under “Isolation routing” you want to set the tool diameter to whatever the diameter of your V-mill (or endmill) is at the depth that you plan to mill to. If you want, you can do multiple passes and have them overlap. But, I find a single pass to be enough as long as I mill deep enough. Once you have set those values, click on the “Generate Geometry” button. You should notice the drawing on the right side of the window will how have an outline around the traces on your board. 

Switch back to the “Project” tab, and you should notice that a new file is listed. It will be the same name as the file you were working with, but will have “iso” appended to it. Select this new file, and switch to the “Selected” tab again. Again, leave all the defaults alone, and fill in the values under the “Create CNC Job” header. For milling the board, I usually set the feed rate to 400,00 or less. For drilling holes in the board, I like to set the feed rate to around 30.00. (You don't want to shove the drill bit in to the board too fast, or it may break!) For the spindle speed, I usually use 15000. The “Travel Z” value sets how high the bit should be above the board when the head is moving to a new location. I usually use 1.0, but you can probably get away with 0.5 safely. The “Cut Z” value is probably the most important, and hardest to get right. This is how deep the mill head should be put in to the board. Lately, I have been using a value of 0.15, but you may need to do some testing to figure out what works best for you. Once you have all of your values set, click the “Generate” button. Now, switch back to the “Project” tab, and you should notice yet another new file is listed. It will also have the same name as the original, but will now have the extension “iso_cnc” appended to it. Select this new file, and switch to the “Selected” tab again. Make sure the “Tool dia” value is set to the diameter of the V-mill you are using, and then click the “Export G-code” button. You should now be prompted to name the file that will be created. Give it a name (usually ending in .gcode), and click Okay. Congratulations! You have just set up the G-codes for milling one side of the board! 

Now, repeat the same steps for the other side of the board. 

Once you have created G-codes for both sides of the board, you want to create the G-codes for drilling the holes in the board. The steps are very similar to creating the G-codes to mill the board. From the “Project” tab, select the file name for the drills, and then switch to the “Selected” tab. You will see a list of drill sizes. You can select all of them, and create a single drill file, or you can select a single one, create a drill file, then select the next one and create a drill file. It is simply a matter of following these instructions multiple times instead of a single time. So, select the drill holes that you want to use, then set the values under “Create CNC job”. I usually set “Cut Z” to 3.0mm so that I get all the way through the board, and poke a little bit of a hole in the sacrificial layer under it. I also usually set the feed rate to around 30 so that the drill bit isn't shoved in too fast. Once you have the values set how you want them, click the “Generate” button. 

Now, switch back to the “Project” tab. You should see another new file created. It will be named the same as your drill file, but will have the “_cnc” extension on it. Select that file, and switch to the “Selected” tab. On the “Selected” tab, make sure your tool diameter is set correctly, and then click the “Export G-code” button. Give your drill file a name (usually ending with .gcode) and you are done! 

Editing the G-code


The G-code that comes out of FlatCAM doesn't quite seem to be what the FABtotum expects to see. In addition, there is a bug in how the FABtotum processes the G-code that can result in the spindle stopping while the head is still moving. So, I had to hand edit the G-code a little bit to make everything work correctly. 

With your favorite text editor, open up the G-code file that you created with FlatCAM. The beginning of every G-code file that FlatCAM has created for me looks like this (with some minor differences) : 

G21
 G90 
 G94 
 F400.00 
 G00 Z1.0000 
 M03 S15000 
 G04 P1 


 These G-codes define how the head should start up. Everything after these are the codes to move the head around to mill the board. (It is easy to search the net to find what all of these codes do, so I won't bother explaining them here.) 

The first thing we need to change is this set of lines : 

G94 
 F400.00 


 Note that your G-codes may have a different value where I have “F400”. The “F400” defines the feed rate that should be used while milling. However, the change you need to make will be the same no matter what the value is. For this first change, you want to change these two lines in to a single line, like this : 

G94 F400.00 

The rest of the lines in the group above can be left how they are. 

The next line you want to change is the VERY last line in the file. FlatCAM sets this line to : 

M05 

This G-code tells the FABtotum to stop spinning the spindle. However, a bug in the latest FABtotum firmware can result in this G-code being processed early, and the head shutting down. Since the FABtotum shuts down the head when the milling is complete, we don't actually need this G-code. 

However, I usually replace it with something like this : 

G04 P500 

The G04 G-code basically tells the FABtotum to wait for a short period of time. Using this G-code probably doesn't make a difference, but I do it anyway, as it has always resulted in the spindle spinning during the entire time the mill is running. 

One other change that you may want to make is to append the feed rate to each of the “G00” and “G01” G-codes. In theory, the “G94 F400.00” G-code that we already fixed should set the feed rate for the whole project to 400.00. However, it doesn't always seem to work that way. Instead if you append the feed rate to each line, you can be fairly sure that the correct feed rate is used while you mill. To append this value to each line easily, I use Notepad++, use Find/Replace, set it to use regex, and in the “Find” line, I put “$” (without quotes). In the “Replace” line, I put “ F400.00” (again, without quotes, but WITH the leading space!). Then, clicking the “Replace All” button will add “ F400.00” to the end of each line. Then, you need to go back and remove the added “ F400.00” from blank lines, and the G-codes at the top of the file. (Basically, if the line doesn't start with G00 or G01, you probably don't want the “F400.00” on the end.) 

Milling the board


<Coming soon> 
  
pcb_milling_workflow2.txt · Last modified: 2016/03/24 11:10 by jj