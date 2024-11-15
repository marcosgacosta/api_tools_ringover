# Project Title

Ringover API Tools for Support

## Description

These scripts are created to automate some of the support tasks we have.
* api_bulkteamdnc_add.py - Add numbers to the blocklist from a list.
* api_bulkteamdnc_remove.py - Remove numbers to the blocklist from a list.
* api_currentcalls.py - Find the call ID of the current calls.

## Getting Started

### Executing program

* All scripts require the creation of an API Key with the corresponding permissions.
* The api_bulkteamdnc_add.py and the api_bulkteamdnc_remove.py requires a file named numbers.csv containing the list of numbers that are gonna be added/removed from the blocklist.
* The list of numbers in numbers.csv should be using the e.164 format without the '+'. i.e: 15742922031

## Authors

Marcos Acosta - marcos.acosta@ringover.com

## Version History

* 0.1
    * Initial Release
