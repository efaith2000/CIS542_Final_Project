# CIS542_Final_Project

This program was written by Eric Faith for CIS 542 - Digital Forensics, in December 2023.

This program can be utilized by opening it in any Python IDE or compiler, and simply executing it. No changes whatsoever are required for proper execution. The only requirement is that the User account that is being used when running the program must have administrator privileges, as the operation of the program requires administrative access.

The purpose of this program is to identify a list of all USB devices that a computer has ever been plugged into. This includes storage devices (e.g. external hard drives), as well as any other USB-connected device (e.g. a smart phone). By running this code, the program will obtain this information by accessing the Windows Registry, accessing the Local Machine Hive, and identifying the USB key, which contains a list of all devices that have been plugged into the computer via USB. It will then iterate through each device and print the manufacturer, hardware ID, service, and (if it exists) colloquial/"friendly" name of the device.

Note that the Registry actually lists these attributes for each separate time ("instance") that the device was plugged in. Therefore, if any device has been connected to the PC more than once, its information will appear in the final outputs more than once. Such duplicates can be ignored or removed. I considered having the program only print the attributes for each device once, but it occured to me that I am not certain if the data belonging to each instance may be different; many of the attributes are present in some devices but not in others, which raises the possibility that such attributes may be present in some instances of one device, but not in others. Therefore, I decided to have the program print the attributes for each individual instance, just to ensure that all desired information would be attained, if it is present.
