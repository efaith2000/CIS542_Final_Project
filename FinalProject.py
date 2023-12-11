# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""


#Written by Eric Faith
#December 9, 2023
#CIS 542 - Digital Forensics


import winreg

from winreg import (
  ConnectRegistry,
  OpenKey,
  KEY_ALL_ACCESS,
  EnumValue,
  QueryInfoKey,
  HKEY_LOCAL_MACHINE,
  HKEY_CURRENT_USER,
  CloseKey,
  EnumKey
)

def main():
    folderUSB = winreg.OpenKey(HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Enum\USB')
    
    i=0
    j=0
    k=0
    while(True):
        try:
            deviceName = EnumKey(folderUSB, i) 
            deviceOpen = winreg.OpenKey(folderUSB, deviceName)                                      #get i-th key in USB folder (represents a device)
            while(True):
                try:
                    instanceName = EnumKey(deviceOpen, j)                                                   #get j-th key in device i folder (represents an instance of device being plugged in)
                    instanceOpen = winreg.OpenKey(deviceOpen, instanceName)
                    while(True):
                        try:
                            attribute = EnumValue(instanceOpen, k)                                                  #iterate through each attribute k of instance j of device i
                            if attribute[0] in ['FriendlyName', 'HardwareID', 'Mfg', 'Service']:                            #check if attribute k is one of the four attributes we want to print
                                print(attribute[0], ": ", attribute[1])                                                             #if so, print the name and data for that attribute
                            k+=1                                                                                            #increment k by 1 (will be looking at next attribute for instance j of item i)
                        except WindowsError:
                            break
                    print("\n\n\n")
                    CloseKey(instanceOpen)                                                                          #close key for instance j
                    k=0                                                                                             #reset k to 0 (will be looking at attributes for next instance of device i)
                    j+=1                                                                                            #increment j by 1, to look at next instance for device
                except WindowsError:
                    break
            print()
            CloseKey(deviceOpen)                                                                           #close key for device i
            j=0                                                                                            #reset j to 0 (will be looking at instances of next device)
            i+=1                                                                                           #increment i by 1, to look at next device
        except WindowsError:
            break
    CloseKey(folderUSB)                                                                             #close key for USB folder, once all items have been examined

    
       
main()
