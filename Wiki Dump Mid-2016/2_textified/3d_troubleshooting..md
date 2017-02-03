
3d_troubleshooting
Table of Contents

    3D printing troubleshooting
            Not extruding / No filament coming out of the nozzle
            Filament not sticking on the plane
            Print not starting/ bed,extruder not heating
            Pillowing
            Elephant's foot
            Very visible lines on the bottom layer
            Under extrusion
            Walls not touching
            Grinding
            Scratches
            "Hairy" print
            Ringing

3D printing troubleshooting
Not extruding / No filament coming out of the nozzle

Description : Filament is not coming out from the nozzle (Hybrid Head)
Possible Causes:

    Cause A - The Feeder is not engaged (Valid only for versions older than July 2015).
    Note 1: The engaging/disengaging feeder has been changed, you can easily update it following this tutorial: Feeder Update.
    Note 2: The feeder will disengage itself after a print.
    First, extract the white PTFE Feeding tube from the head by heating the extruder at 210°C from the JOG Menu In the FABUI.
    From FABUI Go to Maintenance then select Feeder.
    Follow the instructions to locate and press the feeder mechanism. Be sure that the button inside and the back of the printing area is pushed with the right force.A “click” sound should come from the mechanism if fully engaged.

    engaged.jpg

    When the feeder is engaged go back to the JOG menu, press the E tab in the right hand side of the panel.Press the plus button and see if the filament is moving inside the tube, by watching the end that was just unplugged from the Head.

    Press the Plus botton in the JOG menu until the filament sticks out for 3cm from the PTFE feeding tube. If the filament is coming out, carefully reinsert it in the head. Be careful to not get the filament stuck on the sides of the head when pushing it down. this will bend the filament and block extrusion.When inserting the tube and the filament, the nozzle should be pouring some molten plastic.
    Once the tube is firmly locked in place, extrude another 10mm by pressing the Plus button to verfy the correct extrusion of material.
    Cause B - The nozzle is too close to the printing surface
    Increase the distance by pressing the Z+ button during the print or calibrate the Probe lenght (Maintenance → Probe Lenght Calibration)
    Cause C - The temperature is too low
    You could try to Increase the temperature a bit (5-10°C would help) during prints.
    Some filaments, especially with colorants, have higher melting point (180-230°C).
    Cause D - Excessive temperature
    If the temperature is too high, the filament will melt before reaching the nozzle, causing excessive friction.
    Be sure to keep the cooling fan on (M106 at the start of the gcode or “FAN always on” in slic3r)
    Cause E - The nozzle is jammed
    First, Verify that the PTFE tube in the back is correctly sticking out and is not caught inside the back of the unit.
    Remove the tube from the head, and with the Z in the middle of the height (bed Halfway), try to push some filament Manually in the head. can you push the filament and see it being extruded?
    If not the nozzle could be obstructed and requiring some cleaning or the filament is not getting all the way down in the nozzle (getting caugth in the sides of the head before entering the heating chamber).
    Try dipping some filament from the top by hand and then pulling it out for a few times (with the nozzle at 210°C) helps to clean it.
    Insert a small 0.3mm electric wire in the nozzle while at 210°C from below and make sure there are no obstructions.
    For see how to clean the nozzle follow this guide.

—-
Filament not sticking on the plane

Description : Filament is not sticking / drops are left on the bed (Hybrid Head)
Possible Causes:

    Cause A - The nozzle is too far from the bed
    -Verify that the 4 bed set-screws are almost completely screwed in (highest position possible minus 2 turns)
    -Run the Probe Length Calibration wizard from the maintenance menu
    -Run the Assisted Bed Leveling procedure from the maintenance menu
    -be sure that the PTFE tube is not getting stuck in the back of the unit.
    Cause B - Extruder or bed temperature is too low
    Increase the temperature of the bed and the extruder in the supported range and wait a few seconds:
    Extruder: Min 180°C, Don't surpass 210°C if you don't see any result.
    Bed: Min 55°C, Don't surpass 70°C if you don't see any result.
    Cause C - The bed doesn't have a sticky coating
    Look on this page how to make your bed sticky

—-
Print not starting/ bed,extruder not heating

