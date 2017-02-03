pcb_milling_workflow

  

Table of Contents


•I. Preparation steps

◦1. Creating an appropriate sacrifical layer


◦2. Selecting the tools and manufacturing parameters


◦3. Feed rate experiments



•II. Designing your PCB

◦1. Designing with KiCAD

◾1.1. DRC rules


◾1.2. Setting a reference point for manufacturing


◾1.3. Creating the Gerber files for manufacturing




•III. From Gerber/DXF to Gcode

◦1. Why do I need to do this?


◦2. FlatCAM

◾2.1. The software


◾2.2. Application Defaults


◾2.3. A practical example



◦3. Heekscad



•IV. Manufacturing the Gcode with the FABtotum

◦1. Manufacturing using FAB-UI's substractive manufacturing


◦2. Manufacturing using PCBMill FAB-UI plugin

◾2.1. Overview


◾2.3. Do I need auto-leveling for milling PCBs?


◾2.3. Status


◾2.4. Installing PCBMill


◾2.5. Checking firmware installation


◾2.6. PCB Examples




•V. Advanced PCB Manufacturing Examples

◦1. Introduction


◦2. Example 1

◾2.1. Preparation / tools


◾2.2. PCB design


◾2.3. From Gerber/DXF to Gcode


◾2.4. Manufacturing with FAB-UI PCBMill plugin


◾2.5. Gcode files



 
I. Preparation steps



1. Creating an appropriate sacrifical layer


Yes, you can mill a with almost any sacrifical layer. However, in order to decrease the amount of problems a sacrifical layer should comply with some requirements: 

1. The sacrificial layer is substantially flat. I do not mean leveled, I mean flat. This is because even when using the autoleveling in the PCBMill plugin, if the support is substantially flat, there will be less amount of “play” (movement) between the PCB and the support while probing on it and milling it (so in situations were the PCB is under a perpendicular force, which may even be of a different magnitude while probing and milling). 

2. The attachment means. Yes it is possible to use double sided tape, but this would differentially increase the distance between PCB and support. The same applies in the case that you try attachments in the border of the PCB that introduce some force in the direction of the PCB in addition to the for in the perpendicular of the PCB. A plurality of the former forces will tend to bend the PCB in the center area outwards, creating an area of no contact between sacrificial layer and PCB, which varies depending on the force exerted during probing/milling, thereby arriving to inconsistent results. 

3. The sacrificial layer should mount tightly to the subtractive side of the bed and preferably consistently in the same position. In particular, the PCB clad surface for two-sided PCBs is maximized when a PCB clad can consistently be oriented so that two opposite edges are parallel to the X axis of the FABtotum, so that when the copper clad is flipped over the Y axis to manufacture the other side, the Y axis used for mirroring the PCB is substantially equal to the FABtotum Y axis. 

I am currently making holes near the corners of the PCBs to attach it firmly to the sacrificial layer. But these holes have to be made with a certain precision so that no tangential forces (as opposed to the perpendicular forces) are generated. The same holes are so arranged as to facilitate the manufacturing of two sided PCBs. 

2. Selecting the tools and manufacturing parameters


Selecting the right tool is not an easy task. I do not pretend to cover here exhaustively every parameter to consider as first is not the aim of this section and second I do not have the knowledge to do it properly. After some googling I have drawn my own conclusions (that might not be right):
 

1. Rpms: For PCBs you generally want rpms in the range of 10k-15k. This is a matter of using a faster feedrate to decrease the manufacturing time than that which could be achieved at lower rpms. The pros seem to do this at 50k to 100k.


2. Tool deflection: Tool deflection is very important. Basically if when you move the head and the mill is in contact with the PCB, the mill will have a component of force (friction) perpendicular to its axis and in the opposite to the direction of movement of the head. This force will tend to deflect (“bend”) the tool so that it is no longer perpendicular to the bed, but within the limits of the flexibility/rigidity of the tool tend to follow the head. You probably thought about it already, if this force is too big, the tool will break. This is the case of the tips of V mills and the the point of connection of the mill to the shaft for thin mills like 0.2 mm mills. So, if you mill is thin, your feedrate will be more limited. This is additionally limited by the depth of cut, or how much the mill enters into the material while cutting. The higher the depth of cut, the higher the force, the higher the tool deflection. It is relevant to note that not only the danger of breaking the tool plays a role, but also the deflection leads to the tip of the mill not following the same path as the head, so it also leads to lack of accuracy (this can be seen nicely using a 0.2 mm endmill, as you increase the feed rate you will see that it goes from cutting straight to bending and thus cutting a different path, so probably in your pad instead of around your pad).


3. Depth of cut: The first obvious link is that if you plunge deeper into your material, you have to go at a slower feedrate. The second link is with tool deflection, the more you plunge the more deflection you will have.


4. Vertical feedrate: This is very important. More mills (except boring mills) are designed to cut in the horizontal plane and are not good at cutting vertically, so the vertical feedrate (used to enter until the depth of cut) has to be very slow for the sake of the endurance of the tool.


5. Horizontal feedrate: Too low and the cut is not nice and the tool may dull. Too high and the cut will not be nice and the tool may break or endure less. There is an optimum point that varies at the tool ages. Within this “normal usage range”, lower means it ages slowlier but also takes more time to route, higher means it ages faster but takes less time to route a PCB.


My way around this is fix the rpms (the FAB goes to 15k which is not much, so it is usually not a limiting factor for the tools and PCB manufacturing) Try to fix the DoC (unless the manufacturer of the bit tells you what you should use) Check tool deflection with a simulator determine the horizontal feedrate. 

So now that we talked about the parameters, let's talk about the mills. By Googling you may discover that there are two ways to go: 

