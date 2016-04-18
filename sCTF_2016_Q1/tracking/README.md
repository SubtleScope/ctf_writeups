# Tracking Write Up

## Synopsis
  GPS satellites use trilateration. You must do something similar to the equations listed on the trilateration Wikipedia page. Take the average of the x, y, and z values to get the flag. Please see the tracking.in and description.txt files.

## Hint
  Flag should be submitted in sctf{x, y, z} format

## Requirements
  - math (ceil and sqrt)

## Files
  - coord.py, python script to perform the calculations
  - coords.txt, d1 through d4 values
  - tracking.in, data used for calculations
  - description.txt, challenge description

## Notes
  - I did not solve this challenge, but wanted to share it anyway.
  - You need the equations to solve for the four distances (radii) 

## Solution (unsolved)
  - $ `./coord.py`
  - Output: <br />
    .... <br />
    sctf{536.0, 1000.0, 976.0}
