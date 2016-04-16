#!/usr/bin/python

##########################################################
# Synopsis:                                              #
#                                                        #
# SCTF 2016 Quarter 1 Verticode Challenge                #
##########################################################
# Image Format:                                          #
#                                                        #
#           Color        Black and White Colors      (y) #
#       |____________|____________________________|  _0  #
#       |____________|____|___|___|___|___|___|___|  _12 #
#       |____________|____|___|___|___|___|___|___|  _24 #
#       |____________|____|___|___|___|___|___|___|  _36 #
#       |____________|____|___|___|___|___|___|___|      #
# (x)   0            84   96 108 120 132 144 156 168     #
##########################################################
# Image Calculations:                                    #
#                                                        #
# Colors: Red    => 0                                    #
#         Purple => 1                                    #
#         Blue   => 2                                    #
#         Green  => 3                                    #
#         Yellow => 4                                    #
#         Orange => 5                                    #
#                                                        #
#         White =>  0                                    #
#         Black =>  1                                    #
#                                                        #
#         * Color Value is added to the binary value of  #
#         the black and white portion of each line       #
#                                                        #
#         * Black and White squares correspond to a      #
#         binary value, so:                              #
#                                                        #
#         Squares = 1000001                              #
#         Decimal = 65                                   #
#         ASCII   = A                                    #
#                                                        #
#         * The colors have an associated value, so:     #
#                                                        #
#         Purple  = 1                                    #
#         Squares = 1000001 => 65 => A                   #
#         Purple + Squares = 1000010 => 66 = B           #
#                                                        #
#         So the new value of the line is B              #
##########################################################

# Import socket
import socket

# Import re
import re

# Import base64
import base64

# Import Image Library from PIL
from PIL import Image

# Function to Convert RGB Values to Hex
def rgb2hex(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(r, g, b)

# Function to Convert RGB Hex Value to Incremental Value
def getColor(hexVal):
    pixVal = ""

    if hexVal == "ff0000":
        # Red
        pixVal = 0
    elif hexVal == "800080":
        # Purple
        pixVal = 1
    elif hexVal == "0000ff":
        # Blue
        pixVal = 2
    elif hexVal == "008000":
        # Green
        pixVal = 3
    elif hexVal == "ffff00":
        # Yellow
        pixVal = 4
    elif hexVal == "ffa500":
        # Orange
        pixVal = 5
    elif hexVal == "ffffff":
        # White
        pixVal = 0
    elif hexVal == "000000":
        # Black
        pixVal = 1 
    else:
        # No Color
        print "Error: Color not Found!"

    return pixVal

def getString(getImg, imgWidth, imgHeight, rgbImg, binArr, flagStringArr):
    # Loop through Image height in increments of 12 pixels
    for y in xrange(0, imgHeight, 12):
        for x in xrange(84, imgWidth, 12):
             # Start Get Color Values #

             # Get Color Hex Value
             r, g, b = rgbImg.getpixel((0, y))
        
             # Get Color Value
             hexVal = rgb2hex(r, g, b)
             pixVal = getColor(hexVal)

             binColor = pixVal

             # Start Black and White Colors #

             # Get Black and White Hex Values
             r, g, b = rgbImg.getpixel((x, y))

             # Get Binary Value of Black and White Colors
             binHexVal = rgb2hex(r, g, b)
             binVal = getColor(binHexVal)

             # Append Binary Value to Array
             binArr.append(binVal)

             # Just to be sure, Make sure binary string is 
             # at 7 characters (Only 7 Black and White Cubes
             # in the image
             if len(binArr) == 7:
                 # Set binary length to 8
                 binary = "0" + ''.join(str(x) for x in binArr)

                 # Reset binArr now that we have a full binary 
                 # value
                 binArr = []
             else:
                 # If we don't have a full 7 bits, continue
                 continue

             # Convert binary value to decimal and add the 
             # color value 
             binNewVal = int(binary, 2) + binColor

             # Append ASCII character to flagStringArr
             flagStringArr.append(chr(binNewVal))

    # Print the flag value
    # Flag is not in the standard sctf{XXXXX} format
    # The Flag should be easily found within the output
    return ''.join(str(x) for x in flagStringArr)

def Main():
    while True:
        # Start Connection to Website
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("problems1.2016q1.sctf.io", 50000))

        # Get Response from Web Page
        resp = sock.recv(90000)
        print "Getting Socket Information:"
        print resp

        # Parse Response for base64 encoded image
        imgTag = re.findall('.?', resp)
        imgB64 = ''.join(str(x) for x in imgTag[38:len(imgTag) - 9])

        # Decode Image base64
        rawImg = base64.b64decode(imgB64)

        # Save Decoded Image to image.png
        with open("image.png", 'wb') as imgFile:
            imgFile.write(rawImg)

        # Load Image
        getImg = Image.open('image.png')

        # Get Image Size
        imgWidth, imgHeight = getImg.size

        # Convert Image to RGB
        rgbImg = getImg.convert('RGB')

        # Empty Array for Binary Values
        binArr = []

        # Empty Array of Decoded Values (Flag)
        flagStringArr = []

        # Get Decoded Flag Value from Image
        flagStr = getString(getImg, imgWidth, imgHeight, rgbImg, binArr, flagStringArr)

        print "Printing flagStr value:"
        print flagStr  

        # Send Decoded Flag Value to Web Page
        sock.send(flagStr)

        # Get Website Response
        print sock.recv(1024)

if __name__ == '__main__':
    Main()
