
Basics


This is a basic tutorial to start writing your first FABui Plugin. For a better understanding of this tutorial It's good to have some skills on Codeigniter PHP Framework 
 With FABui plugins you can add functionality without changing the core programming of the FABui.
 A FABui plugin is a program, or a set of one or more functions, written in the PHP or PYTHON scripting language, that adds a specific set of features or services to the FABui. 

--------------------------------------------------------------------------------

Creating a plugin 

This section goes trough the steps you need to follow, and things to consider when creating a well-structured FABui plugin.

Plugin Name 
 The first task in creating a plugin is to think about what the plugin will do, and make a unique name for your plugin

Plugin Files 
 The next step is to create a PHP class file with a name derived from your chosen plugin name. For instance, if your plugin will be called “Hello World ” you might call your PHP class file helloworld.php . 

Again, use a unique name. People who install your plugin will be putting this PHP file into the FABui plugins directory application/plugins / , so no two plugins they are using can have the same PHP class file name.

 Another option is to split your plugin into muliple files. Your plugin must have at least on PHP file; it could also contain JavaScript files, CSS files, Image files, Python scripts, etc. Put all your plugins file into a directory that has the same name of the PHP file of your plugin.</font>
A good practice is to group all CSS files, JavaScript files and images into an “ assets ” directory, and group others scripts files in a “ lib ” directory 
All the “views” files must be saved into “views” folder: 

Files Header 
Now it's time to put some information into your main Plugin PHP file. 

Standard Plugin Information 
 <font 13px line-height: normal; background-color: rgb(250, 250, 250);/Verdana, Arial, Tahoma, Calibri, Geneva, sans-serif;;inherit;;rgb(51, 51, 51) font-family: Verdana, Arial, Tahoma, Calibri, Geneva, sans-serif; font-size: 13px; line-height: normal; background-color: rgb(250, 250, 250);>The top of your Plugin's main PHP class file must contain a standard Plugin information header. This header lets FABui recognize that your Plugin exists, add it to the Plugin management screen so it can be activated, load it, and run its functions; without the header, your Plugin will never be activated and will never run. Here is the header format: 

You can download this example here: 

• helloworld.zip (1.1 KB, 3 views)

  
forum.fabtotum.cc/showthread.php.txt · Last modified: 2014/12/14 17:55 by fabtotum