1. China eBay mills (around 20 Euros per 10 mills): There is no endmill under 0.8 mm that is a real endmill. All those that appear with lower values are “drilling mills” and are not suitable for horizontal cutting. Once this is said, if you are going to do thru-hole PCBs, then it may make sense to buy a set of difference drill diameters for the holes. Starting at 0.8 mm you can get a TiAlN coated carbide burr endmill (search for “titanium burrs mill PCB 0.8” in eBay). For anything lower than 0.8 mm 0.5 mm (which is big in PCB units), you have to resort to V-Shaped engraving mills. V-Shaped mills vary the cut width the amount you plunge into the copper clad. So the cut is wider as you increase the depth of cut (the width increasing with the tangent of the angle of the V-Shape). You may be tempted to go for low angles (10 degrees) so as to reduce the variability of cutting width as a function of the cutting depth, but this tools are much more brittle, age worse, produce a less clean cut and are prone to break. Then you may want to go to a 90 degrees one to avoid all that, so a small variation in cut of depth (maybe because your PCB flexed up a little in the middle?) may make a track much thinner than expected. As always there is a compromise, which for me is 60 degrees.


2. PCB engineered mills (around 20 Euros per 1 mill): There are products specially designed for PCB milling which age much slower and produce much more clean cuts and consistent results according to extensive Googling. One if this: PreciseBit (US), another is this vhf (Germany). In the US one you can see that they tell you which exact Depth of Cut you should use, which you will realise that is not sufficient to totally cut the copper in a single pass (so you will have to pass several times at increasingly “Depth of Cut” amounts until you cover the copper layer)


Typical TiAlN coated carbide burr endmill from China: 

12_burr.jpg 

There are 0.5 mm ones if you search in eBay for “A box 10pcs Carbide End Mill Engraving Bits for CNC PCB Rotary Burrs 0.5mm”, and they work great (though they are not TiAlN coated). 

Typical 0.2 mm 60 degrees V-Shaped engraving mills from China: 

12.jpg 

I have got myself a lot of China tools and imported the US profi tool (which I did not use yet). My approach is first to try to find my way with the China tools, so that I can get a feeling of the limits of the tools and problems associated to PCB manufacturing without having to care about how many mills I broke due to collisions, software bugs, wrongly calculated manufacturing parameters…, and then try the high-end mills (and hopefully enjoy the extra quality and aging). I can simply break 10 China tools for the price of a profi tool… and believe me, you will break a lot of them just with collisions while jogging. 

It is nice to “play” with a simulator like this one to see how the different parameters affect cutting force, deflection and feed rates: FSWizard. The guy who did it also has applications for Android and IPhone for those interested. 

3. Feed rate experiments


You have to get to know your tools. This is even more true for those China tools that come without any indication whatsoever of which manufacturing parameters you should use. For those, testing is the only option. I have done this simple test in Heekscad, which tries a mill at 15k rpms at feedrates from 50 to 400 mm/min at depths of cuts of 0.051, 0.075 and 0.1 mm. 

 

Each vertical zig-zag, has different parameters, from left to right: 

1. Feedrate 50 mm/min, 15k rpms, DoC=-0.051 mm


2. Feedrate 100 mm/min, 15k rpms, DoC=-0.051 mm


3. Feedrate 150 mm/min, 15k rpms, DoC=-0.051 mm


4. Feedrate 200 mm/min, 15k rpms, DoC=-0.051 mm


5. Feedrate 250 mm/min, 15k rpms, DoC=-0.051 mm


6. Feedrate 300 mm/min, 15k rpms, DoC=-0.051 mm


7. Feedrate 350 mm/min, 15k rpms, DoC=-0.051 mm


8. Feedrate 400 mm/min, 15k rpms, DoC=-0.051 mm


9. Feedrate 50 mm/min, 15k rpms, DoC=-0.075 mm


10. Feedrate 100 mm/min, 15k rpms, DoC=-0.075 mm


11. Feedrate 150 mm/min, 15k rpms, DoC=-0.075 mm


12. Feedrate 200 mm/min, 15k rpms, DoC=-0.075 mm


13. Feedrate 100 mm/min, 15k rpms, DoC=-0.1 mm


14. Feedrate 200 mm/min, 15k rpms, DoC=-0.1 mm


15. Feedrate 300 mm/min, 15k rpms, DoC=-0.1 mm


The gcode of the test and the heekscad source is here: 

feedrate_trial.gcode.zip 

feedrate_trial.heeks.zip 

I have run this test for a 0.8 mm China burrs TiAlN mill and for a 0.2 mm 60 degrees V-shape. 

These are the results for the 0.2 mm 60 degrees V-Shape blade. The first picture shows (left the last track made at 0.51 mm DoC, center the first at 0.075 mm (50 mm/m) and the second at 0.075 (100 mm/m)). The scale superimposed is in tenths of millimeter per division (0.1 mm between lines). The second picture is a zoom of the center line. 

2015-04-18-192722.jpg 

2015-04-18-192849.jpg 

The information I extracted from these tests is that I can go with the V mill up to 300 mm/m at 15k even at -0.075 and -0.1 mm DoC with similar cutting results, but due to the geometry of the tool and the PCB copper thickness -0.051 is not enough to cut out the copper. The cut width is around 0.2-0.3 mm as expected from a simple calculation ( 0,2 mm +2*0,1 mm*tan(60/360)=0.23 mm). The cuts are reasonably clean for this kind of tool. 

These are the results for the 0.8 mm burr mill: 

All the cuts were similar, so I can also go up to 300 mm/m up to 0.1 mm DoC with this mill. The cut is however beautiful, much more clean that the V-mill. 

2015-04-18-214921.jpg 

A zoomed in shows that the cut is around 0.75 mm consistently, no matter the DoC (it is a straight endmill after all, not an V shaped one), but even at -0.51 cuts out all the material. The lines at different rates and speed are just identical, not only to the naked eye, but also to the microscope. 

2015-04-18-214813.jpg 

I liked this extra picture. Because I am cheap (or cost-conscious), I reused the same area of the copper clad for both tests, so here you can see the 0.8 mm track (of the burrs mill) intersecting a 0.3 mm track (of the V shaped mill). 

2015-04-18-215105.jpg 

