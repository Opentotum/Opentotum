
assembly_camera
Table of Contents

    Raspicam
        Specs
        Cleaning
        External Links:

Raspicam

p1680861m_1.jpg

The camera, which is used for 3D-scanning and Computer vision, is mounted on the Y axis, below the left-side linear bearing.
The camera assembly is composed by the following parts:

    A standard issue RPI-Camera Module
    A longer Flex cable compatible with the Raspberry Pi UART
    A custom made plastic camera casing/support

The camera is calibrated to focus on a specific distance instead of infinite. This is accomplished by turning the 3.5mm lens casing on top of the module. The RPI camera is well known to suffer from static shocks.
Specs

    Sensor type: OmniVision OV5647 Color CMOS QSXGA (5-megapixel)
    Sensor size: 3.67 x 2.74 mm
    Pixel Count: 2592 x 1944
    Pixel Size: 1.4 x 1.4 um
    Lens: f=3.6 mm, f/2.9
    Angle of View: 54 x 41 degrees
    Field of View: 2.0 x 1.33 m at 2 m
    Full-frame SLR lens equivalent: 35 mm
    Fixed Focus: 1 m to infinity
    Video: 1080p at 30 fps with codec H.264 (AVC)
    Up to 90 fps Video at VGA
    Board size: 25 x 24 mm (not including flex cable)

Because the focal length of the lens is roughly the same as the width of the sensor, it is easy to remember the field of view: at x meters away, you can see about x meters horizontally, assuming 4×3 stills mode. Horizontal field of view in 1080p video mode is 75% of that (75% H x 55% V sensor crop for 1:1 pixels at 1920×1080).
Cleaning

The camera can be cleaned with canned air first and a clean cloth.
Do not apply force when cleaning the lens.
External Links:

http://www.raspberrypi.org/wp-content/uploads/2013/07/RaspiCam-Documentation.pdf
https://www.raspberrypi.org/documentation/raspbian/applications/camera.md
assembly_camera.txt · Last modified: 2015/10/23 15:03 by jj
