#!/bin/bash

opkg update
opkg install python-light
opkg install python-logging
opkg install python-openssl
#for url encoding
opkg install python-codecs
