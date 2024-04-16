#!bin/usr/env python

import subprocess
import optparse

parser = optparse.OptionParser()  #  parser is an object and OptionParser is an class

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mack address") #  dest is the variable storage
parser.add_option("-m", "--mac", dest="mac_new", help="New mac address")

(options, arguments) = parser.parse_args()

interface = options.interface
mac_new = options.mac_new

print("[+] Changing MAC address for " + interface + " to " + mac_new)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac_new])
subprocess.call(["ifconfig", interface, "up"])