Description: The 3D print process is not starting
Possible Causes :

    Cause A - the bed is not making contact with the power supply connector
    Verify that the temperature can be read from the JOG menu,
    Try set a temperature over 60°C and press “temperature” to see it grows.The Red LEDs on the Bed will turn on.
    If it does not raise the bed is not at the right height or it's not making contact.
    Verify that the unit is not locked (no error message or safety warning)
    Cause B - the machine is currently in SAFETY LOCK mode
    1. Check the temperature of the bed in the FABUIIt must not be 0°C. Push the bed from the right side towards the left side as to facilitate the contact. If The temperature is still zero remove the bed and check the contacts, if any of them is deformed try to put it in place with some pliers.

    2. You get a non-zero reading but it won't start. Check what temperature is your Gcode asking your bed? Is it higher than 90ºC? re-slice the file with a lower temp. The contacts allow to read the temperature but it is not heating. Do you see the red lights embedded in the platform? No Check contacts and apply the same solutions as in 1. Yes you are too impatient or still not all the heating circuits make proper contact.

    Possible solution: If you need more temperature, change it to a higher value in the gcode/slicer. Possibly anything starting at 60-70º is more than sufficient. The firmware allows to go up to 115ºC, but you might have to wait 30 minutes for the heated bed to arrive to this temperature, and you won't probably have any advantage.

Pillowing

Pillowing show up as bumps in the top surface of a print and can either be open or closed. The most important thing here is to make sure that your cooling fans are going top speed when the printer is laying down the top layer. Without proper cooling the thin strands of plastic tend to curl up and stick up above the surface of the print and make it harder for subsequent layers to properly span over the gap. With good cooling the strands gradually grow over the gaps until it closes fully.

Besides cooling you also need to print a thick enough top surface so that the printer can properly close it. In general you should make sure that you are printing at least six top layers. Since the top and bottom thickness is set in mm you will have to do some basic math to make sure you're printing enough layers. If you are printing with a 0.1mm layer height you should make your top thickness at least 0.6mm.

In general you will need more top layers the thinner your layer height is. With very thin layers the thin strands of plastic are more likely to break before fully bridging over the gaps in the infill and providing a nice base for the following layer. You will therefore need to print more layers to make up for this. In other words very thin layers can be another cause of pillowing.

d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53c3e307e4b085fad945cd9f_file-9ryfuyfjl6.jpgThis image shows two prints done with exactly the same settings, except for one, the bottom print did not have the cooling fans enabled.

Some users have also reported that the change in infill pattern between 24% and 25% (and up) makes a big difference. The difference between infill percentages at 24 or lower and 25 and higher is how cura lays down each layer. The infill is a crosshatch pattern made with diagonal intersecting lines. At lower densities both directions are laid down for each layer while at higher densities it is only laid down in one direction per layer. So, for layer X it will do lines from the lower left to the upper right. At layer X+1 it will do lines going from lower right to upper left.
Elephant's foot

d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53ba99cfe4b09d13bf3cdb5f_file-nznhvow08g.jpg

It's very common that the first couple of layers of a print is wider than you expected them to be. This is because you will generally want to make sure the first layer is nicely squished into the build platform so that it sticks properly. By doing this the plastic gets squished out into a thicker line than normal and thus the bottom of the print will bulge out a bit like an elephant's foot. You can decrease this effect by levelling your bed so that the nozzle is slightly further away from the bed and lowering the bed temperature a bit. It's hard to get rid of this effect entirely without sacrificing bottom layer quality and bed adhesion. It will be easier on small prints as they are less likely to warp and detach from the platform and you can therefore get away with not squishing the first layer as hard.
Very visible lines on the bottom layer

d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53babb97e4b09d13bf3cdb7e_file-9bo8shakry.jpg

If the bottom layer of your print is showing very obvious print lines it's likely that your bed is simply levelled a little bit too far away from the nozzle. The closer to the nozzle the bed is on the first layer the harder the plastic will be squished into the bed and the lines will then blend together better. However, you can't go too closely as that will prevent the plastic from escaping from the nozzle properly. Pressure will build up and eventually the plastic will squirt out and create an ugly blob, or, it could cause the feeder to grind your filament which is something you don't want.
Under extrusion

d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53bbf859e4b09d13bf3cdd85_file-njow1ah4bz.jpg

Under extrusion is simply that the printer can not supply the amount of plastic that is asked for. Symptoms of this is missing layers, very thin layers or layers that have random dots and holes in them. This problem is probably the trickiest to find the direct cause for as there are so many variables at play.

The printer will do its best to try and achieve the printing speeds that you are asking for. If this is beyond what the printer is capable of you will run into problems. If the printer is at the very edge of its capability the amount of plastic being extruded will be reduced but the print keeps going normally. When this happens your printed object might look ok at first glance but if you look closer you will see that walls are not properly fused and there are gaps between fill lines.

