# Vetinet Write Up

## Challenge Information
  Welcome to Vertinet.

  This problem follows the same specifications as the previous Verticode problem, except that you have to solve many of them by developing a client to communicate with the server available at problems1.2016q1.sctf.io:50000. Good luck.

## Background
  ########################################################## <br />
  # SCTF 2016 Quarter 1 Verticode Challenge                # <br />
  ########################################################## <br />
  # Image Format:                                          # <br />
  #                                                        # <br />
  #           Color        Black and White Colors      (y) # <br />
  #       |____________|____________________________|  _0  # <br />
  #       |____________|____|___|___|___|___|___|___|  _12 # <br />
  #       |____________|____|___|___|___|___|___|___|  _24 # <br />
  #       |____________|____|___|___|___|___|___|___|  _36 # <br />
  #       |____________|____|___|___|___|___|___|___|      # <br />
  # (x)   0            84   96 108 120 132 144 156 168     # <br />
  ########################################################## <br />
  # Image Calculations:                                    # <br />
  #                                                        # <br />
  # Colors: Red    => 0                                    # <br />
  #         Purple => 1                                    # <br />
  #         Blue   => 2                                    # <br />
  #         Green  => 3                                    # <br />
  #         Yellow => 4                                    # <br />
  #         Orange => 5                                    # <br />
  #                                                        # <br />
  #         White =>  0                                    # <br />
  #         Black =>  1                                    # <br />
  #                                                        # <br />
  #         * Color Value is added to the binary value of  # <br />
  #         the black and white portion of each line       # <br />
  #                                                        # <br />
  #         * Black and White squares correspond to a      # <br />
  #         binary value, so:                              # <br />
  #                                                        # <br />
  #         Squares = 1000001                              # <br />
  #         Decimal = 65                                   # <br />
  #         ASCII   = A                                    # <br />
  #                                                        # <br />
  #         * The colors have an associated value, so:     # <br />
  #                                                        # <br />
  #         Purple  = 1                                    # <br />
  #         Squares = 1000001 => 65 => A                   # <br />
  #         Purple + Squares = 1000010 => 66 = B           # <br />
  #                                                        # <br />
  #         So the new value of the line is B              # <br />
  ########################################################## <br />
`
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
