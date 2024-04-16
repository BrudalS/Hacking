#!bin/usr/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()  # parser is an object and OptionParser is an class
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change its mack address")  # dest is the variable storage
    parser.add_option("-m", "--mac", dest="mac_new", help="New mac address")
    (options, agruments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.mac_new:
        parser.error("[-] Please specify an interface, use --help for more info")
    return options


def change_mac(interface, mac_new):
    print("[+] Changing MAC address for " + interface + " to " + mac_new)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_new])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not get mac address")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.mac_new)

current_mac = get_current_mac(options.interface)
if current_mac == options.mac_new:
    print("[+] MAC address was sucessfully changed to " + str(current_mac))
else:
    print("[+] The MAc address did not change")