# Secure Text Saver Jar Write Up

## Synopsis
  A simple program to save text and retrieve it later

## Background
  Find the flag.

## Software
  I used Luyten to get the java code from the class files contained in the Secure_Text_Saver.jar file

## Solution
  - > `luyten-0.4.5.jar`
  - File -> Open File -> Secure_Text_Saver.jar
  - Select Login_Page.class
  - Login_Page.accounts.add(new Account("ztaylor54", "]!xME}behA8qjM~T".toCharArray()));
  - > `Secure_Text_Saver.jar`
  - Enter the username and password
  - Flag: sctf{w0w_th4t_w45_pr377y_e45y}
  - Solution: <br />
    ![Solution](SecureTextSaver_Solution.jpg?raw=true "Solution") <br />
