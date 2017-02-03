

electrical_continuity_probe

  

Table of Contents


•Electrical continuity z probe

◦1. Construction


◦2. Setup


◦3. Accuracy, Precision and error

◾3.1. Initial tests and results


◾3.2. More tests



 
Electrical continuity z probe



1. Construction


This shows how to create an electrical continuity probe like the one used for the PCBMill plugin. 

To make this probe you need: 

1. Two rather long cables (make sure they can go from the connector all the way up to the top of the FAB and back to the lowest position of the bed, so that when/if G27 is executed, the cable is long enough).


2. A 2 pin PH connector,


3. A 1 kOhm resistor.


4. (Optional) a metal washer for a M4/M5 screw (or whatever screw you will use to attach the cooper clad to the the substactive platform).


How to do it: 

1. Attach each cable to a pin of the connector.


2. Attach each cable to one end of the resistor (by soldering for example)


3. Attach the washer (or the whatever you are using to connect the probe to the copper clad) to the cable to the left when looking at the photo:


ASCII User comments 

This is how it looks when the washer is connected to the copper clad. 

ASCII User comments 

You are done!! 

2. Setup


I think that the best way is to connect the probe to an screw located near the back left corner of the working area. This way the cable is located behind the X-carriage, which prevents the cable from being trapped when a homing procedure (G28) is executed. 

One possible routing of the cables is, from the totumduino, between the totumduino board and the cable going to the Y_MAX endstop, to the same slot where the flex cable goes, then from there (in the rear panel) to the slot with the brushes in the top-back-left area of the working area, just between the brushes. I have it there permanently. This allows to close the left side panel. 

3. Accuracy, Precision and error


This section is under construction and intended more as a discussion due to the low quality of the images in the forums. 

3.1. Initial tests and results


I have been doing some investigation regarding the accuracy, precision and error introduced by the electrical conductivity probe. Here accuracy is the closeness between the measured value and the real true value and precision is the difference between the measured values. The measurement resolution of the probe is 0.01 mm as this is what the firmware provides. For a refresher on accuracy, precision, measurement resolution, follow the link: 

http://en.wikipedia.org/wiki/Accuracy_and_precision 

I have conducted an experiment where the SAME 4 points are probed in a copper clad: 

1. Tests 1-5: Each point is probed 10 times at 100 mm/m feedrate. 

2. Tests 6-10: Each point is probed 10 times at 50 mm/m feedrate. 

3. Tests 11-16: Each point is probed 100 times at 100 mm/m feedrate (I chose 100 mm/m as I can not see any advantage from using 50 mm/m). 

Results:  

So, this first graph represents the distribution of measured values at each point. It is worth mentioning that all the measurements are put together, so the first 10 tests contribute with 10 measurement each, whereas the last 6 tests contribute with 100 measurements each. This means that this distribution is biased towards the last 6 tests (should any test dependent error exist, we will revisit this later, but those outliers in under the whiskers are related to this). 

So you might have been fast and draw your conclusion that each measurement has around of 50 um of precision (from the whiskers, set by default to 1.5*IQR by Sage), or taking into account my remark on the number of points, maybe 100 um (first measurement point goes from around 9.25 mm to 9.35 mm). 

Let's investigate a little bit further. This new graph splits the measurements by test cases: 

So, it seems like if we consider each test in isolation, we have a precision (from whiskers) of around 20 um. If we go into observing the outliers, most of the outliers over the top whisker are mostly 10 um over the median value (taking into account that our measurement resolution is 10 um this is great). If we observe the bottom outliers (those under the bottom whisker), this mainly happens on the measurements at the first point. Moreover, the bottom outliers at the points other than the first point are also mostly 10 um under the median value (taking into account that our measurement resolution is 10 um this is great). However, at the first point, there are bottom outliers even 50 umunder the median value of the distribution. 

The fact that it happens only at the first point makes me think that it may be related to a systemic measurement error source (mechanical source?, firmware?), more than a random error (if it would be random then it would appear at all the locations equally). 

The other observation to be done in this graph, is that the median values of the measurements at a given point also differ around 50 um. So there also seems to be anothersource of error, that I think it is systemicand that I do not know if it may be related to the first systemic error or not. 

I have tried to determine how these errors happen. In order to investigate error 1, I studied the temporal variability of the measurements of each test. So I have plotted the measurements of each case. Please not thatI did a mistakelabeling the x axis, the x axis represents the measurement number, that is why the first 10 measurements only go from 0 to 10, whereas the rest goes to 100: 

 

