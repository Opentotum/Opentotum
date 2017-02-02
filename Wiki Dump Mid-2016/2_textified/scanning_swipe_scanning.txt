

scanning_swipe_scanning

 
Swipe scanning


This scanning method uses the raspicam and the laser line to make a 3D scan. 

swipe_scanning.jpg 

It works likewise the Rotating scanning, and i't used to scan objects that can't be easily fixed on the 4th axis chuck. 

It takes two pictures of an object placed on the bed: one with the line projected on the object to scan and one without. Then the post processor installed on the Raspberry makes a subtraction between the two images, obtaining just the line modified on the object's profile. Many lines will compose the point cloud. 
  
scanning_swipe_scanning.txt · Last modified: 2016/03/22 15:30 by jj