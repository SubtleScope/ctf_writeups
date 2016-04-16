# Cookie Jar Write Up

## Synopsis
  My mom put a password on the cooie jar

## Background
  Find the flag.

## Software
  I used Luyten to get the java code from the class files contained in the cookie.jar file

## Solution
  - > `luyten-0.4.5.jar`
  - File -> Open File -> cookie.jar
  - Select Cookie.class
  - answer = "fdf87a05e2169b88a8db5a1ebc15fa50";
  - Crack the md5 hash and you get: thisisaverystrongpassword
  - >`cookie.jar`
  - Enter the password
  - Flag: sctf{g3t_y0ur_h4nd_0ut_0f_my_c00k13_j4r!}
  - Solution: <br />
    ![Solution](CookieJar_Solution.jpg?raw=true "Solution") <br />
