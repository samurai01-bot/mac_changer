#! /usr/bin/env python
#MAC-address_Default = 50:e5:49:e3:d4:4f
import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_MAC", help="New Mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_MAC:
        parser.error("[-] Please specify a new MAC address, use --help for more info.")
    return options



def change_mac(interface, new_MAC):
    print("[+] Change MAC address for " + interface + " to " + new_MAC)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_MAC])
    subprocess.call(["ifconfig", interface, "up"])
    
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface]).decode()
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result: 
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
#change_mac(options.interface, options.new_MAC)

