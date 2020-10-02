#!/usr/bin/env python3


import os
import json
import sys
import re


# SAMPLE TMSH SHOW SYS LICENSE FORMAT (STDOUT_LINES) BELOW

# [
#     [
#         "Sys::License",
#         "Licensed Version                       15.1.0",
#         "Registration key                       W5842-34609-82388-12435-0981557",
#         "Licensed On                            2020/09/20",
#         "License Start Date                     2020/09/19",
#         "License End Date                       2020/10/21",
#         "Service Check Date                     2020/09/20",
#         "Platform ID                            Z100",
#         "Daily Renewal Notification Days        5",
#         "Daily Renewal Notification Start Date  2020/10/16",
#         "Permitted Versions                     5.*.* - 18.*.*",
#         "",
#         "Active Modules",
#         "  GTM-DNS, RL, BIG-IP (v11.4 & later) (M851928-1854326)",
#         "    GTM-DNS, RL, BIG-IP (v11.4 & later)",
#         "  LTM, Lab, VE (Y511655-4264505)",
#         "    IPV6 Gateway",
#         "    Rate Shaping",
#         "    Client Authentication",
#         "    Application Acceleration Manager, Core",
#         "    SSL, VE",
#         "    Recycle, BIG-IP, VE",
#         "    APM, Limited",
#         "    Max Compression, VE",
#         "    Ram Cache",
#         "    Enable all versions",
#         "    Anti-Virus Checks",
#         "    Base Endpoint Security Checks",
#         "    Firewall Checks",
#         "    Machine Certificate Checks",
#         "    Network Access",
#         "    Protected Workspace",
#         "    Secure Virtual Keyboard",
#         "    APM, Web Application",
#         "    App Tunnel",
#         "    Remote Desktop",
#         "    LTM, Lab, VE"
#     ]
# ]

REG_KEY_PREFIX = 'Registration key'
LIC_ON_PREFIX = 'Licensed On'
LIC_START_DATE_PREFIX = 'License Start Date'
LIC_END_DATE_PREFIX = 'License End Date'
SER_CHECK_DATE_PREFIX = 'Service Check Date'

license_info = {}
add_on_list = []

addOnKeyPattern = re.compile("\w{7}[-]\w{7}")

#curr_dir = os.getcwd()

lic_file = sys.argv[1]
lic_keys_file = 'lic_keys.json'


with open(lic_file, 'r') as in_file:
    for lineNum, line in enumerate(in_file, 1):
        if REG_KEY_PREFIX in line:
            reg_key = line.split()[2].strip('\t\n,"')
            license_info['reg_key'] = reg_key
        if LIC_ON_PREFIX in line:
            lic_on = line.split()[2].strip('\t\n,"')
            license_info['lic_on'] = lic_on
        if LIC_START_DATE_PREFIX in line:
            lic_start = line.split()[3].strip('\t\n,"')
            license_info['lic_start'] = lic_start
        if LIC_END_DATE_PREFIX in line:
            lic_end = line.split()[3].strip('\t\n,"')
            license_info['lic_end'] = lic_end
        if SER_CHECK_DATE_PREFIX in line:
            ser_check = line.split()[3].strip('\t\n,"')
            license_info['ser_check'] = ser_check
        if bool(addOnKeyPattern.search(line)):
            addon_key = ''
            addon_key = line.split()[-1].strip('\t\n,"\(\))')
            add_on_list.append(addon_key)
    license_info['addon_keys'] = add_on_list

with open(lic_keys_file, 'w') as out_file:
    json.dump(license_info, out_file)