I did tests with 0.1 mm 10 degrees V-mills and they were awful by comparison. 

II. Designing your PCB



1. Designing with KiCAD


KiCAD is the rising start of true opensource EDA software. This does not pretend to be a KiCAD tutorial and even less a electronic design course. However it deals with some of the details that you have to now to produce a design that is suitable for being milled in a FABtotum. This does not mean that other ways are not possible. It is just a way known to work with the current (Q1 2015) KiCAD release. 

1.1. DRC rules


This simplifies your life by forcing you to define your track widths and more importantly the separations between tracks and other elements. This is very important because it defines which tool (endmill) you will need to use to manufacture the PCB. No surprises, the higher the distance between tracks (and other elements), the bigger the tool you can use, the lower amount of problems of breaking tools, tool deflection, tracks thinner than designed you will have. So DRC rules are your friend. When filling in the dialog, this idea might be handy: 

The smaller end-mill (flat bottom) that I have managed to use without a substantial tool deflection with extraordinary cutting results and useful end-result is an TiAN coated 0.8 mm diameter mill. This provided a beautiful finishing, leaving enough space so that solder or solder past would not jump and bridge your connections. Of course, this may be too big of a distance for many designs. In general, use the bigger clearance that your designs allows you to have (it would be nice to have clearance separated track-to-track from pad-to-track, but KiCAD does not support such a feature). Such an approach maximizes the PCB area where no problems will exist in the final prototype and minimize the areas where problems may exist, meaning that you can concentrate more in testing that no jumpers happen in that area. It is perfectly ok to have different areas of a PCB with different clearances, during manufacturing, you may use two different tools one after the other to remove everything you can with the bigger tool and leave that areas requiring more removal to other tools. 

I have read about 0.4 mm endmills that work fine. I did not tried them yet. I have tried 0.2 mm China endmills that actually seem more adapted to boring than to milling. The deflection on these tools is outrageous and the tension of displacement, even at low feedrates, may cause tool permanent deformation and significant deviations between the path really milled and that that was intended. 

There are more professional mills for cutting that area c onical shaped (tapered tips). I have one of 0.20 mm waiting to be used. The problem that I already see is that they require several passes at different depths (the depth of cut, DoC, is tool small to avoid forcing the tool). FlatCAM currently does not support passes at different depths (Heekscad does). 

But that is enough information, as this section is about setting your DRC rules. A summary is: “Bigger clearances provide better results and less trouble during manufacturing”. 

1.2. Setting a reference point for manufacturing


It is convenient to set the reference point for manufacturing directly in KiCAD. This point is the 0,0 in absolute coordinates. Once set, you will see a vertical and horizontal crossing lines in the PCB view like the ones in the figure. 

 

In order to insert auxiliary axis you use this tool from the right toolbar . 

If you are going to use the PCBMill plugin allowing autoleveling of the gcode, this origin must be on the bottom left of your manufacturing area, so that all the elements are located at the right/top of this point (all elements have positive coordinates with respect to this point). 

1.3. Creating the Gerber files for manufacturing


The Gerber files generated by KiCAD (and with basic settings any other EDA) is seen as manufactured from top. If your PCB is a single-sided PCB with tracks on the bottom layer, then you need to flip/mirror your exported layer. Heekscad allows you to mirror the imported gerber, but FlatCAM (unless you are doing a two sided PCB) does not. The plugin PCBMill currently does not allow for mirroring directly from the plugin. This means that if will use FlatCAM in a single sided PCB with the tracks on the bottom layer of the PCB, then you have to mirror the layer first. The easiest way I found to do this, is directly from KiCAD. Just select everything in PCBnew, right click and select “Flip block”. You will realise that your tracks routed on the bottom layer have been transferred to the top layer and the image is mirrored. Of course that does not apply in the case that you are doing a single sided PCB with the tracks on the top layer (and if thru-hole, the components mounted on the bottom layer). I do not cover double sided PCBs here since PCBMill is currently not able to process them directly (though it should be possible to do it using the FlatCAM double sided PCB feature and tricking PCBMill to think everything should be done from top), but in that case you do not have to mirror anything at this point. 

The result (mirrored or not) is exported using the “Plot” function in the file menu. Generally, you want to export in Gerber format as most the software to process the output of EDA software support this format. It may be convenient, for example for the PCB cut layer to also export in DXF format. KiCAD's DXF format is not fully compatible with other DXF (there is 2.54 factor conversion that as your intuition tells you is about converting from inches to mm or vice versa). A trick is to load KiCAD's DXF in LibreCAD and save it as DXF again in LibreCAD (saving as 2007 DXF works for me). This resulting DXF is properly read by other software, like Heekscad. These are the options I use to export the files (make sure to activate the auxiliary axis): 

 

 

You should have now a Gbr file for every layer to be manufactured. 

III. From Gerber/DXF to Gcode



1. Why do I need to do this?


The Gerber file shows the tracks. However, in order to manufacture a PCB with our FABtotum by milling, we need actually the contrary, where do we have to remove material. This is called insulation milling and a piece of software is needed to calculate where it should be milled so that the tracks remain after the milling process. 

2. FlatCAM



2.1. The software


FlatCAM is one of the multiple alternatives to convert a Gerber file into Gcode usable with the FABtotum. You can find the manual for FlatCAM here. 

FlatCAM is a very nice python tool with a graphical interface. You import your Gerber and Excellon files directly into it and it allows you to generate, a (plurality of) insulation pass(es) with the same or different tools, and generate a Gcode file for each, and one or more drill operations with the same or different tools (you can group similar drill diameter in a single file or have all job in a different file). From this you can generate a CNC job for each. 

The main limitation of the current version, is that it does not support passes at different depths, so you are limited to tools supporting a Depth of Cut at least as big as the thickness of the copper layer in your copper clad (PCB). Of course you can still generate different jobs at different depths and then execute them in the right order, but it is not automated. 

The best is that you get to know the software and your tool. I am just going to explain what I have used to give you an idea of the order of magnitude of the CNC values I use (that are not necessarily good ones). But as said, every tool has it values and your tool is different from my tool. 

