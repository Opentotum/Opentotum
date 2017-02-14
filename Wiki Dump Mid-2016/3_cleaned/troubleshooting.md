
![Wrench Icon](imgs/icons/wrench-icon.png)

# General Troubleshooting #


## The FABtotum is not turning on. ##

**Description :** 
    *Despite a functional Powercable connection, the Fabtotum does not power on once power is supplied.*

**Solution:**    
    *Please check that the fuse in the back of the power connector, which is located between the plug and the power button, has been loaded in the correct position.*  
     *The unit usually receives a new fuse before being shipped, as during the factory tests a fuse is used.A correctly inserted fuseblock should look like the image below.*

![Powerconnector](imgs/connectors/C13_female_with_fuse.jpg)

## The AmbientLight is pulsing yellow for more than 3 minutes. ##

**Description :**
    *The Ambient light stays yellow as long as there is no serial connection between the totumduino and the Raspberry Pi.*

**Solution**
  * *Cause A - SD card corrupted*  
    This can happen trough a power outage or a forced shutdown. Please reflash the FabUI onto the SD.  
    *Link to SD Flash Page*

  * *Cause B - physical connection broken*  
    Are both devices, totumduino and Raspberry Pi,correct installed and connected? Recheck!

  * *Cause C - defect Raspberry Pi*  
    Test the Raspberry Pi with a Monitor attached (HDMI). Can you see the bootsequenz? No? You will need a new Pi then...


## I can't connect to the FABtotum ##

