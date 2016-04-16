# Vetinet Write Up

## Challenge Information
  Welcome to Vertinet.

  This problem follows the same specifications as the previous Verticode problem, except that you have to solve many of them by developing a client to communicate with the server available at problems1.2016q1.sctf.io:50000. Good luck.

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