1. I generated tracks of 0.8 mm (for an 0.8 mm endmill with TiAN coating from China), and a different job for a V-bit of 10º 0.1 mm. I ran both at @ 7500 rpm 75 mm/m. The 0.8 mm mill did an incredible job with a clear cut. The V-bit not so much, I will have to try with other configuration. I will also switch to 60º V-bits, because with autoleveling 60º is ok and I can go much faster, with less tool breaking occurrence. I milled 0.075 mm in the Z direction. 

2. I generated a PCB cutout with Heekscad, because even if you can do it with FlatCAM, cutting the PCB generally needs several passes at different depth of cuts, which FlatCAM does not support. I used a 2.4 mm endmill, final depth 1.6 mm, step 0.4 mm @ 10000 rpm, horizontal 190 mm/m, vertical 80 mm/m. 

3. The holes are done with typical china carbide mill that is non-flat @ 7500 rpm 30 mm/m, drilling to Z=-1.7 mm. This was ok, except for the 3 mm mill, for which the vertical feed rate was too much, I will use 15 mm/m next time. 

Once you create all your gcode you have to post-process it so that the FAB and PCBMill plugin can understand it and properly use it. If you do not post-process the result it will go at the default feedrate and probably the motor will not start. I postprocess the files using the shell script: 

#!/bin/bash  

# $1 file_in  

# $2 rpms  

feed_rapids='F2000'  

feed_tool=`cat $1 | grep '^F'`  

cat $1 | sed “/^G00/ s/$/ $feed_rapids/” | sed “/^G01/ s/$/ $feed_tool/” | sed “/^G21/ d” | sed “/^G94/ d” | sed “/^F/ d” | sed “/^G04 P1/ d” | sed “s/M03/M03 S$2\nG4 S3/g” | sed “s/M05/G4 S5\nM05/g” | sed 's|Y| Y|g' | sed 's|Z| Z|g' | sed -e '/^$/ d' | sed 's/G00/G0/g' | sed 's/G01/G1/g'> `echo $1 | sed 's/.gcode/_postprocessed.gcode/g'`  

As you can see the script takes the gcode file generated by FlatCAM and the spindle RPM and reformats the default output to generate a file with the same name but ending in _processed.gcode instead of .gcode as the original. 

I have been pointed out that this script won't work when copied and pasted. You can download the file from Github here. 

2.2. Application Defaults


It is worth setting some application defaults and saving them (in File Menu, save defaults), so that we do not have to change a lot of values during each step. All values are in mm, you have to configure FlatCAM to work in mm. If you are used to the imperial units I am not certain that you can put everything in mills and then generate gcode in mm, and Marlin requires mm (afaik). This are my defaults: 

 

 

You can copy the application defaults to your project by using Options → transfer options. 

2.3. A practical example


So I decided to make a practical example. These are my Gerbers generated by KiCAD and I have already mirrored the PCB so that I manufacture directly this file and it will be the bottom side of the PCB (see note in the KiCAD section), just in case you want to practice with these files: 

fabdialindicatorhead.zip 

Nevermind the name. Originally was going to be a Dial Indicator Head, but it is an (untested) proto head instead. 

I load into FlatCAM only the files FABDialIndicatorHead-F_Cu.gbr and FABDialIndicatorHead.drl, that are my Top copper tracks (that will go in the bottom, but is mirrored so is top) and the drills file (this one is called Excellon file). I did not load neither the silkscreen, nor the bottom (that only has the pads of the thru-holes), nor the cut of the board (because I process that one with Heekscad, as it is simpler for me), My view looks like this: 

 

To process the Top layer, just double click in the name to create an insulation job. This dialog appears: 

 

So the first operation is an insulation milling around the tracks with a tool generating 0.3 mm wide cut (if you read the section above, a 0.2 mm 60 degrees V-mill that cuts around 0.2-0.3 mm and I want to be on the safe side with the width of the tracks). This is how the insulation path looks like after having pressed “Generate Geometry”: 

 

So the red line is where the mill will cut. This generates two path objects in the tree (one for each of the two passes), if we double click on them, we can generate a CNC job for them. This dialog appears: 

 

If we click generate for both operations, this is the result: 

 

The blue is the copper scheduled to go away and two new objects appear, the CNC jobs. Double clicking in each of them allows to produce the gcode. This dialog appears: 

 

Clicking on “Export G-Code” allows you to save the Gcode file for this CNC Job. Do it for each CNC Job. 

Now if we look close to the FABtotum pogo connector, we will see that there is still some copper between pins: 

 