**Description :**
    *You are directly connected to the Fabtotum via the included LAN cable, none of the above errors fits, but you still can't connect to the FabUI?*  
  * **Cause A - Wrong network configuration:**  
    Did you read the manual and did what it said?  
    * Duh, i do many things, reading manuals ...not so much... - Let me tell you, once you do it, it's awesome :wink: [the LAN portion is what you need](http://www.fabtotum.com/setting-connecting-network/).
    
    * Yep, but it just won't connect... - Please follow the instructions below:  
    #### Windows: ####
    Press WIN+R at the same time  
    Copy/Paste *ncpa.cpl* into the new window that appeared in the bottom left corner and press ENTER (copy only the cursive text!)  
    RightClick on the *Ethernet* and select *Properties*  
    DoubleClick on the *Internetprotocoll, Version4*  
    Select *Use the following IP address* and enter type the following into the fields: (Please remember the numbers if you have already something in this fields!)  

    IP address: *169.254.1.2*  
    Subnet mask: *255.255.255.0*  
    Default Gateway: *169.254.1.1*  
    Leave the dns setting empty.

    ### Linux (If you know how to do this, please add it, thx) ###  

    You should now be able to connect to the [FABUI](http://169.154.1.2).  
    Don't forget to restore the settings after you successfully connected the Fabtotum with your WLAN.


## The Frontdoor or Sidepanel(Filamentside) switch stops the process ##  

**Description :**  
* The Frontdoor switch is on despite the fact that the front door is closed.
* Your Filamentspool is to big to close the Sidepanel.

**Solution:** From FABUI 0.75 upwards you can disable the frontdoor/sidepanel warning in the settings.


## 3D Printing ##

### Not extruding / No filament is coming out of the nozzle ###  

**Possible Causes:**

* Cause A - Units OLDER Than *July 2015*: Feeder not engaged.  

    Please check that the Feeder is engaged (Button pressed). After each print the Feeder disengages itself, but you can disable this through a physical hack.  ### insert link to conversion guide here ###

* Cause B - Blocked Nozzle
    
    Please follow this ![Link](http://www.fabtotum.com/cleaning-clogged-nozzle/) to the official Manual on how to clean the Nozzle
    
* Cause C - The nozzle is too close to the printing surface

    Increase the distance by pressing the Z+ button during the print or calibrate the Probe lenght (Maintenance -> Probe Lenght Calibration)

* Cause C - The temperature is too low
    
    Please try to Increase the temperature a bit (5-10°C should be enough) during prints. The Meltpoint of filaments can vary through things like color, sfx or basematerial.

## Filament not sticking on the plane ##

**Description :**
* Filament is not sticking / drops are left on the bed (Hybrid Head)  

**Possible Causes:**

* Cause A - The nozzle is too far from the bed  
    
    Rerun the Bedleveling from the Maintenance menu and check that the bowden tube is not getting catched while the bed moves up.

* Cause B - Extruder or bed temperature is too low  
    Increase the temperature of the bed and the extruder in the supported range and wait a few seconds  
    **Hybrid Head**: Don't surpass 210°C if you don't see any result.  
    **Bed**: Normally between 55-70°C.

* Cause C - Increase the stickiness of the bedLook. Please check the official Tipps [here](http://www.fabtotum.com/improving-3d-printed-object-adhesion-tips-tricks/).  

## Print not starting or the bed / extruder is not heating ##

**Possible Causes** :

* Cause A - the printbed is not making contact with the power supply connector** \\ Verify that the temperature can be read from the JOG menu,     \\ Try  set a temperature over 60°C and press "temperature" to see it grows.The Red LEDs on the Bed will turn on.     \\ If  it does not raise the bed is not at the right height or it's not making contact.     \\ Verify that the unit is not locked (no error message or safety warning) \\  \\ Check the connection pins are properly working. \\
    * **Cause B - the machine is currently in SAFETY LOCK mode   **  \\ 1. Check the temperature of the bed in the FABUIIt must not be 0°C. Push the bed from the right side towards the left side as to facilitate the contact. If The temperature is still zero remove the bed and check the contacts, if any of them is deformed try to put it in place with some pliers.     \\  \\ 2. You get a non-zero reading but it won't start. Check what temperature is your Gcode asking your bed? Is it higher than 90ºC? re-slice the file with a lower temp. The contacts allow to read the temperature but it is not heating. Do you see the red lights embedded in the platform? No Check contacts and apply the same solutions as in 1. Yes you are too impatient or still not all the heating circuits make proper contact.     \\  \\ Possible solution: If you need more temperature, change it to a higher value in the gcode/slicer. Possibly anything starting at 60-70º is more than sufficient. The firmware allows to go up to 115ºC, but you might have to wait 30 minutes for the heated bed to arrive to this temperature, and you won't probably have any advantage.

### Pillowing ###

Pillowing show up as bumps in the top surface of a print and can either be open or closed. The most important thing here is to make sure that your cooling fans are going top speed when the printer is laying down the top layer. Without proper cooling the thin strands of plastic tend to curl up and stick up above the surface of the print and make it harder for subsequent layers to properly span over the gap. With good cooling the strands gradually grow over the gaps until it closes fully.

Besides cooling you also need to print a thick enough top surface so that the printer can properly close it. In general you should make sure that you are printing at least six top layers. Since the top and bottom thickness is set in mm you will have to do some basic math to make sure you're printing enough layers. If you are printing with a 0.1mm layer height you should make your top thickness at least 0.6mm.

In general you will need more top layers the thinner your layer height is. With very thin layers the thin strands of plastic are more likely to break before fully bridging over the gaps in the infill and providing a nice base for the following layer. You will therefore need to print more layers to make up for this. In other words very thin layers can be another cause of pillowing.

{{http://d33v4339jhl8k0.cloudfront.net/docs/assets/53970867e4b0c76107b1091a/images/53c3e307e4b085fad945cd9f/file-9RYFuYfJL6.jpg?nolink&100}}This image shows two prints done with exactly the same settings, except for one, the bottom print did not have the cooling fans enabled.

Some users have also reported that the change in infill pattern between 24% and 25% (and up) makes a big difference. The difference between infill percentages at 24 or lower and 25 and higher is how cura lays down each layer. The infill is a crosshatch pattern made with diagonal intersecting lines. At lower densities both directions are laid down for each layer while at higher densities it is only laid down in one direction per layer. So, for layer X it will do lines from the lower left to the upper right. At layer X+1 it will do lines going from lower right to upper left.

### Elephant's foot ###

{{http://d33v4339jhl8k0.cloudfront.net/docs/assets/53970867e4b0c76107b1091a/images/53ba99cfe4b09d13bf3cdb5f/file-NZnhvOw08g.jpg?nolink&100  }}

It's very common that the first couple of layers of a print is wider than you expected them to be. This is because you will generally want to make sure the first layer is nicely squished into the build platform so that it sticks properly. By doing this the plastic gets squished out into a thicker line than normal and thus the bottom of the print will bulge out a bit like an elephant's foot. You can decrease this effect by levelling your bed so that the nozzle is slightly further away from the bed and lowering the bed temperature a bit. It's hard to get rid of this effect entirely without sacrificing bottom layer quality and bed adhesion. It will be easier on small prints as they are less likely to warp and detach from the platform and you can therefore get away with not squishing the first layer as hard.

### Very visible lines on the bottom layer ###

{{http://d33v4339jhl8k0.cloudfront.net/docs/assets/53970867e4b0c76107b1091a/images/53babb97e4b09d13bf3cdb7e/file-9BO8SHAKrY.jpg?nolink&100  }}

If the bottom layer of your print is showing very obvious print lines it's likely that your bed is simply levelled a little bit too far away from the nozzle. The closer to the nozzle the bed is on the first layer the harder the plastic will be squished into the bed and the lines will then blend together better. However, you can't go too closely as that will prevent the plastic from escaping from the nozzle properly. Pressure will build up and eventually the plastic will squirt out and create an ugly blob, or, it could cause the feeder to grind your filament which is something you don't want.

### Under extrusion ###

{{http://d33v4339jhl8k0.cloudfront.net/docs/assets/53970867e4b0c76107b1091a/images/53bbf859e4b09d13bf3cdd85/file-NJOw1Ah4bz.jpg?nolink&100  }}

Under extrusion is simply that the printer can not supply the amount of plastic that is asked for. Symptoms of this is missing layers, very thin layers or layers that have random dots and holes in them. This problem is probably the trickiest to find the direct cause for as there are so many variables at play.

The printer will do its best to try and achieve the printing speeds that you are asking for. If this is beyond what the printer is capable of you will run into problems. If the printer is at the very edge of its capability the amount of plastic being extruded will be reduced but the print keeps going normally. When this happens your printed object might look ok at first glance but if you look closer you will see that walls are not properly fused and there are gaps between fill lines.

If you go beyond this in-the-middle stage the printer tries pushing harder and harder to extrude the material but eventually the pressure will be too high. Ideally when this happens the extruder motor will do what we call a skip back where the axis of the motor spins in the opposite direction for about a quarter turn to relieve pressure. This will not damage the printer, it's an intended behaviour to prevent the filament from being ground up by the feeder. You will hear when this happens as it will make a <nowiki>*</nowiki>tock<nowiki>*</nowiki> sound and if you look closely at the filament that is being extruded you will see a sudden reduction in volume.

### Walls not touching ###

{{http://d33v4339jhl8k0.cloudfront.net/docs/assets/53970867e4b0c76107b1091a/images/53bbf985e4b08d4d93a1c413/file-hI8vWnECLk.jpg?nolink&100  }}

First of all you have to determine if the walls are not touching at all or if they are touching in some parts only. Using a cylinder as an example it is common that there will be two "sides" touching and two that do not.

This is very likely caused by the short belts not being tight enough. Please see [[http://support.3dverkstan.se/article/23-a-visual-ultimaker-troubleshooting-guide#circles|this section]] which deals with this issue.

===   ===

===   ===

###   ###

### Grinding ###

{{http://d33v4339jhl8k0.cloudfront.net/docs/assets/53970867e4b0c76107b1091a/images/53be84cce4b0f628cad49d69/file-i140XtEHYW.jpg?nolink&100  }}

Grinding happens when the motor tries to push the filament through the nozzle but for whatever reason it starts to slip on the filament and instead grinds the plastic down. The more it grinds the filament the less grip it is able to get and very soon it will not be able to move the filament neither in nor out. To help prevent this problem on the UM2 the feeder motor current is deliberately limited so that the motor will skip back before starting to grind the filament down. When this happens you will hear a //tock //   sound and the feeder wheel will spin in reverse for about a quarter turn.

### Scratches ###

{{http://d33v4339jhl8k0.cloudfront.net/docs/assets/53970867e4b0c76107b1091a/images/53c3cf9fe4b0bbe0c00d60f1/file-Y7RjbMbOfe.jpg?nolink&100  }}

As the print head is completing a top layer travel moves can cause ugly lines to appear. This can be caused by a couple of things. Either the head is making an actual scratch on the surface or you are seeing slight oozing of plastic during the travel move.

You can try to enable the "z-hop" feature in cura which will find in the expert settings under the retraction heading: ''Expert → Open expert settings…''   This feature will make the printer lift the nozzle a tiny amount just before making a travel move and then move back down once it arrives at the destination. In combination with this you can increase the speed at which the printer executes travel moves. You can increase the default 150mm/s to 250mm/s without problems. The faster move will reduce the amount of time the nozzle can ooze out plastic. Also consider lowering your temperature to further reduce oozing.

To reduce oozing even more you can set the Minimum travel distance to 1 and set Minimum extrusion to 0. This will force cura to always retract before performing a travel move. This may add a bit of printing time as a retraction doesn't happen instantly.

A side effect of the z-hop feature is that it can leave behind a tiny little blob. However, a small blob is far less visible and easier to remove than a scratch.

This effect is more prone to happen on surfaces which are broken up by holes since the head needs to move around more. "Dreamworker" on the Ultimaker forums came up with a clever workaround to reduce the complexity of the top surface. By adding a thin solid layer on top of the object he was able to reduce the travel moves significantly. The thin layer of plastic was then cut to reveal the holes again.

### "Hairy" print ###

{{http://d33v4339jhl8k0.cloudfront.net/docs/assets/53970867e4b0c76107b1091a/images/543d2a31e4b01a27d3c00773/file-EScLhyQzYu.jpg?nolink&100  }}

This is a tricky problem without a clear solution at the moment. This problem should not be confused with[[http://support.3dverkstan.se/article/23-a-visual-ultimaker-troubleshooting-guide#stringing|stringing]] which is a different issue. This problem is similar to stringing in appearance but the strands of plastic are very very thin and they seem to be able to appear even if there are no travel moves crossing over voids.

It seems to be fairly material dependent so consider trying a different roll of plastic and see if that helps.

Also make sure that your nozzle is clean so that small amounts of plastic isn't being deposited randomly during the print.

Thankfully the little hairs are quite easy to remove. Rubbing them off with your fingers work quite well. Another way, if you're a bit lazy, is to hit the print with the flame from a "jet" lighter very briefly. This will burn away the strands pretty cleanly. Don't use a regular lighter or a candle as it will likely leave ugly marks on it.

### Ringing ###

{{http://d33v4339jhl8k0.cloudfront.net/docs/assets/53970867e4b0c76107b1091a/images/53baa75fe4b08d4d93a1c20e/file-sDk3kVHFi4.jpg?nolink&100  }}

Ringing is what we call the small waves or shadows that usually appear around sharp corners on a print. It's often very apparent if you have text on your print as you will see what looks like shadows of the text. This happens when the print head makes a sudden direction change and the inertia of the head causes vibrations that show up in the print. To combat this there's a couple of things you can do. Simply slowing down your print speed will help lessen the effect. Decreasing the acceleration of the printer will make a big impact on the reduction of ringing without affecting print speed too heavily.

There's also another defect that can look like ringing while it actually isn't. Something that can happen is that infill shows through to the outside layer. This can look similar to ringing. To get rid of this the solution is to print thicker outer walls to hide the infill. Try printing at least two outer shells which, with a standard nozzle, will equate to 0.8mm thick walls.

Excessive temperature can also cause strange vertical lines in a print. Try lowering the temperature slightly and see if that helps.

Excerpt from [[http://support.3dverkstan.se/article/23-a-visual-ultimaker-troubleshooting-guide|"A visual Ultimaker troubleshooting guide"]] by [[http://3dverkstan.se/|3DVerkstan]]

For more details you can visit also [[http://reprap.org/wiki/Print_Troubleshooting_Pictorial_Guide|this]] page.


###= Milling ###=

----

###= Scanning ###=

----
