h-bot_x_and_y_axis

 
FABtotum's CoreXY: X and Y Axis


In an H-bot or CoreXY system the X or Y movements are basically a sum of 45 degrees vectors. We are effectively working on a tilted reference cartesian chart here. 

Since vectors add to one another the resulting force in the normal XY plane is much higher. Sounds complex? here a scheme: 

blog.fabtotum.com_wp-content_uploads_2014_04_layout-xy-2.jpg 

As you can see, with the same motors you get a different result than the basic cartesian system, with twice as much force in each direction (except in diagonal moves, ergo in the direction of the native tilted reference cartesian system). The price to pay is the distance you move, wich is effectively reduced to half, just as expected. 

This alternative driving method was simple and effective in most movements and condition but one: X-axis movements. To fight the movement on the Carriage, forces have to be balanced properly. If the XY carriage faces resistance (like in any machining), there is a resulting force in the gantry that causes the gantry itself to flex, generating positioning errors.
 This is pretty clear if you think of “what is holding what” and looking at the gantry.
 The Hbot design can bring substantial advantages during additive manufacturing but it’s not suitable for subtractive machining due to this problem. 

To balance the forces in a belt driven design, systems like the MIT’s Core XY have been developed, and we did some research too to see if it could fit our application. 

 

From a movement point of view the COREXY can be summed up as a normal cartesian motion tilted on a 45 degrees angle, just like the simpler H-Bot (see http://corexy.com/theory.html). 

Unlike the H-bot, however, the CoreXY introduced a crossed belt that balances the forces on the gantry. From this basic implementation the COREXY is a valid hybrid system that however has some flaws.
 First and foremost, the belt is very long, introducing a “dampening effect” due to the belt extending under tension. 

One solution is the one to increase the belt size, but this means more friction, noise and loss in force in a system with 8 idlers and 2 motor pulleys for a total of 8 90°angle turns and 2 180° angle turns. 

Never cross the belts
 Try to imagine all life as you know it stopping instantaneously and every molecule in your body exploding at the speed of light. Ok it’s not going to happen but that’s what you’d deserve for driving belts that way.
 Belts in the coreXY are not running on the same plane because they have to cross on one side to balance forces. The result is that each tooth of the belt entering the pulley encounters a non-straight pulley, wich results in noise and possibly ruining the belt in the long term. We love the coreXY beacause it’s essentially a great and smart solution. Many things like belts crossing could still be improved in the FABtotum and so we started working on it tirelessly to squeeze each and every last Newton we could. 

But before continuing let’s have a recap of some of the belt-driven systems we considered during the Alpha and Beta development. 

blog.fabtotum.com_wp-content_uploads_2014_04_layout-xy-3.jpg 

blog.fabtotum.com_wp-content_uploads_2014_04_layout-xy-4.jpg 

blog.fabtotum.com_wp-content_uploads_2014_04_layout-xy-5.jpg 

blog.fabtotum.com_wp-content_uploads_2014_04_layout-xy-6.jpg
 Our interpretation of the Core XY solution was to avoid crossing the belts, like in a H-bot style design, but still having the advantage of balanced forces of the Core XY design.
 The solution we adopted was to have 2 closed belt loops, on two different planes. 

This way effectively compensates the Hbot torque on the gantry with the help of the belt on the other side. At the same time avoids unortodox pulley mis-usages.
 The system works like this: 

blog.fabtotum.com_wp-content_uploads_2014_04_beta_xy.jpg 

M1, the left motor, drives the red circuit, while M2 drives the blue circuit. 

Those 2 belt circuits run each one on different levels, always straight and do not cross.
 Two equal and opposite forces “F” separated by a L distance generate a torque of M=2FL.
 In this solution the forces generate a couple on the carriage, wich is effectively mitigated by the short distance between the 2 forces.
 If we compare this to the Hbot, we basically moved the problem in a location where it couldn’t affect the system anymore.
 In other words, while in the Hbot “L” was really big (the distance between the motors) now L is the distance between the 2 anchor points on the carriage/head which can be as small as we want. 2F*(small L) = Small torque. 

blog.fabtotum.com_wp-content_uploads_2014_04_img_2251.jpg 
  
h-bot_x_and_y_axis.txt · Last modified: 2015/07/03 11:04 by jj