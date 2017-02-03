

upgrades-third-party_heads

  

Table of Contents


•Third Party Heads


•

◦Basic Informations

◾Mechanical Specifications


◾Electrical Specifications


◾Software Specifications


◾Safety


◾Licensing heads



 
Third Party Heads





Basic Informations



 The FABtotum Personal Fabricator has been developed to be a multipurpose personal fabrication platform.
 One of the key elements of the FABtotum' hardware is the head carriage.
 The head carriage can accommodate different heads beside the standard “Hybrid Head”.
Heads can be developed and even sold independently by anyone, to perform different tasks.
 The following are guidelines that will help developers to design and manufacture new heads. 

The FABtotum Personal Fabricator Carriage is the platform on which each and every head have to sit.
 The carriage provide Energy, Communication and other things trough the carriage connector plate.
 The carriage moves in the XY plane.


 Energy and communication is provided as specified in the electrical specifications 
 A retractable touch-probe, A laser line generator and a LED light are part of the assembly and are always available to be used during the use of custom/third-party heads, as long as they don't inferfere with each other 

(example: the probe hitting the lower part of a custom-made head). 

carriage.jpg 

The Connectors a Head should use to interface with the Fabtotum carriage are the Bourns 70AB/Male - Modular Contact Operating Characteristics and further information can be found here the corresponding .stp file for use in CAD are also provided by the manufacturer here. 

The five Bourne connectors (also used as a battery connector for some PDAs) are attached to the head and held in contact with the PCB by the lockdowns. So, when you lock the head in place it forces the contacts against the PCB. 

Mechanical Specifications


Each head is locked in place by interference with the carriage and a locking mechanism built in the carriage.
 Disengaging and engaging the locking mechanism is accomplished by pushing two levers on the side of the carriage.
 While the shape of the support plate of an head is critical for a precise lock, the locking mechanism function is to hold down the head and avoid undesired movements. 

carriage1.jpgcarriage2.jpgcarriage3.jpg 


 in the provided Step file a sample head mounting plate has been designed to provide basic dimensioning for a stable platform on which build the desired application.

 Mechanical specifications for the head are documented in the attached file Head-Carriage.zip (398.6 KB) 

Electrical Specifications



 The Carriage is connected to the Totumduino Board and can be controlled by the Raspberry Pi. 
 The pinout is critical to operations and it's achieved with spring-loaded contacts positioned on the head mounting plate or pcb (“pogo pins”).
Specifications for the contact module can be found here.
 The contact should always be protected by dust or accidental contacts by the head shape, see the “Hybrid Head” mounting plate.
 Pinout specifications for the head should always follow the Head Connector Pinout specifications, as reported in the following chart: 

 

Software Specifications


-Software safety features
-Automated head recognition guidelines
-Plugins for custom heads


Safety



 Each head as well as each optional hardware attached to the fabtotum should comply with these guidelines, as well as safety regulations and relative standards for the country of use and be marked accordingly to ensure safety and performance specifications are met.
 Please also note that FABtotum cannot be responsible or liable for use or misuse of third party heads. 

Licensing heads


The full documentation,drawings and the reproduction of the FABtotum Personal Fabricator is allowed and encouraged under the Creative Commons Attribution-Noncommercial-Sharealike 3.0 Unported Licence.
 Custom and Third-party heads can be reproduced and sold as the creator see fit, as long as:

- They are not marketed as FABtotum' official products 

1. They don't use the FABtotum trademark or graphical assets.


2. They don't pose direct danger or harm to users or can be used for illegal or questionable activities.


3. they comply with Mechanical, Electrical,Software, Safety and licensing standards outlined in this document.

  
upgrades-third-party_heads.txt · Last modified: 2015/10/21 16:46 by jj
 
--------------------------------------------------------------------------------