The first observation that I made in this graph is that the first measurements at the first point have much more variation than rest and that this variation happens during the first 2-3 measurement points (40 um is the variation in test 5, see array pcbstr[4] in the raw data below), after that, they vary +/- 10 um from this “reference value” (which is perfectly fine with a measurement resolution of 10 um and can be taken care by averaging). This is the same for all the other points, but from the begining. They just vary around 10 um from the first measurement onwards… 

So I ignore the source (help me here!), but I know that I can get rid of this error by excluding from the measurement the first 2-3 measurements of the first measurement point (it is like it would need some time to get into measuring correctly… FAB you are lazy… :) ). 

Here I assume that those 2-3 measurements are wrong, but actually it could be also the other way around, it could the that those 2-3 measurements are closer to the real value, and that by measuring the to-be-measured value is altered towards the “steady state value”. This I can not know without another measurement method (like a dial indicator). 

As expected, using the median instead of the average filters out this errors. The fact that the mode almost always matches the median is nothing but an indicator of what we know from above, i.e. that after some measurements, almost always the same value is returned for the rest. In this situation, it would not help to just exclude the outliers and average the rest to decrease the random error, as the random error is under the measurement resolution. This is clear in this graph: 

In order to investigate the second source of error (varying median values among tests), and inspired by the fact that the measurements of the points 2-3 seem to vary in accordance with the variation of point 1, I produced this graph: 

 

This graph presents the difference between the mean/median/mode of the probed values of each test case - the median value of the first point of the test case (so in other words, for each test references those statistics to the median value of the first point). No surprise that the error of the first point is zero (by definition). The interesting result is in the other points. The leveling error is the same in all test cases (within +/- 10 um corresponding to the measurement resolution), even though the averaged measured value is indeed different (within 50 um). This means that even though the probe does not measure the same values in each test, the differences in level between each point are the same (within 20 um, i.e. +/- 10 um). 