If you go beyond this in-the-middle stage the printer tries pushing harder and harder to extrude the material but eventually the pressure will be too high. Ideally when this happens the extruder motor will do what we call a skip back where the axis of the motor spins in the opposite direction for about a quarter turn to relieve pressure. This will not damage the printer, it's an intended behaviour to prevent the filament from being ground up by the feeder. You will hear when this happens as it will make a *tock* sound and if you look closely at the filament that is being extruded you will see a sudden reduction in volume.
Walls not touching

d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53bbf985e4b08d4d93a1c413_file-hi8vwneclk.jpg

First of all you have to determine if the walls are not touching at all or if they are touching in some parts only. Using a cylinder as an example it is common that there will be two “sides” touching and two that do not.

This is very likely caused by the short belts not being tight enough. Please see this section which deals with this issue.
Grinding

d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53be84cce4b0f628cad49d69_file-i140xtehyw.jpg

Grinding happens when the motor tries to push the filament through the nozzle but for whatever reason it starts to slip on the filament and instead grinds the plastic down. The more it grinds the filament the less grip it is able to get and very soon it will not be able to move the filament neither in nor out.
Scratches

d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53c3cf9fe4b0bbe0c00d60f1_file-y7rjbmbofe.jpg

As the print head is completing a top layer travel moves can cause ugly lines to appear. This can be caused by a couple of things. Either the head is making an actual scratch on the surface or you are seeing slight oozing of plastic during the travel move.

You can try to enable the “z-hop” feature in cura which will find in the expert settings under the retraction heading: Expert → Open expert settings… This feature will make the printer lift the nozzle a tiny amount just before making a travel move and then move back down once it arrives at the destination. In combination with this you can increase the speed at which the printer executes travel moves. You can increase the default 150mm/s to 250mm/s without problems. The faster move will reduce the amount of time the nozzle can ooze out plastic. Also consider lowering your temperature to further reduce oozing.

To reduce oozing even more you can set the Minimum travel distance to 1 and set Minimum extrusion to 0. This will force cura to always retract before performing a travel move. This may add a bit of printing time as a retraction doesn't happen instantly.

A side effect of the z-hop feature is that it can leave behind a tiny little blob. However, a small blob is far less visible and easier to remove than a scratch.

By adding a thin solid layer on top of the object he was able to reduce the travel moves significantly. The thin layer of plastic was then cut to reveal the holes again.
"Hairy" print

d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_543d2a31e4b01a27d3c00773_file-esclhyqzyu.jpg

This is a tricky problem without a clear solution at the moment. This problem should not be confused withstringing which is a different issue. This problem is similar to stringing in appearance but the strands of plastic are very very thin and they seem to be able to appear even if there are no travel moves crossing over voids.

It seems to be fairly material dependent so consider trying a different roll of plastic and see if that helps.

Also make sure that your nozzle is clean so that small amounts of plastic isn't being deposited randomly during the print.

Thankfully the little hairs are quite easy to remove. Rubbing them off with your fingers work quite well. Another way, if you're a bit lazy, is to hit the print with the flame from a “jet” lighter very briefly. This will burn away the strands pretty cleanly. Don't use a regular lighter or a candle as it will likely leave ugly marks on it.
Ringing

d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53baa75fe4b08d4d93a1c20e_file-sdk3kvhfi4.jpg

Ringing is what we call the small waves or shadows that usually appear around sharp corners on a print. It's often very apparent if you have text on your print as you will see what looks like shadows of the text. This happens when the print head makes a sudden direction change and the inertia of the head causes vibrations that show up in the print. To combat this there's a couple of things you can do. Simply slowing down your print speed will help lessen the effect. Decreasing the acceleration of the printer will make a big impact on the reduction of ringing without affecting print speed too heavily.

There's also another defect that can look like ringing while it actually isn't. Something that can happen is that infill shows through to the outside layer. This can look similar to ringing. To get rid of this the solution is to print thicker outer walls to hide the infill. Try printing at least two outer shells which, with a standard nozzle, will equate to 0.8mm thick walls.

Excessive temperature can also cause strange vertical lines in a print. Try lowering the temperature slightly and see if that helps.

Excerpt from "A visual Ultimaker troubleshooting guide" by 3DVerkstan

For more details you can visit also this page.

Another good resource for a visual troubleshooting guide is this.
3d_troubleshooting.txt · Last modified: 2016/05/05 14:36 by jj