This may pose problems to soldering, so we want to make it go. A trick is to use another pass with the V-mill, but generating an insulation geometry for a 0.5 mm drill 0.4 mm drill (that we do not have) (the change from 0.5 to 0.4 is because otherwise it won't process the connector with the thicker lines, it took a lot to figure this out during manufacturing), and milling that path with the V-mill. This is the result: 

 

Much better now. 

Now, because I like much more the finishing of the 0.8 mm burr endmill, I am going to do a couple of passes with this endmill (for the places where it fits). The result is this: 

 

Now if I double click in the Drill file (Excellon file) the following dialog appears: 

 

This dialog allows you to select different drills to group them to CNC jobs. For example drill 3 and 2 (and also 4) are around 0.8 mm and I am selecting all them and generating a single cnc job of 0.8 mm. I then repeat for 1 mm and 3 mm (for this I go down to 2 mm at 10 mm/m as the drill has an angle and 1.8 mm is not enough to drill a 3 mm hole up to the bottom of the PCB, I also found 30 mm/m to be too much for 3 mm holes), to end up to this result: 

 

Now this Gcode will be post-processed by the shell script to generate Marlin compatible G-Code: 

#!/bin/bash 

# $1 file_in 
# $3 rpm 
feed_rapids='F10000' 
feed_tool=`cat $1 | grep '^F'` 

cat $1 | sed “/^G00/ s/$/ $feed_rapids/” | sed “/^G01/ s/$/ $feed_tool/” | sed “/^G21/ d” | sed “/^G94/ d” | sed “/^F/ d” | sed “/^G04 P1/ d” | sed “s/M03/M03 S$2\nG4 S3/g” | sed “s/M05/G4 S5\nM05/g” | sed 's|Y| Y|g' | sed 's|Z| Z|g' | sed -e '/^$/ d' | sed 's/G00/G0/g' | sed 's/G01/G1/g' > `echo $1 | sed 's/.gcode/_postprocessed.gcode/g'` 

I do it like this: 

for i in `ls *.gcode`; do ./post_process_2.sh $i 15000;done 

Thispostprocessed files are loaded into the FABtotum for manufacturing. 

3. Heekscad


An alternative to FlatCAM is to use Heekscad. It directly takes the Gerber and asks you if you want to normal or mirrored image and if you want the actual tracks (for printing with conductive ink) or insulation milling. Then you have to define the tools to use and generate the profile or pocketing operation from there. 

The result is also gcode that is not usable with the FABtotum. But I have written a post processor for Heekscad that you can download from here. This is much more integrated that in the FlatCAM case, you just install it once and then all the gcode that is generated is compatible with the FAB. 

IV. Manufacturing the Gcode with the FABtotum



1. Manufacturing using FAB-UI's substractive manufacturing


This is totally possible. The only problem that you will encounter is that after each gcode file you mill, you will have to execute the wizard again and set the zero again (with the lack of precision that you may introduce). Additionally you do not have autoleveling of the gcode. This means that the mill enters into the PCB more in those parts where the bed is higher and less in those parts that the bed is lower. If you increase the depth of milling to compensate for it you may enter into different problems: 

1. Tool deflection increases with the depth of cut, so there is a higher chance of breaking the tool and for thin endmils the forces may cause that you do not mill where you want because the tool bends while the XY carriage moves. 

2. If you use V-shaped bits, the more you enter into the PCB the wider the cut area is, so either your tracks will be thinner than designed, or if you compensated it in FlatCAM/Heekscad, your tool may no longer enter that clearance because now it is too wide. It will also tend you to use lower degrees V-shaped bits (because at a lower angle the width increases slower as the depth increases) which break easier and endure less. 

2. Manufacturing using PCBMill FAB-UI plugin


The plugin in its alpha version (current state) is very hairy. I have some bugs to correct and functionality to add but it is half-usable. Currently it only supports manufacturing from top side (so it won't flip the circuitry for you, you have to do it in KiCAD, Heekscad, …). It features all the milling operations in a loop having a single homing process to calibrate all of them and lets you change the tool between files. It makes use of a electrical continuity probe and a special firmware to auto-zero the tool and (current versions of FABlin do not require any special firmware) to allow to perform gcode autoleveling (with the algorithm used in bCNC that I borrowed here). 

2.1. Overview


To use PCBMill you have first to create an object using the Object Manager (like in any other print/mill). You put all the gcode files inside this object. Then go to the plugin and select the object, you will see all the files and will allow you to select them and set the manufacturing order (just click on the name of the file and it assigns the next manufacturing number to it). I looks like this: 

 

When you click next, it allows you to start the zeroing procedure, the machine homes and uses the Z-Probe (yes, the stock Z-Probe) to home all axis. Then asks you to jog to the position that will be the ZERO position of all your files (no, currently it does not support a different zero position and for everything to work properly the zero positionhastobe the closest position to the left-front corner of the manufacturing area). You will see this screen: 

 

This screen allows you to use a PS3 sixaxis to go to the zero position (thank Tohara for it, I just embedded his code). Just remember to push the circle when you are done, so that if you move the joystick accidentally during the milling nothing happens. Alternatively you can enter the coordinates (absolute coordinates) where you want your zero to be and click go. Alternatively you can jog with the arrows until you are where you want to be. Grabbing the head with your hand and moving it where you want to be is NOT an option, as the plugin will not know where you are because it was not the steppers that moved it there. 

One nice feature is that, if you did the probing (next step), next time you run the plugin the edit boxes will show you the coordinates of the last time you zeroed. So if for any reason you start today and have to continue later, you can re-run the plugin and just hit “Go” in this screen to go to the ZERO point you considered last time (within the accuracy that a homing procedure inbetween provides). With this plugin you do notneed to push or click anything to actually “zero” the machine (actually you can not, because I removed the functionality from the JOG pad in the screen and the PS3 control), the plugin does it for you. 

Beforeclicking next you need to have a electric conductivity probe connected to your machine like described in here. Without this probe you will  crash your tool against the bed. The tool will go down slowly until contact is made with the bed, and it will set this point as reference for the probing process. Now you can click next and you will see this: The screen informs you of the dimensions as calculated from the G-Code (if for any reason these numbers do not make sense, do not continue, it may be that the g-code analyzer was not recognising your g-code and the probing won't work. This happens at least when the G-code does not leave whitespaces between the operation and coordinates or parameters). The default values are calculated to have a probed point every 0.5 mm, this was a recommendation I found, but feel free to use any other configuration (probing will take a while, like 10 minutes for a 60×40 cm circuit with this configuration). In fact, lately I am having good results just with 1 square (4 points). The plugin also also tells you the point you selected as zero and the point the plugin detected using the electrical conductivity probe. Now, if you did not realise it yet, credit for most of the probing goes to procrash, I just took his code, integrated it and made it use the electrical conductivity probe. There might be some goodies if you use IE that I do not know about. I know there is some code that makes nothing useful in my Firefox. For probing, it makes sense to use a mill that is rigid and resistant (not a thin one). I use a 3 mm cheap boring mill for this. 

When you are ready click “start probing”. You realised it did not start, yes you are right, hit the button again and it will start (I have to look for the cause). It is worth mentioning that there is a bug in the representation, so it may be that the grid appears off the bed picture. So far it never tried to probe out of it (though I had one case where half of it was out). It is just another bug to be fixed. 

When it is finished, you are ready to press next and go to the next stage, that looks like this (well the next alpha has one extra box to enter a tool offset, this offset is added to the depth in the gcode and it takes negative values, so -0.05 will make the FAB think that where it touches is actually Z0.05 position, so it will plunge an extra 0.05 mm making the cut deeper. Use it with care as you might eat your clearance, I use 2mm and have tons of colissions. This is thought to allow you to plunge a little bit deeper in a second execution avoiding you to have to regenerate the gcode): 

 

This shows you the name of the file that is going to be milled (it helps to indicate in the name the tool to be used, so that now you know what you have to mount for each file). You will see one of these screens for each file that you have to manufacture (you see one, you manufacture it, you see the next one,…). 

The idea is that now you remove the head and mount the tool to be used (yes it will complain that you removed the head, you do not care, you mount your tool and remount the head and click ok in your browser). Try not to move the head-holder while changing the tool. I am planing to have something to keep the steppers energized to help with this task. If you moved it, then it is better you re-do the plug-in again with the remaining files and use the ability to remember the last zero to use “the same” zero position. 

When you have your tool, you click “click here if you are ready”. The (new) tool touches the bed and the zero is readjusted to this position (this adapts for tools of different lengths). Then your gcode file is leveled using the probed data via the wonderful code from the bCNC project (yes that guy rocks a lot, he writes wonderful code and it was really painless to integrate his code into this plugin. If you by accident read this: you rock), and this leveled gcode file is then manufactured as any other subtractive file…. it goes back to the zero point, leaves you some space to change the new tool, and you will get the screen for the next file in the batch… 

One tip here. There is bug that sometimes the next file will not appear. It seems to be related with having the FAB-UI in the browser active. FAB-UI in its current design requires that you do not close FAB-UI until you are finished (many features rely on javascript instead of php). However, currently it is possible to press “next” if the page does not appear. Sometimes the next file appears just by doing it. Some other times after having pressed next, you have to click in “step 4” in the top bar. Then you can continue manufacturing… 

2.3. Do I need auto-leveling for milling PCBs?


Well, you can certainly do a lot of things in life with bad tools and good tools. While a skilled operator may achieve better results with worse, it is generally preferred to have good tools. Auto-leveling helps you avoid to have to fine level your bed before manufacturing and generally achieves a better result than what can be expected from bed leveled by an operator. 

The typical correction for a PCB in a non-calibrated bed looks like this: 

 

The bottom are the X,Y axes and the vertical (and color) is the perceived tool length at those X,Y coordinates. A perfectly calibrated bed graph would be a horizontal plane, where no matter the X,Y coordinates, the perceived tool length is the same. As you can see I have 1 mm of difference between the two further apart corners. 

However, depending on the PCB and specially if the attachment means exert tangential forces on the PCB you can get surfaces like this: 

 

You want to avoid the tangential forces, as they may introduce other sources of inaccuracies, but with autolevel you can mill a decent PCB even on that surface. 

2.3. Status


It is functional, but it has bugs that need to be corrected: 

1. The autolevel via probing mostly works well, but sometimes it is way off. I need to investigate further why sometimes a value is off. Maybe I need to change the way the probing is done (probe more times… at different feedrates…). Fortunately it does not happen often. 

2. The manufacturing feeds only work for the first file. I think I need to reset some values after each file is manufactured. A bug to be fixed. 

3. The batch list sometimes stops in the middle (I was actually doing a PCB with this tutorial). It manufactured 5 files (i.e. the tracks) and left the 3 files of holes of different diameters. Luckily it now remember things (yep here is like alpha0.2), so I only had to restart, it remembered by zero point and my probing, and I only had to resume it where it was left. 

4. Probably more bugs (like representation of grid in probing step). If you find one put it here (and notify me!!). 

The only one that worries me is the first one, as it the one that limits my PCB manufacturing. I have narrowed it down to two factors: 

A. Rarely the probe produces bad results (it plunges more in one point, specially with thin mills) needs further investigation (probing multiple times may help here). 

B. PCB flexes (is not in contact with the bed in all the surface). The electrical conductivity probe is not a force sensor, it stops upon conductivity, so it generally (except rarely as in A) stops without exercising any force on the PCB. If the PCB is not in contact with the bed, then this is higher than wanted. Why? because while milling the mill does exert a force and the PCB prefers to move down (to the gap) than to allow copper to be removed. This can be solved by: 

Improving the fixture of PCB to the bed. 
 Vacuum table, but it is overcomplicated for a DIY IMO 
 A force sensor, but it is not as easy as the electrical conductivity probe. 
 increasing the final depth of cut (inserts a limit to the narrowness of the track that can be made with a given tool), though easy solution. 
 SW help: Allow to insert an offset to a job (remember the offset) to do a second pass slightly deeper (without having to go back to the CAM software and modify the depth). This could be done by tweaking the tool length detected by zeroing via electrical conductivity before autoleveling takes place. In my mind it can also be that the camera is used to detect the areas of PCB where copper was not properly cut, map them to the probing, modify the probing and do a second pass (only in those areas)… but that sounds almost as overkilling as learning bacteria to selectively eat copper. 

2.4. Installing PCBMill


PCBMill requires a customized firmware in order to support the electrical conductivity probe. I have made a pull request so that the code goes into FABlin, but it has not been merged yet. Therefore I provide a firmware that is equivalent to 1.007 with the electrical conductivity probe code. The modified firmware should be generally as safe as the unmodified one, as the sections of code that differ are only activated when the electrical conductivity probe is active. I have been running this firmware quite a long time, including during printing and I have had no problem. However, be advised of that “the software is as is” and I provide no warranty whatsoever disclaimer. Use it at your own risk. 

Install method one: The easy way 

Yes, I am aware that it does not look logic, but you wanted easy… 

1. Download the plugin from here: pcbmill.zip


2. Install the plugin


3. Remove the plugin


4. Goes to http://fabtotum/recovery/flash.php and flash the “local firmware” (i.e. click on the button “Flash local”)


5. Install the plugin again


Install method two 

1. Download the firmware from here: marlin.cpp.hex.zip


2. Install the firmware following the instructions in here:


3. Download the plugin from here: pcbmill.zip


Install method three: I refuse to install binaries from the Internet 

1. Download the code (via zip) or git clone the branch G38M746 of this repository: https://github.com/imarin2/FABlin/tree/G38M746


2. Compile the code, upload the binaries and flash the FABtotum as described in here


3. Download the plugin from here: pcbmill.zip or get the code from the repository (you may want to follow the instructions in the README): https://github.com/imarin2/PCBMill/tree/basic_mill


2.5. Checking firmware installation


Got to the jog module and in the MDI window execute: M746 

If the firmware supports PCBMill it will reply as follows: 

M746: SECURE_SW Z PROBE ENABLED: FALSE ok 

If you do not see this, do not execute the plugin or your bed will crash against your head. 

2.6. PCB Examples


This is by far not the best example. I have used this PCB for testing/debugging the plugin (it is the result of the FlatCAM example above). Each file of the batch was repeated several times at different depths to check different things, with homings inbetween, so positioning errors accumulated and led to some pads having been “eaten by the tool”. However, the end result is functional!! I will try to post a better one next time I mill a PCB (or if you use it and get a nice one, just put it here!!),,, 

ASCII User comments 

This is the other side, so that you can make an idea of how it looks… 

ASCII User comments 

This other example is with the new “energizing the steppers on tool change” option. Look at the drills, they are in the middle of the pads!! 

ASCII User comments 

And this is how a FABtotum protohead having this PCB looks like: 

ASCII User comments 

This is mounted on a PLA printed PCB-Holder, like this: 

 

So, yes, my aim is to use the FABtotum to make heads for the FABtotum. I will be releasing a “Protohead Kit” when everything is tested, comprising: 

1. Several head cases that mechanically fit in the FABtotum's carriage and have a template of alignment holes for the PCB: FreeCAD original files, STL and gcode so that you can directly print them in PLA. 

2. A KiCAD template, so that you can design a PCB having the alignment holes that fit the case, so that when you mount the PCB on the PLA plastic, you have a good electrical contact. 

3. A simple Arduino mini pro firmware, so that if you use an Arduino mini pro in your PCB, it identifies to the FABtotum via I2C. 

This should enable us to develop heads much more quickly. 

V. Advanced PCB Manufacturing Examples



1. Introduction


It always marvels me when something is said to be “advanced”, specially when it predates my own existence. So I would like to define what “advanced” means in this context. It is a collection of Examples, including tips, convering one or more aspects of the overall manufacturing process (preparation, design of a PCB, gcode generation tool chains, or FABUI manufacturing) that is simply more advanced that what is presented in sections I-IV. Sections I-IV cover quite a lot of aspects of the manufacturing from the perspective of a newcomer to the milling world and it is my humble opinion that it has quite a didactic value. However the possibilities that further developement of the tools and knowledge open are certainly worth sharing them separately. Feel free dear reader to include your own example below if you want to share your own experience and contribute with your own tips. 

2. Example 1



2.1. Preparation / tools


In this experiment I have settled for reducing the amount of tools used. I use: 

1. A 0.5 mm carbide burrs endmill (insulation milling)


2. A 1 mm drilling mill (drilling thru-holes)


3. A 2.5 mm drilling mill (very inappropriate but at hand tool to execute the cut-out of the edge of the PCB)


All three were sourced from China via eBay. 

2.2. PCB design


I am a KiCAD user. No change there. From my previous tests I realised that: 

1. Insulation milling actually leaves a lot of copper islands (no need to be Sherlock Holmes to realise that).


2. Clearance settings during the design phase can actually help a lot to get a better manufacturing result.


So I did my design as to: 

1. Use copper fill areas together with copper exclusion zones so as to actually maximize the use of the copper that is not going to be milled away.


2. Enforce clearances higher than 0.5 mm as much as possible as this is my tool size for this example.


This is my PCB design (yes it is a mini PCB intended for a head design, I just dropped the pogos of the milling motor): 

 

As you can see I designed the PCB to have an “as big as possible” GND copper plane. I wanted this plane to have a clearance larger than 0.5 mm (0.55 mm at the end) and to meet the cutout (edge) of the PCB. I wanted to prevent the copper from entering the area where the pogos are to be soldered (to prevent unwanted shorts in this area and problems with solder paste jumping to where it should not). 

Most PCB SW have different ways to achieve this. In KiCAD I set an exclusion zone (keep out area in KiCAD terminology) for the pogos with this configuration: 

 

So I just want to keep “copper pour” out of this area. Then I set two copper zones with different priority levels, so that a clearance of 0 mm is left with respect to the Edge, while a 0.55 mm clearance is enforced with respect to all the other elements. The priority just makes the 0 mm clearance to be enforced over the 0.55 mm clearance in the area of overlap of both copper zones. I put the configuration for the curious: 

 

 

The normal track clearance is enforced using NetClasses like this: 

 

As a sidenote, there is no track in this design in the “Default category”. 

One last tip: Designing the cutout in KiCAD is not nice, specially when you have already modeled it in another CAD and you have a model of the size and shape that matches your final product. I had such a model done in FreeCAD, so I exported the model as DXF in FreeCAD and imported it in KiCAD. As the pogo pins require quite an exquisite positioning, I also exported in the DXF the carriage contacts, which I set in a user layer just to help me place the pogo pin layout and double check the component footprint. 

2.3. From Gerber/DXF to Gcode



2.3.1. Heekscad: Edge cutout


Flatcam does not allow for multipass when cutting the edge, so I use Heekscad for this (remember to use the FABtotum postprocessor as indicated in section III). I export the Edge layer in KiCAD as DXF. I open it with LibreCAD, remove any unnecesary double profile and separate the cutout in different files, each with a closed contour (this PCB has 2 slots for positioning that must be milled away) and save it in the 2007 format (to fix a problem with Imperial-metric system in the KiCAD DXF). This 3 DXF files can be imported into Heekscad and each of them be assigned a profile operation (the cutout is by the outside and the slots by the inside). If the profile appears as “bad” just click in “reorder”. I ended up with this: 

 

Each profile having these parameters (the slots “inside” instead of “outside” and without the “offset extra”): 

 

Probably I should use a lower vertical and horizontal feedrates, specially for the slots. 

Tip:I do not use tags. As I do a multi-depth pass, at some point the PCB comes out fine. I have to file the etches, but I am fine with it. 

2.3.2. FlatCAM


The bottom layer and drills, I exported them in gerber/excellon format (do not forget to flip the PCB as suggested in Section II). 

I have tested different configurations (I must have done linke 5 or 6 of this PCB). The relevant test are: 

1. Test 1: tool dia 0.5 mm - 3 insulation milling passes with 0.15 (ratio, not mm) overlap. CNC job as 0.5 mm mill, -0.075 mm cut z, travel z: 1mm, feedrate: 400 mm/m. I generated 3 gcode files like explained in section III. 

2. Test 2: same configuration as in Test 1, but I did more post-processing on the final result (apart from the post_process.sh script I applied two other scripts to make a finishing pass for each gcode file and combine the 3 gcode files using the same tool together, more below). 

3. Test 3: Instead of doing insulation milling, I used the “non-copper regions” with 0.0 mm boundary margin to identify the non-copper regions and then generated a “paint area” with tool diameter 0.5mm, overlap 0.5, margin 0 mm, method: standard for each of the non-copper regions. 

Rationale: 

Test 1 is just what was presented in section III or the “old” result (just there for comparison). 

Test 2 tries to improve finishing quality (by introducing an extra finishing pass at a deeper depth, just 0.025 deeper, so at -0.1 mm overall depth), reduce any source of “tool zeroing offset error” when using the same tool (one gcode file for all the passes), and improve the speed as there are no stops when using the same tool and honestly I do not have to be so attentive to start the next pass of the same tool. 

Test 3 tries to improve the aesthetic issue of leaving small islands (even if sufficiently appart as not to become a functional problem) and test the “painting option” of FlatCAM. It generates a cnc job per closed area to be painted and it uses the same post-processing as in Test 2 (finishing pass+single gcode file per tool). It is worth mentioning that I incremented overlap from 0.15 to 0.5 to decrease ocasional scraps still in Test 2 (so theoretically Test 2 with this increased overlap would have achieved this goal). 

Results: 

Test 2 is a real improvement over Test 1. The finishing pass removes so extra copper scrap that withstood the first pass and there is not any occasional tool misalignment, meaning that you can see all the cleared area is at the same depth (so the clear areas are uniform). 

Test 3 is beautiful in comparison with Test 2 and not that much more area to mill away for this specific example (that uses an as large as possible GND plane). You can judge the difference yourself. This is test 2 vs test 3: 


2015-08-22-215041.jpg  2015-08-22-215145.jpg  
2015-08-22-215228.jpg  2015-08-22-215243.jpg  

Scripts  

All the shell scripts are available from GitHub. 

The files MUSTbe first processed by the post_process.sh script. 

addfinishingpass.sh 

A very simple script that adds an additiona pass with a higher depth. The depth can be controlled by the script:


usage:
 addfinishingpass.sh Protohead_v4_FAB_rc1-F_Cu.gbr_iso1_cnc_2_0.5mm_postprocessed.gcode 0.025

 The number is the “extra depth” of the finishing pass. So if your file is coded to mill away 0.075 mm,
 it will do a first pass with that amount and a second finishing pass with 0.1 mm (0.075+0.025). 

mergepostprocessedfiles.sh 

It merges several gcode files (to be executed with the same tool) into a single one.

 mergepostprocessedfiles.sh Protohead_v4_FAB_rc1-F_Cu.gbr_iso1_cnc_2_0.5mm_postprocessed_finishpath.gcode Protohead_v4_FAB_rc1-F_Cu.gbr_iso3_cnc_2_0.5mm_postprocessed_finishpath.gcode

 generates a Protohead_v4_FAB_rc1-F_Cu.gbr_iso1_cnc_2_0.5mm_postprocessed_finishpath_merged.gcode with both files executed in the given order. 

Tip: This mergepostprocessedfiles.sh script is born deprecated, because FlatCAM +8.0 already includes a tool to “join” geometry into a “combo” and then generate gcode for this combo. So the script is there, but I will use the “join geometry” in the “Edit” menu instead for this purpose. The of course, I will have to post-process the output and probably add a finishing pass using the other script. 

2.4. Manufacturing with FAB-UI PCBMill plugin


A quick note is that PCBMill has evolved in the meantime to improve accuracy. Now it probes several times each point during probing, so the “suggestion” of how many squares to probe is generally speaking excesive. In this tests (for this very small PCB) I have used a single square (4 points). 

Tip: Update your PCBMill (github.com/imarin2/PCBMill/tree/basic_mill). 

Tip: Consider using many less squares than suggested in PCBMill. Share your results. 

2.5. Gcode files


I have realised that many of you just want to make a quick test to see the results and then bother about the rest. Here you have some gcode files you can mill with the PCBMill plugin using tools similar to the ones described in 2.1:protohead_v4_fab_rc1.zip 

This zip contains 3 files. The manufacturing order is: 

1. gbr_noncopper_paint_cnc_1_postprocessed_finishpass_merged_merged_merged_merged_merged.gcode


2. Protohead_v4_FAB_rc1.drl_cnc_1mm_postprocessed.gcode


3. cutout.gcode


You have to use the 0.5 mm burrs endmill for 1, the 1mm drilling mill for 2 and a 2.5 mm drilling mill for 3. The feedrates and rpms are calculated for these tools and may not be acceptable for others. 
  
pcb_milling_workflow.txt · Last modified: 2015/09/10 13:16 by imarin