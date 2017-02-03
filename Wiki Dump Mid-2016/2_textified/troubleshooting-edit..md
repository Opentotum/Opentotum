
<p>
<a href="/lib/exe/detail.php?id=troubleshooting&media=pictures:wrench-icon-614x460.png" class="media" title="pictures:wrench-icon-614x460.png"><img src="/lib/exe/fetch.php?w=248&h=183&tok=ece492&media=pictures:wrench-icon-614x460.png" class="medialeft" alt="" width="248" height="183" /></a>
</p>

<h2>General Troubleshooting</h2>
<div class="level2">
<hr />

</div>

<h3>The FABtotum is not turning On.</h3>
<div class="level3">

<p>
<b>Description : </b> Despite a functional Power-cable connection, the Unit does not power on once the power button is pressed.<b><br/>

</b>
</p>
<ul>
<li class="level1"> <a href="/lib/exe/detail.php?id=troubleshooting&media=pictures:11529.jpg" class="media" title="pictures:11529.jpg"><img src="/lib/exe/fetch.php?w=118&h=124&tok=385d70&media=pictures:11529.jpg" class="medialeft" title="11529.jpg" alt="11529.jpg" width="118" height="124" /></a><b>Solution:  </b>    Please check that the fuse in the back of the power connector (it's located between the plug and the power button) has been loaded in the correct position. The unit usually receives a new fuse before being shipped, as during the factory tests a fuse is used.A correctly inserted Fuseblock should look like the image below</li>
</ul>

</div>

<h2></h2>
<div class="level2">
<hr />

</div>

<h3>Yellow Ambient light is pulsing for more than 3 minutes / can't connect.</h3>
<div class="level3">

<p>
The Ambient light is yellow when the totumduino board's serial port doesn't register any connection.
</p>
<ul>
<li class="level1"> <b>Cause A - SD card corrupted</b> <br/>
Usually this is caused by a forced shutdown.    <br/>
To fix it you must revert the SD card to factory settings by flashing the SD card back to normal.    <br/>
See <a href="/doku.php?id=sdflashing" class="wikilink1" title="sdflashing">Flashing an SD card</a></li>
</ul>

<p>
—-
</p>

</div>

<h3>I Can't connect to the FABtotum</h3>
<div class="level3">

<p>
<b>Description :</b>     while connected with the LAN cable provided i can't get to see the FAB UI or the Installation page<b>     <br/>
</b>
</p>
<ul>
<li class="level1"> <b>Cause A - Check your network configuration:</b>  <br/>
You can check your connection by trying to connect to <a href="http://169.254.1.2" class="urlextern" title="http://169.254.1.2"  rel="nofollow">http://169.254.1.2</a> (see first setup instructions).     <br/>
 If that fails you can look at the connection setting (on windows is visible under <em> Network and Internet&lt;nowiki&gt;\&lt;/nowiki&gt;Network and Sharing Center</em>      and then <em>Change adapter settings</em>      and right-click on your LAN adapter.     <br/>
 <br/>
Choose <em>Status</em>      and then Details. the IP should be listed as "IPV4 gateway".     <br/>
If not make sure that the Ethernet adapter is set to receive an IP automatically.     <br/>
Under <em>Change adapter settings</em>      right-click on your LAN adapter. then select properties , Internet Protocol Version 4 (TCP/IP V4).     <br/>
Everything should look as in the image below.     <br/>
 <br/>
<a href="/lib/exe/detail.php?id=troubleshooting&media=pictures:connection.png" class="media" title="pictures:connection.png"><img src="/lib/exe/fetch.php?w=267&h=297&tok=8e8323&media=pictures:connection.png" class="media" alt="" width="267" height="297" /></a></li>
</ul>

<p>
—-
</p>

</div>

<h3>The safety lock switch stops the process</h3>
<div class="level3">

<p>
<b>Description : </b>    the safety lock switch is on despite the fact that the front door is closed perfectly
</p>
<ul>
<li class="level1"> <b>Cause A - the spring of the switch is too strong / the front panel is deformed      <br/>
</b></li>
</ul>

<p>
From FABUI 0.75 you can disable the front door panel warning.
</p>

<p>
—-
</p>

</div>

<h2>3D Printing</h2>
<div class="level2">
<hr />

</div>

<h3>Not extruding / No filament coming out of the nozzle</h3>
<div class="level3">

<p>
<b>Description </b>: Filament is not coming out from the nozzle (Hybrid Head)    <br/>
<b>Possible Causes:</b>
</p>
<ul>
<li class="level1"> <b>Cause A - UNITS OLDER THAN July 2015: The Feeder is not engaged</b> <br/>
note: <em>The feeder will disengage itself after a print.</em>  <br/>
First, extract the white PTFE Feeding tube from the head by heating the extruder at 210°C from the JOG Menu In the FABUI.    <br/>
From there Go to Maintenance then select Feeder.    <br/>
Follow the instructions to locate and press the feeder mechanism. Be sure that the button inside and the back of the printing area is pushed with the right force.A "click" sound should come from the mechanism if fully engaged.      <br/>
 <br/>
<a href="/lib/exe/detail.php?id=troubleshooting&media=engaged.jpg" class="media" title="engaged.jpg"><img src="/lib/exe/fetch.php?w=270&h=298&tok=d72d52&media=engaged.jpg" class="media" title="engaged.jpg" alt="engaged.jpg" width="270" height="298" /></a> <br/>
 <br/>
When the feeder is engaged go back to the JOG menu, press the E tab in the right hand side of the panel.Press the plus button and see if the filament is moving inside the tube, by watching the end that was just unplugged from the Head.    <br/>
 <br/>
Press the Plus botton in the JOG menu until the filament sticks out for 3cm from the PTFE feeding tube. If the filament is coming out, carefully reinsert it in the head. Be careful to not get the filament stuck on the sides of the head when pushing it down. this will bend the filament and block extrusion.When inserting the tube and the filament, the nozzle should be pouring some molten plastic.    <br/>
Once the tube is firmly locked in place, extrude another 10mm by pressing the Plus button to verfy the correct extrusion of material.</li>
<li class="level2"> <b>Cause B - The nozzle is too close to the printing surface</b> <br/>
Increase the distance by pressing the Z+ button during the print or calibrate the Probe lenght (Maintenance -&gt; Probe Lenght Calibration)</li>
<li class="level2"> <b>Cause C - The temperature is too low</b> <br/>
You could try to Increase the temperature a bit (5-10°C would help) during prints.      <br/>
Some filaments, especially with colorants, have higher melting point (180-230°C).</li>
<li class="level2"> <b>Cause D - Excessive temperature    <br/>
</b>If the temperature is too high, the filament will melt before reaching the nozzle, causing excessive friction.    <br/>
Be sure to keep the cooling fan on (M106 at the start  of the gcode or "FAN always on" in slic3r)</li>
<li class="level2"> <b>Cause E - The nozzle is jammed   </b>  <br/>
First, Verify that the PTFE tube in the back is correctly sticking out and is not caught inside the back of the unit.      <br/>
Remove the tube from the head, and with the Z in the middle of the height (bed Halfway), try to push some filament Manually in the head. can you push the filament and see it being extruded?      <br/>
If not the nozzle could be obstructed and requiring some cleaning or the filament is not getting all the way down in the nozzle (getting caugth in the sides of the head before entering the heating chamber).      <br/>
Try  dipping some filament from the top by hand and then pulling it out for a  few times (with the nozzle at 210°C) helps to clean it.      <br/>
Insert a small 0.3mm electric wire in the nozzle while at 210°C from below and make sure there are no obstructions.   <br/>
For see how to clean the nozzle follow <a href="/doku.php?id=mantainance#clean_the_nozzle" class="wikilink1" title="mantainance">this</a> guide.</li>
</ul>

<p>
—-
</p>

</div>

<h3>Filament not sticking on the plane</h3>
<div class="level3">

<p>
<b>Description : </b>   Filament is not sticking / drops are left on the bed (Hybrid Head)    <br/>
<b>Possible Causes:</b>
</p>
<ul>
<li class="level1"> <b>Cause A - The nozzle is too far from the bed</b> <br/>
-Verify that the 4 bed set-screws are almost completely screwed in (highest position possible minus 2 turns)    <br/>
-Run the Probe Length Calibration wizard from the maintenance menu    <br/>
-Run the Assisted Bed Leveling procedure from the maintenance menu    <br/>
-be sure that the PTFE tube is not getting stuck in the back of the unit.</li>
<li class="level2"> <b>Cause B - Extruder or bed temperature is too low</b> <br/>
Increase the temperature of the bed and the extruder in the supported range and wait a few seconds:    <br/>
<b>Extruder</b>: Min 180°C, Don't surpass 210°C if you don't see any result.    <br/>
<b>Bed</b>: Min 55°C, Don't surpass 70°C if you don't see any result.</li>
<li class="level2"> <b>Cause C - The bed doesn't have a sticky coating</b> <br/>
Look on <a href="/doku.php?id=stick&id=stick" class="wikilink1" title="stick">this</a> page how to make your bed sticky</li>
</ul>

<p>
—-
</p>

</div>

<h3>Print not starting/ bed,extruder not heating</h3>
<div class="level3">

<p>
<b>Description:</b> The 3D print process is not starting     <br/>

<b>Possible Causes</b> :
</p>
<ul>
<li class="level1"> <b>Cause A - the bed is not making contact with the power supply connector</b> <br/>
Verify that the temperature can be read from the JOG menu,     <br/>
Try  set a temperature over 60°C and press "temperature" to see it grows.The Red LEDs on the Bed will turn on.     <br/>
If  it does not raise the bed is not at the right height or it's not making contact.     <br/>
Verify that the unit is not locked (no error message or safety warning) <br/>
 <br/>
Check the connection pins are properly working. <br/>
</li>
<li class="level2"> <b>Cause B - the machine is currently in SAFETY LOCK mode   </b>  <br/>
1. Check the temperature of the bed in the FABUIIt must not be 0°C. Push the bed from the right side towards the left side as to facilitate the contact. If The temperature is still zero remove the bed and check the contacts, if any of them is deformed try to put it in place with some pliers.     <br/>
 <br/>
2. You get a non-zero reading but it won't start. Check what temperature is your Gcode asking your bed? Is it higher than 90ºC? re-slice the file with a lower temp. The contacts allow to read the temperature but it is not heating. Do you see the red lights embedded in the platform? No Check contacts and apply the same solutions as in 1. Yes you are too impatient or still not all the heating circuits make proper contact.     <br/>
 <br/>
Possible solution: If you need more temperature, change it to a higher value in the gcode/slicer. Possibly anything starting at 60-70º is more than sufficient. The firmware allows to go up to 115ºC, but you might have to wait 30 minutes for the heated bed to arrive to this temperature, and you won't probably have any advantage.</li>
</ul>

</div>

<h3>Pillowing</h3>
<div class="level3">

<p>
Pillowing show up as bumps in the top surface of a print and can either be open or closed. The most important thing here is to make sure that your cooling fans are going top speed when the printer is laying down the top layer. Without proper cooling the thin strands of plastic tend to curl up and stick up above the surface of the print and make it harder for subsequent layers to properly span over the gap. With good cooling the strands gradually grow over the gaps until it closes fully.
</p>

<p>
Besides cooling you also need to print a thick enough top surface so that the printer can properly close it. In general you should make sure that you are printing at least six top layers. Since the top and bottom thickness is set in mm you will have to do some basic math to make sure you're printing enough layers. If you are printing with a 0.1mm layer height you should make your top thickness at least 0.6mm.
</p>

<p>
In general you will need more top layers the thinner your layer height is. With very thin layers the thin strands of plastic are more likely to break before fully bridging over the gaps in the infill and providing a nice base for the following layer. You will therefore need to print more layers to make up for this. In other words very thin layers can be another cause of pillowing.
</p>

<p>
<img src="/lib/exe/fetch.php?w=100&tok=17ce6c&media=http%3A%2F%2Fd33v4339jhl8k0.cloudfront.net%2Fdocs%2Fassets%2F53970867e4b0c76107b1091a%2Fimages%2F53c3e307e4b085fad945cd9f%2Ffile-9RYFuYfJL6.jpg" class="media" title="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53c3e307e4b085fad945cd9f_file-9ryfuyfjl6.jpg" alt="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53c3e307e4b085fad945cd9f_file-9ryfuyfjl6.jpg" width="100" />This image shows two prints done with exactly the same settings, except for one, the bottom print did not have the cooling fans enabled.
</p>

<p>
Some users have also reported that the change in infill pattern between 24% and 25% (and up) makes a big difference. The difference between infill percentages at 24 or lower and 25 and higher is how cura lays down each layer. The infill is a crosshatch pattern made with diagonal intersecting lines. At lower densities both directions are laid down for each layer while at higher densities it is only laid down in one direction per layer. So, for layer X it will do lines from the lower left to the upper right. At layer X+1 it will do lines going from lower right to upper left.
</p>

</div>

<h3>Elephant's foot</h3>
<div class="level3">

<p>
<img src="/lib/exe/fetch.php?w=100&tok=bec562&media=http%3A%2F%2Fd33v4339jhl8k0.cloudfront.net%2Fdocs%2Fassets%2F53970867e4b0c76107b1091a%2Fimages%2F53ba99cfe4b09d13bf3cdb5f%2Ffile-NZnhvOw08g.jpg" class="medialeft" title="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53ba99cfe4b09d13bf3cdb5f_file-nznhvow08g.jpg" alt="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53ba99cfe4b09d13bf3cdb5f_file-nznhvow08g.jpg" width="100" />
</p>

<p>
It's very common that the first couple of layers of a print is wider than you expected them to be. This is because you will generally want to make sure the first layer is nicely squished into the build platform so that it sticks properly. By doing this the plastic gets squished out into a thicker line than normal and thus the bottom of the print will bulge out a bit like an elephant's foot. You can decrease this effect by levelling your bed so that the nozzle is slightly further away from the bed and lowering the bed temperature a bit. It's hard to get rid of this effect entirely without sacrificing bottom layer quality and bed adhesion. It will be easier on small prints as they are less likely to warp and detach from the platform and you can therefore get away with not squishing the first layer as hard.
</p>

</div>

<h3>Very visible lines on the bottom layer</h3>
<div class="level3">

<p>
<img src="/lib/exe/fetch.php?w=100&tok=2a541b&media=http%3A%2F%2Fd33v4339jhl8k0.cloudfront.net%2Fdocs%2Fassets%2F53970867e4b0c76107b1091a%2Fimages%2F53babb97e4b09d13bf3cdb7e%2Ffile-9BO8SHAKrY.jpg" class="medialeft" title="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53babb97e4b09d13bf3cdb7e_file-9bo8shakry.jpg" alt="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53babb97e4b09d13bf3cdb7e_file-9bo8shakry.jpg" width="100" />
</p>

<p>
If the bottom layer of your print is showing very obvious print lines it's likely that your bed is simply levelled a little bit too far away from the nozzle. The closer to the nozzle the bed is on the first layer the harder the plastic will be squished into the bed and the lines will then blend together better. However, you can't go too closely as that will prevent the plastic from escaping from the nozzle properly. Pressure will build up and eventually the plastic will squirt out and create an ugly blob, or, it could cause the feeder to grind your filament which is something you don't want.
</p>

</div>

<h3>Under extrusion</h3>
<div class="level3">

<p>
<img src="/lib/exe/fetch.php?w=100&tok=47b66c&media=http%3A%2F%2Fd33v4339jhl8k0.cloudfront.net%2Fdocs%2Fassets%2F53970867e4b0c76107b1091a%2Fimages%2F53bbf859e4b09d13bf3cdd85%2Ffile-NJOw1Ah4bz.jpg" class="medialeft" title="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53bbf859e4b09d13bf3cdd85_file-njow1ah4bz.jpg" alt="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53bbf859e4b09d13bf3cdd85_file-njow1ah4bz.jpg" width="100" />
</p>

<p>
Under extrusion is simply that the printer can not supply the amount of plastic that is asked for. Symptoms of this is missing layers, very thin layers or layers that have random dots and holes in them. This problem is probably the trickiest to find the direct cause for as there are so many variables at play.
</p>

<p>
The printer will do its best to try and achieve the printing speeds that you are asking for. If this is beyond what the printer is capable of you will run into problems. If the printer is at the very edge of its capability the amount of plastic being extruded will be reduced but the print keeps going normally. When this happens your printed object might look ok at first glance but if you look closer you will see that walls are not properly fused and there are gaps between fill lines.
</p>

<p>
If you go beyond this in-the-middle stage the printer tries pushing harder and harder to extrude the material but eventually the pressure will be too high. Ideally when this happens the extruder motor will do what we call a skip back where the axis of the motor spins in the opposite direction for about a quarter turn to relieve pressure. This will not damage the printer, it's an intended behaviour to prevent the filament from being ground up by the feeder. You will hear when this happens as it will make a <em><</em>nowiki>&#42;<em><</em>/nowiki>tock<em><</em>nowiki>&#42;<em><</em>/nowiki> sound and if you look closely at the filament that is being extruded you will see a sudden reduction in volume.
</p>

</div>

<h3>Walls not touching</h3>
<div class="level3">

<p>
<img src="/lib/exe/fetch.php?w=100&tok=719099&media=http%3A%2F%2Fd33v4339jhl8k0.cloudfront.net%2Fdocs%2Fassets%2F53970867e4b0c76107b1091a%2Fimages%2F53bbf985e4b08d4d93a1c413%2Ffile-hI8vWnECLk.jpg" class="medialeft" title="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53bbf985e4b08d4d93a1c413_file-hi8vwneclk.jpg" alt="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53bbf985e4b08d4d93a1c413_file-hi8vwneclk.jpg" width="100" />
</p>

<p>
First of all you have to determine if the walls are not touching at all or if they are touching in some parts only. Using a cylinder as an example it is common that there will be two "sides" touching and two that do not.
</p>

<p>
This is very likely caused by the short belts not being tight enough. Please see <a href="http://support.3dverkstan.se/article/23-a-visual-ultimaker-troubleshooting-guide#circles" class="urlextern" title="http://support.3dverkstan.se/article/23-a-visual-ultimaker-troubleshooting-guide#circles"  rel="nofollow">this section</a> which deals with this issue.
</p>

</div>

<h4></h4>
<div class="level4">

</div>

<h4></h4>
<div class="level4">

</div>

<h3></h3>
<div class="level3">

</div>

<h3>Grinding</h3>
<div class="level3">

<p>
<img src="/lib/exe/fetch.php?w=100&tok=ccb4c7&media=http%3A%2F%2Fd33v4339jhl8k0.cloudfront.net%2Fdocs%2Fassets%2F53970867e4b0c76107b1091a%2Fimages%2F53be84cce4b0f628cad49d69%2Ffile-i140XtEHYW.jpg" class="medialeft" title="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53be84cce4b0f628cad49d69_file-i140xtehyw.jpg" alt="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53be84cce4b0f628cad49d69_file-i140xtehyw.jpg" width="100" />
</p>

<p>
Grinding happens when the motor tries to push the filament through the nozzle but for whatever reason it starts to slip on the filament and instead grinds the plastic down. The more it grinds the filament the less grip it is able to get and very soon it will not be able to move the filament neither in nor out. To help prevent this problem on the UM2 the feeder motor current is deliberately limited so that the motor will skip back before starting to grind the filament down. When this happens you will hear a <em>tock </em>   sound and the feeder wheel will spin in reverse for about a quarter turn.
</p>

</div>

<h3>Scratches</h3>
<div class="level3">

<p>
<img src="/lib/exe/fetch.php?w=100&tok=1e78ad&media=http%3A%2F%2Fd33v4339jhl8k0.cloudfront.net%2Fdocs%2Fassets%2F53970867e4b0c76107b1091a%2Fimages%2F53c3cf9fe4b0bbe0c00d60f1%2Ffile-Y7RjbMbOfe.jpg" class="medialeft" title="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53c3cf9fe4b0bbe0c00d60f1_file-y7rjbmbofe.jpg" alt="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53c3cf9fe4b0bbe0c00d60f1_file-y7rjbmbofe.jpg" width="100" />
</p>

<p>
As the print head is completing a top layer travel moves can cause ugly lines to appear. This can be caused by a couple of things. Either the head is making an actual scratch on the surface or you are seeing slight oozing of plastic during the travel move.
</p>

<p>
You can try to enable the "z-hop" feature in cura which will find in the expert settings under the retraction heading: <code>Expert → Open expert settings…</code>   This feature will make the printer lift the nozzle a tiny amount just before making a travel move and then move back down once it arrives at the destination. In combination with this you can increase the speed at which the printer executes travel moves. You can increase the default 150mm/s to 250mm/s without problems. The faster move will reduce the amount of time the nozzle can ooze out plastic. Also consider lowering your temperature to further reduce oozing.
</p>

<p>
To reduce oozing even more you can set the Minimum travel distance to 1 and set Minimum extrusion to 0. This will force cura to always retract before performing a travel move. This may add a bit of printing time as a retraction doesn't happen instantly.
</p>

<p>
A side effect of the z-hop feature is that it can leave behind a tiny little blob. However, a small blob is far less visible and easier to remove than a scratch.
</p>

<p>
This effect is more prone to happen on surfaces which are broken up by holes since the head needs to move around more. "Dreamworker" on the Ultimaker forums came up with a clever workaround to reduce the complexity of the top surface. By adding a thin solid layer on top of the object he was able to reduce the travel moves significantly. The thin layer of plastic was then cut to reveal the holes again.
</p>

</div>

<h3>"Hairy" print</h3>
<div class="level3">

<p>
<img src="/lib/exe/fetch.php?w=100&tok=c5bcb8&media=http%3A%2F%2Fd33v4339jhl8k0.cloudfront.net%2Fdocs%2Fassets%2F53970867e4b0c76107b1091a%2Fimages%2F543d2a31e4b01a27d3c00773%2Ffile-EScLhyQzYu.jpg" class="medialeft" title="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_543d2a31e4b01a27d3c00773_file-esclhyqzyu.jpg" alt="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_543d2a31e4b01a27d3c00773_file-esclhyqzyu.jpg" width="100" />
</p>

<p>
This is a tricky problem without a clear solution at the moment. This problem should not be confused with<a href="http://support.3dverkstan.se/article/23-a-visual-ultimaker-troubleshooting-guide#stringing" class="urlextern" title="http://support.3dverkstan.se/article/23-a-visual-ultimaker-troubleshooting-guide#stringing"  rel="nofollow">stringing</a> which is a different issue. This problem is similar to stringing in appearance but the strands of plastic are very very thin and they seem to be able to appear even if there are no travel moves crossing over voids.
</p>

<p>
It seems to be fairly material dependent so consider trying a different roll of plastic and see if that helps.
</p>

<p>
Also make sure that your nozzle is clean so that small amounts of plastic isn't being deposited randomly during the print.
</p>

<p>
Thankfully the little hairs are quite easy to remove. Rubbing them off with your fingers work quite well. Another way, if you're a bit lazy, is to hit the print with the flame from a "jet" lighter very briefly. This will burn away the strands pretty cleanly. Don't use a regular lighter or a candle as it will likely leave ugly marks on it.
</p>

</div>

<h3>Ringing</h3>
<div class="level3">

<p>
<img src="/lib/exe/fetch.php?w=100&tok=e859af&media=http%3A%2F%2Fd33v4339jhl8k0.cloudfront.net%2Fdocs%2Fassets%2F53970867e4b0c76107b1091a%2Fimages%2F53baa75fe4b08d4d93a1c20e%2Ffile-sDk3kVHFi4.jpg" class="medialeft" title="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53baa75fe4b08d4d93a1c20e_file-sdk3kvhfi4.jpg" alt="d33v4339jhl8k0.cloudfront.net_docs_assets_53970867e4b0c76107b1091a_images_53baa75fe4b08d4d93a1c20e_file-sdk3kvhfi4.jpg" width="100" />
</p>

<p>
Ringing is what we call the small waves or shadows that usually appear around sharp corners on a print. It's often very apparent if you have text on your print as you will see what looks like shadows of the text. This happens when the print head makes a sudden direction change and the inertia of the head causes vibrations that show up in the print. To combat this there's a couple of things you can do. Simply slowing down your print speed will help lessen the effect. Decreasing the acceleration of the printer will make a big impact on the reduction of ringing without affecting print speed too heavily.
</p>

<p>
There's also another defect that can look like ringing while it actually isn't. Something that can happen is that infill shows through to the outside layer. This can look similar to ringing. To get rid of this the solution is to print thicker outer walls to hide the infill. Try printing at least two outer shells which, with a standard nozzle, will equate to 0.8mm thick walls.
</p>

<p>
Excessive temperature can also cause strange vertical lines in a print. Try lowering the temperature slightly and see if that helps.
</p>

<p>
Excerpt from <a href="http://support.3dverkstan.se/article/23-a-visual-ultimaker-troubleshooting-guide" class="urlextern" title="http://support.3dverkstan.se/article/23-a-visual-ultimaker-troubleshooting-guide"  rel="nofollow">"A visual Ultimaker troubleshooting guide"</a> by <a href="http://3dverkstan.se/" class="urlextern" title="http://3dverkstan.se/"  rel="nofollow">3DVerkstan</a>
</p>

<p>
For more details you can visit also <a href="http://reprap.org/wiki/Print_Troubleshooting_Pictorial_Guide" class="urlextern" title="http://reprap.org/wiki/Print_Troubleshooting_Pictorial_Guide"  rel="nofollow">this</a> page.
</p>

</div>

<h3></h3>
<div class="level3">

</div>

<h3></h3>
<div class="level3">

</div>

<h2>Milling</h2>
<div class="level2">
<hr />

</div>

<h2>Scanning</h2>
<div class="level2">

<p>
If the images look blurry, check if you remove the transparent protection film form the lens of the camera.
</p>
<hr />

</div>
