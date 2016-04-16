# Veticode Write Up

## Challenge Information
  Welcome to Verticode, the new method of translating text into vertical codes.

  Each verticode has two parts: the color shift and the code.

  The code takes the inputted character and translates it into an ASCII code, and then into binary, then puts that into an image in which each black pixel represents a 1 and each white pixel represents a 0.

  For example, A is 65 which is 1000001 in binary, B is 66 which is 1000010, and C is 67 which is 1000011, so the corresponding verticode would look like this.

  Except, it isn't that simple.

  A color shift is also integrated, which means that the color before each verticode shifts the ASCII code, by adding the number that the color corresponds to, before translating it into binary. In that case, the previous verticode could also look like this.

  The table for the color codes is:

    0 = Red
    1 = Purple
    2 = Blue
    3 = Green
    4 = Yellow
    5 = Orange

  This means that a red color shift for the letter A, which is 65 + 0 = 65, would translate into 1000001 in binary; however, a green color shift for the letterA, which is 65 + 3 = 68, would translate into 1000100 in binary.

  Given this verticode, read the verticode into text and find the flag.

  Note that the flag will not be in the typical sctf{flag} format, but will be painfully obvious text. Once you find this text, you will submit it in thesctf{text} format. So, if the text you find is adunnaisawesome, you will submit it as sctf{adunnaisawesome}.

## Hint
  You might want to look at imaging libraries

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
  - Python Imaging Library

## Included Files
  - verticode.py, verticode python implementation
  - verticode_debug.py, verticode python implementation with print statements
  - code1.png, the main file containing the flag
  - A-Code.png, a test image, with just the black and white porton
  - B-Code.png, a test image, with the color blocks andwhite and black squares

## HowTo
  - Ensure that code1.png and verticode.py are in the same directory
  - `python verticode.py`
  - Output:
    RygNqvq�gskwkrulqknltimvi|emkt|ursz~y|it}vgexjnaj~nkkyap~uhgewooxji�szpjune{~k}zvgrkrrqvoicxe|ZroyinPwpspizetsvexonjcuocth�}sgshictoaxencvetowmqxkmctcjvmofyiihvmnk|powsgtvoy|jkorqxepapmgnylkvidqwitganoypskrt�ekzsiygyTqoRwtsqgofk{~|y}mhapkrgkjo{rjircnh{}mn~je{rk~tmxgd|kwaivytsnyzmgqkhxsuiprsvkvuksznkz}~vynkve}emllohzin�gzke~}vm{lesvgyxrini~enzozlgtkrhtiaHitnegkf|hkwivcisreyvaxvivzmvn~qjsvugysrvyhwj|ixoctntpcgmjxnmvkvi{ewpemnzhisofltkopozJgxrmtepkrvgtkdvrezkryj|rmwxwre}exivllmeyspzstlktknksiwrkzqvoe�|lmxwwgxqnvrkroc~or{Ho�g{irizxanki�k|rvjmhmc}t�uf~pow|itisjmsixymuterhnqjt~k|gnxw|miktpi~gz}tg|gmxsrralwheajopkxu{crhposTrkwlvspi�asyyqkmr{jmqutqujofenfvpmmqumjia~k}ovnhxa{vunvqwmt}gnvLukLqhoknxyetgmxwfrm|ghbpacotiysjq}nn|ohoizevcvpetlmqov}iyrzne~cuKFMkgmxrmpniiinpvs}ovci{epwpwomFGNct�uxmyhuykjox{|vcuodmogtwqxjTglono{stjSLgxlQ|wfkeswetaznotyvioojoxvefreNqo}ewcpuswudfgxv}qrvvokgjzwwtj|wkngokxqkorsovrkuqukkq}{ytjkmcegn~vmc~azeyo|s}szla{|xqvmqqrxskevamkir~Mq}njzsivgme|qgovyuzjc}m{eio}{�xpmgmcktvziizipstuQlsmgtiz~csqrq�ati{enoinOpi~grsonoi}iknNwo

## Notes
  - I wanted to share this code with others, but I did not actually solve this challenge. This code is not 100% and I did not have time to correct it, in order solve the challenge. However, I wanted to include the code, in the event that somebody would like to have a baseline/potential solution to solving this challenge.