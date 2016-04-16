# Vetinet Write Up

## Challenge Information
  Welcome to Vertinet.

  This problem follows the same specifications as the previous Verticode problem, except that you have to solve many of them by developing a client to communicate with the server available at problems1.2016q1.sctf.io:50000. Good luck.

## Background
  ##########################################################
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

## Requirements
  - Python Imaging Library (PIL)
  - Python re 
  - Python socket
  - Python base64

## Included Files
  - vertinet.py, vertinet python implementation

## HowTo
  - `python vertinet.py`

## Notes
  - I wanted to share this code with others, but I did not actually solve this challenge. This code is not 100% and I did not have time to correct it, in order solve the challenge. However, I wanted to include the code, in the event that somebody would like to have a baseline/potential solution to solving this challenge. The majority of this code was based off of the Veticode challenge code. This code connects to `problems1.2016q1.sctf.io` on port `50000` and attempts to read in the base64 encoded image and run it through the verticode code. Then, it attempts to submit the answer to the web page and get back the response.