So, yes we have a measurement error of yet unknown source that is introduced at the begining (let's say it is a random accuracy error, as we do not know the true value), but if we raise the probe to the samedistance and repeat the measurement, even if we change the XY position inbetween, then the same unknown error is present in all the measurements, and the differences cancel the error, thereby providing leveling results within 20 um (+/- 10 um). 

I have though this may be due to the backslash, however my knowledge of this mechanical effect is very much limited, and I am very much interested in your feedback. 

I plan to introduce modifications in PCBMill to reduce the error, but it always helps to provide the right solution to understand the causes, just to treat the root of the problem, not the sympthoms. 

Raw_data pcbstr = []; 

 pcbstr.append([]); 

 # test1 10 probed points at 100 feedrate 
 pcbstr[0]="168.92", "78.47", ["9.28","9.29","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30"], "True"], ["219.39", "78.47", ["9.36","9.36","9.36","9.36","9.36","9.36","9.36","9.36","9.36","9.36"], "True"], ["168.92", "138.82", ["9.17","9.17","9.17","9.17","9.17","9.17","9.17","9.18","9.18","9.18"], "True"], ["219.39", "138.82", ["9.27","9.27","9.27","9.27","9.27","9.27","9.27","9.27","9.27","9.27"], "True"; 


 pcbstr.append([]); 

 pcbstr[1]="168.92", "78.47", ["9.26","9.29","9.30","9.30","9.30","9.31","9.31","9.31","9.31","9.31"], "True"], ["219.39", "78.47", ["9.37","9.37","9.37","9.37","9.37","9.37","9.37","9.38","9.37","9.37"], "True"], ["168.92", "138.82", ["9.17","9.17","9.17","9.17","9.17","9.18","9.18","9.18","9.18","9.18"], "True"], ["219.39", "138.82", ["9.28","9.28","9.28","9.28","9.28","9.28","9.28","9.28","9.28","9.28"], "True"; 


 pcbstr.append([]); 

 pcbstr[2]="168.92", "78.47", ["9.27","9.30","9.31","9.31","9.32","9.32","9.32","9.32","9.32","9.32"], "True"], ["219.39", "78.47", ["9.38","9.38","9.38","9.38","9.38","9.38","9.38","9.38","9.38","9.38"], "True"], ["168.92", "138.82", ["9.18","9.18","9.18","9.18","9.19","9.19","9.19","9.18","9.19","9.19"], "True"], ["219.39", "138.82", ["9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29"], "True"; 

 pcbstr.append([]); 

 pcbstr[3]="168.92", "78.47", ["9.29","9.31","9.32","9.32","9.32","9.33","9.33","9.32","9.33","9.32"], "True"], ["219.39", "78.47", ["9.38","9.38","9.38","9.38","9.38","9.38","9.38","9.38","9.38","9.38"], "True"], ["168.92", "138.82", ["9.18","9.18","9.18","9.18","9.19","9.18","9.19","9.19","9.18","9.19"], "True"], ["219.39", "138.82", ["9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29"], "True"; 

 pcbstr.append([]); 

 pcbstr[4]="168.92", "78.47", ["9.29","9.31","9.32","9.32","9.33","9.33","9.33","9.33","9.33","9.33"], "True"], ["219.39", "78.47", ["9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39"], "True"], ["168.92", "138.82", ["9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19"], "True"], ["219.39", "138.82", ["9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29"], "True"; 

 #test2 10 probed points at 50 feedrate 

 pcbstr.append([]); 

 pcbstr[5]="168.92", "78.47", ["9.29","9.31","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32"], "True"], ["219.39", "78.47", ["9.38","9.38","9.38","9.38","9.38","9.38","9.38","9.38","9.38","9.38"], "True"], ["168.92", "138.82", ["9.18","9.18","9.18","9.18","9.18","9.18","9.19","9.19","9.18","9.19"], "True"], ["219.39", "138.82", ["9.29","9.29","9.28","9.29","9.29","9.28","9.29","9.29","9.28","9.28"], "True"; 

 pcbstr.append([]); 

 pcbstr[6]="168.92", "78.47", ["9.29","9.31","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32"], "True"], ["219.39", "78.47", ["9.38","9.38","9.38","9.38","9.38","9.38","9.38","9.38","9.38","9.38"], "True"], ["168.92", "138.82", ["9.18","9.18","9.18","9.18","9.18","9.18","9.19","9.19","9.18","9.19"], "True"], ["219.39", "138.82", ["9.29","9.29","9.28","9.29","9.29","9.28","9.29","9.29","9.28","9.28"], "True"; 

 pcbstr.append([]); 

 pcbstr[7]="168.92", "78.47", ["9.30","9.32","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33"], "True"], ["219.39", "78.47", ["9.39","9.39","9.39","9.38","9.38","9.39","9.39","9.38","9.38","9.38"], "True"], ["168.92", "138.82", ["9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20"], "True"], ["219.39", "138.82", ["9.30","9.30","9.29","9.29","9.30","9.29","9.29","9.30","9.29","9.30"], "True"; 

 pcbstr.append([]); 

 pcbstr[8]="168.92", "78.47", ["9.30","9.32","9.32","9.33","9.33","9.33","9.33","9.33","9.33","9.33"], "True"], ["219.39", "78.47", ["9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39"], "True"], ["168.92", "138.82", ["9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19"], "True"], ["219.39", "138.82", ["9.30","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29"], "True"; 

 pcbstr.append([]); 

 pcbstr[9]="168.92", "78.47", ["9.31","9.33","9.33","9.33","9.33","9.33","9.33","9.34","9.34","9.34"], "True"], ["219.39", "78.47", ["9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39"], "True"], ["168.92", "138.82", ["9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20"], "True"], ["219.39", "138.82", ["9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30"], "True"; 

#test3 100 probed points at 100 feedrate 

 pcbstr.append([]); 

 pcbstr[10]="168.92", "78.47", ["9.30","9.32","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.34","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.34","9.33","9.34","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.34","9.33","9.33","9.33","9.33","9.34","9.33","9.33","9.34","9.33","9.33","9.33","9.33","9.33","9.33","9.34","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.34","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33"], "True"], ["219.39", "78.47", ["9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39"], "True"], ["168.92", "138.82", ["9.20","9.19","9.19","9.20","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.20","9.19","9.19","9.20","9.19","9.19","9.19","9.19","9.20","9.20","9.19","9.19","9.19","9.19","9.19","9.20","9.20","9.20","9.20","9.19","9.20","9.19","9.19","9.20","9.20","9.19","9.20","9.19","9.20","9.20","9.19","9.20","9.20","9.19","9.20","9.19","9.19","9.20","9.19","9.20","9.19","9.19","9.20","9.20","9.20","9.20","9.20","9.19","9.19","9.20","9.19","9.20","9.19","9.20","9.19","9.20","9.19","9.19","9.20","9.20","9.20","9.20","9.19","9.19","9.19","9.19","9.20","9.19","9.20","9.19","9.20","9.19","9.20","9.20","9.20","9.19","9.19","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.19","9.20","9.20","9.20","9.20"], "True"], ["219.39", "138.82", ["9.30","9.30","9.31","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30"], "True"; 

 pcbstr.append([]); 


 pcbstr[11]="168.92", "78.47", ["9.31","9.33","9.34","9.34","9.34","9.34","9.34","9.34","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.34","9.34","9.35","9.34","9.35","9.35","9.34","9.35","9.35","9.35","9.35","9.35","9.35","9.34","9.34","9.34","9.35","9.35","9.34","9.34","9.35","9.35","9.35","9.34","9.35","9.35","9.35","9.35","9.34","9.34","9.35","9.35","9.34","9.35","9.34","9.34","9.34","9.34","9.35","9.35","9.35","9.35","9.34","9.35","9.34","9.35","9.35","9.34","9.35","9.35","9.34","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.34","9.34","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35","9.35"], "True"], ["219.39", "78.47", ["9.41","9.41","9.41","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40"], "True"], ["168.92", "138.82", ["9.21","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.21","9.21","9.20","9.20","9.20","9.20","9.21","9.20","9.20","9.21","9.20","9.20","9.20","9.21","9.20","9.21","9.21","9.21","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.21","9.21","9.20","9.21","9.20","9.20","9.20","9.21","9.20","9.20","9.20","9.20","9.21","9.21","9.20","9.21","9.21","9.21","9.21","9.21","9.21","9.21","9.21","9.21","9.21","9.21","9.21","9.20","9.21","9.21","9.21","9.21","9.20","9.21","9.21","9.21","9.20","9.21","9.21","9.21","9.21","9.21","9.21","9.21","9.21"], "True"], ["219.39", "138.82", ["9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31","9.31"], "True" 



 pcbstr.append([]); 

 pcbstr[12]="168.92", "78.47", ["9.31","9.33","9.33","9.33","9.33","9.34","9.33","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.35","9.35","9.35","9.35","9.35","9.35","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.33","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34"], "True"], ["219.39", "78.47", ["9.39","9.39","9.40","9.40","9.40","9.39","9.40","9.40","9.40","9.39","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.41","9.41","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.41","9.39","9.39","9.39","9.39","9.39","9.40","9.40"], "True"], ["168.92", "138.82", ["9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.19","9.19","9.20","9.20","9.20"], "True"], ["219.39", "138.82", ["9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.31","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.31","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.31","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30"], "True" 

 pcbstr.append([]); 

 pcbstr[13]="168.92", "78.47", ["9.30","9.32","9.33","9.33","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.34","9.33","9.33","9.33","9.33","9.33","9.34","9.34","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.34","9.33","9.33","9.33","9.33","9.33","9.34","9.34","9.33","9.33","9.33","9.34","9.34","9.34","9.33","9.34"], "True"], ["219.39", "78.47", ["9.40","9.40","9.40","9.41","9.40","9.39","9.40","9.39","9.39","9.40","9.39","9.39","9.39","9.39","9.40","9.39","9.39","9.39","9.39","9.39","9.40","9.40","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.40","9.39","9.40","9.39","9.39","9.39","9.39","9.40","9.40","9.39","9.39","9.39","9.39","9.39","9.40","9.39","9.40","9.39","9.39","9.39","9.39","9.39","9.40","9.39","9.40","9.39","9.39","9.39","9.39","9.39","9.39","9.40","9.39","9.39","9.40","9.39","9.39","9.40","9.40","9.40","9.39","9.40","9.39","9.40","9.39","9.40","9.39","9.39","9.39","9.39","9.40","9.39","9.39","9.40","9.39","9.39","9.39","9.40","9.40","9.39","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40","9.40"], "True"], ["168.92", "138.82", ["9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.21","9.20","9.21","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.21","9.20","9.20","9.21","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.21","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20","9.20"], "True"], ["219.39", "138.82", ["9.30","9.30","9.30","9.30","9.31","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.31","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30"], "True" 

pcbstr.append([]); 

 pcbstr[14]="168.92", "78.47", ["9.30","9.32","9.32","9.32","9.33","9.33","9.33","9.33","9.33","9.34","9.34","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33"], "True"], ["219.39", "78.47", ["9.40","9.39","9.39","9.40","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.40","9.40","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.40","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.41","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.40","9.40","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.40","9.39"], "True"], ["168.92", "138.82", ["9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.20","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.20","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.20","9.19","9.19","9.20","9.19","9.19","9.19","9.19","9.19"], "True"], ["219.39", "138.82", ["9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.29","9.30","9.29","9.30","9.30","9.30","9.30","9.30","9.29","9.30","9.29","9.30","9.30","9.30","9.30","9.29","9.30","9.29","9.29","9.30","9.30","9.30","9.30","9.30","9.30","9.29","9.30","9.30","9.29","9.30","9.29","9.30","9.30","9.30","9.30","9.29","9.30","9.30","9.29","9.30","9.30","9.29","9.29","9.30","9.30","9.30","9.29","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30"], "True" 

 pcbstr.append([]); 

 pcbstr[15]="168.92", "78.47", ["9.29","9.30","9.31","9.31","9.32","9.33","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.33","9.32","9.32","9.32","9.32","9.32","9.32","9.32","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.33","9.32","9.33","9.32","9.33","9.33","9.33","9.33","9.32","9.32","9.33","9.33","9.32","9.33","9.33","9.33","9.33","9.33","9.33","9.32"], "True"], ["219.39", "78.47", ["9.39","9.39","9.39","9.39","9.39","9.39","9.38","9.39","9.38","9.39","9.38","9.39","9.38","9.38","9.39","9.38","9.39","9.38","9.38","9.38","9.39","9.38","9.38","9.39","9.38","9.38","9.39","9.39","9.39","9.39","9.38","9.39","9.38","9.38","9.38","9.39","9.39","9.39","9.38","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39","9.39"], "True"], ["168.92", "138.82", ["9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19","9.19"], "True"], ["219.39", "138.82", ["9.30","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.30","9.29","9.29","9.29","9.29","9.30","9.30","9.29","9.29","9.30","9.29","9.29","9.30","9.29","9.30","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.29","9.30","9.29","9.29","9.30","9.29","9.29","9.29","9.30","9.30","9.29","9.29","9.29","9.30","9.29","9.29","9.30","9.29","9.29","9.29","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.30","9.29","9.30","9.30","9.30","9.30","9.29","9.30","9.29","9.30","9.30","9.29","9.29","9.30"], "True" 

3.2. More tests


I have repeated the initial tests after sanding the PCB (to remove the effect that an hypothetical coating might have had in the initial tests). The results are the same as before, so this was not playing a role in it. 

I have implemented a modification to the probing algorithm. It probes the first point 5 times more than the rest of the points, and the first 5 measurements at the first point are excluded from the probing results (to account for one of the errors described above). I have done: 

1. 9 tests with 4 probing points (the area is different from the one of the initial tests), 10 times probed at each point. 

2. 7 tests with 16 probing points (same are as in 1), 10 times probed at each point. 

The modification effectively removes the effect of those outliers of in the first measurement (I do not want to flood the wiki with graphs so I omit those). The interesting results of today are: 

1. The measurement at a point seems to depend slightly (20 um difference) on the point that was probed before. This is, with 16 probed points and 4 probed points, the measurements of the 4 corners that are common have consistent differences. This holds even when a 4 probed points is repeated after a 16 probed points one. So whatever physical effect that is responsible for the difference depends slightly on the point measured before. 

2. I have been able to quantify the precision, assuming that the median value of the values measured at a given point is the true value (that is why is a precision measurement and not an accuracy measurement). 

These are the distribution of the leveling error measurements (how much a point is not within an horizontal plane passing at the first measurement point), based on only one measured value at each point (based on the first measurement taken). So yes, I took 10 measurements, but here I considering the leveling error I would have if I would only consider the first measurement (assuming that the median of the 10 measurements is the true value): 

 

 

The following is the same graph, but the median value at each point is substracted, so that it helps see the precision within the scale (so is the distribution of the measurements once the corner points are corrected by the median value, so what is used to correct the gcode): 

 

So, this more or less means that if I measure 6 times at the first point and take the last measurement of those (exclude the first 5 points) and I measure 1 time in the remaining points, the error I may incur in by only considering one measurement (plus the error of measurement, backlash, whatever), is within 30 um. 
  
electrical_continuity_probe.txt · Last modified: 2015/05/05 20:48 by imarin
 
--------------------------------------------------------------------------------
