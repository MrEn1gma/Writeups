@shift /0
@echo off
title UMD-CTF : Old School : RingZer0 Team
color 17
mode con cols=80 lines=25
set b1=
set b2=
set b3=
set b4=
set b5=
set b6=
set b7=
set b8=
set b9=
set b10=
cls
echo ษออออออออออออออออออออออป
echo บ Type your access key บ
echo ศออออออออออออออออออออออผ
echo.
set pass=
set /p pass=ฏ 
if not defined pass goto bad
set #=%pass%
set length=0
:l
if defined # (set #=%#:~1%&set /A length += 1&goto l)
if not %length%==10 (goto bad)
set out=
set n=0
:ll
call set t=%%pass:~%n%,1%%%
set /a n+=1
if defined t (set out=%t%%out%&goto :ll)
set pass=%out%
set b1=%pass:~0,1%
set b2=%pass:~1,1%
set b3=%pass:~2,1%
set b4=%pass:~3,1%
set b5=%pass:~4,1%
set b6=%pass:~5,1%
set b7=%pass:~6,1%
set b8=%pass:~7,1%
set b9=%pass:~8,1%
set b10=%pass:~9,1%
set pass=%pass:~0,10%
set pass=%pass:~0,10%
if %b1%==0 set b1=0000
if %b1%==1 set b1=0001
if %b1%==2 set b1=0010
if %b1%==3 set b1=0011
if %b1%==4 set b1=0100
if %b1%==5 set b1=0101
if %b1%==6 set b1=0110
if %b1%==7 set b1=0111
if %b1%==8 set b1=1000
if %b1%==9 set b1=1001
if %b1%==A set b1=1010
if %b1%==B set b1=1011
if %b1%==C set b1=1100
if %b1%==D set b1=1101
if %b1%==E set b1=1110
if %b1%==F set b1=1111
if %b2%==0 set b2=0000
if %b2%==1 set b2=0001
if %b2%==2 set b2=0010
if %b2%==3 set b2=0011
if %b2%==4 set b2=0100
if %b2%==5 set b2=0101
if %b2%==6 set b2=0110
if %b2%==7 set b2=0111
if %b2%==8 set b2=1000
if %b2%==9 set b2=1001
if %b2%==A set b2=1010
if %b2%==B set b2=1011
if %b2%==C set b2=1100
if %b2%==D set b2=1101
if %b2%==E set b2=1110
if %b2%==F set b2=1111
if %b3%==0 set b3=0000
if %b3%==1 set b3=0001
if %b3%==2 set b3=0010
if %b3%==3 set b3=0011
if %b3%==4 set b3=0100
if %b3%==5 set b3=0101
if %b3%==6 set b3=0110
if %b3%==7 set b3=0111
if %b3%==8 set b3=1000
if %b3%==9 set b3=1001
if %b3%==A set b3=1010
if %b3%==B set b3=1011
if %b3%==C set b3=1100
if %b3%==D set b3=1101
if %b3%==E set b3=1110
if %b3%==F set b3=1111
if %b4%==0 set b4=0000
if %b4%==1 set b4=0001
if %b4%==2 set b4=0010
if %b4%==3 set b4=0011
if %b4%==4 set b4=0100
if %b4%==5 set b4=0101
if %b4%==6 set b4=0110
if %b4%==7 set b4=0111
if %b4%==8 set b4=1000
if %b4%==9 set b4=1001
if %b4%==A set b4=1010
if %b4%==B set b4=1011
if %b4%==C set b4=1100
if %b4%==D set b4=1101
if %b4%==E set b4=1110
if %b4%==F set b4=1111
if %b5%==0 set b5=0000
if %b5%==1 set b5=0001
if %b5%==2 set b5=0010
if %b5%==3 set b5=0011
if %b5%==4 set b5=0100
if %b5%==5 set b5=0101
if %b5%==6 set b5=0110
if %b5%==7 set b5=0111
if %b5%==8 set b5=1000
if %b5%==9 set b5=1001
if %b5%==A set b5=1010
if %b5%==B set b5=1011
if %b5%==C set b5=1100
if %b5%==D set b5=1101
if %b5%==E set b5=1110
if %b5%==F set b5=1111
if %b6%==0 set b6=0000
if %b6%==1 set b6=0001
if %b6%==2 set b6=0010
if %b6%==3 set b6=0011
if %b6%==4 set b6=0100
if %b6%==5 set b6=0101
if %b6%==6 set b6=0110
if %b6%==7 set b6=0111
if %b6%==8 set b6=1000
if %b6%==9 set b6=1001
if %b6%==A set b6=1010
if %b6%==B set b6=1011
if %b6%==C set b6=1100
if %b6%==D set b6=1101
if %b6%==E set b6=1110
if %b6%==F set b6=1111
if %b7%==0 set b7=0000
if %b7%==1 set b7=0001
if %b7%==2 set b7=0010
if %b7%==3 set b7=0011
if %b7%==4 set b7=0100
if %b7%==5 set b7=0101
if %b7%==6 set b7=0110
if %b7%==7 set b7=0111
if %b7%==8 set b7=1000
if %b7%==9 set b7=1001
if %b7%==A set b7=1010
if %b7%==B set b7=1011
if %b7%==C set b7=1100
if %b7%==D set b7=1101
if %b7%==E set b7=1110
if %b7%==F set b7=1111
if %b8%==0 set b8=0000
if %b8%==1 set b8=0001
if %b8%==2 set b8=0010
if %b8%==3 set b8=0011
if %b8%==4 set b8=0100
if %b8%==5 set b8=0101
if %b8%==6 set b8=0110
if %b8%==7 set b8=0111
if %b8%==8 set b8=1000
if %b8%==9 set b8=1001
if %b8%==A set b8=1010
if %b8%==B set b8=1011
if %b8%==C set b8=1100
if %b8%==D set b8=1101
if %b8%==E set b8=1110
if %b8%==F set b8=1111
if %b9%==0 set b9=0000
if %b9%==1 set b9=0001
if %b9%==2 set b9=0010
if %b9%==3 set b9=0011
if %b9%==4 set b9=0100
if %b9%==5 set b9=0101
if %b9%==6 set b9=0110
if %b9%==7 set b9=0111
if %b9%==8 set b9=1000
if %b9%==9 set b9=1001
if %b9%==A set b9=1010
if %b9%==B set b9=1011
if %b9%==C set b9=1100
if %b9%==D set b9=1101
if %b9%==E set b9=1110
if %b9%==F set b9=1111
if %b10%==0 set b10=0000
if %b10%==1 set b10=0001
if %b10%==2 set b10=0010
if %b10%==3 set b10=0011
if %b10%==4 set b10=0100
if %b10%==5 set b10=0101
if %b10%==6 set b10=0110
if %b10%==7 set b10=0111
if %b10%==8 set b10=1000
if %b10%==9 set b10=1001
if %b10%==A set b10=1010
if %b10%==B set b10=1011
if %b10%==C set b10=1100
if %b10%==D set b10=1101
if %b10%==E set b10=1110
if %b10%==F set b10=1111
set binary=%b1%%b2%%b3%%b4%%b5%%b6%%b7%%b8%%b9%%b10%
set A=%binary:~0,1%
set B=%binary:~1,1%
set C=%binary:~2,1%
set D=%binary:~3,1%
set E=%binary:~4,1%
set F=%binary:~5,1%
set G=%binary:~6,1%
set H=%binary:~7,1%
set I=%binary:~8,1%
set J=%binary:~9,1%
set K=%binary:~10,1%
set L=%binary:~11,1%
set M=%binary:~12,1%
set N=%binary:~13,1%
set Z=%binary:~14,1%
set P=%binary:~15,1%
set Q=%binary:~16,1%
set R=%binary:~17,1%
set S=%binary:~18,1%
set T=%binary:~19,1%
set U=%binary:~20,1%
set V=%binary:~21,1%
set W=%binary:~22,1%
set X=%binary:~23,1%
set AA=%binary:~24,1%
set BB=%binary:~25,1%
set CC=%binary:~26,1%
set DD=%binary:~27,1%
set EE=%binary:~28,1%
set FF=%binary:~29,1%
set GG=%binary:~30,1%
set HH=%binary:~31,1%
set II=%binary:~32,1%
set JJ=%binary:~33,1%
set KK=%binary:~34,1%
set LL=%binary:~35,1%
set MM=%binary:~36,1%
set NN=%binary:~37,1%
set ZZ=%binary:~38,1%
set PP=%binary:~39,1%
set F1=%II%%JJ%%KK%%LL%%MM%
set F2=%NN%%ZZ%%PP%%I%%J%
set F3=%K%%L%%M%%N%%Z%
set F4=%P%%A%%B%%C%%D%
set F5=%E%%F%%G%%H%%dd%
set F6=%EE%%FF%%GG%%HH%%AA%
set F7=%BB%%CC%%Q%%R%%S%
set F8=%T%%U%%V%%W%%X%
if %F1%==00000 set F1=A
if %F1%==00001 set F1=B
if %F1%==00010 set F1=C
if %F1%==00011 set F1=D
if %F1%==00100 set F1=E
if %F1%==00101 set F1=F
if %F1%==00110 set F1=G
if %F1%==00111 set F1=H
if %F1%==01000 set F1=J
if %F1%==01001 set F1=K
if %F1%==01010 set F1=L
if %F1%==01011 set F1=M
if %F1%==01100 set F1=N
if %F1%==01101 set F1=P
if %F1%==01110 set F1=R
if %F1%==01111 set F1=S
if %F1%==10000 set F1=T
if %F1%==10001 set F1=V
if %F1%==10010 set F1=W
if %F1%==10011 set F1=X
if %F1%==10100 set F1=Y
if %F1%==10101 set F1=Z
if %F1%==10110 set F1=0
if %F1%==10111 set F1=1
if %F1%==11000 set F1=2
if %F1%==11001 set F1=3
if %F1%==11010 set F1=4
if %F1%==11011 set F1=5
if %F1%==11100 set F1=6
if %F1%==11101 set F1=7
if %F1%==11110 set F1=8
if %F1%==11111 set F1=9
if %F2%==00000 set F2=A
if %F2%==00001 set F2=B
if %F2%==00010 set F2=C
if %F2%==00011 set F2=D
if %F2%==00100 set F2=E
if %F2%==00101 set F2=F
if %F2%==00110 set F2=G
if %F2%==00111 set F2=H
if %F2%==01000 set F2=J
if %F2%==01001 set F2=K
if %F2%==01010 set F2=L
if %F2%==01011 set F2=M
if %F2%==01100 set F2=N
if %F2%==01101 set F2=P
if %F2%==01110 set F2=R
if %F2%==01111 set F2=S
if %F2%==10000 set F2=T
if %F2%==10001 set F2=V
if %F2%==10010 set F2=W
if %F2%==10011 set F2=X
if %F2%==10100 set F2=Y
if %F2%==10101 set F2=Z
if %F2%==10110 set F2=0
if %F2%==10111 set F2=1
if %F2%==11000 set F2=2
if %F2%==11001 set F2=3
if %F2%==11010 set F2=4
if %F2%==11011 set F2=5
if %F2%==11100 set F2=6
if %F2%==11101 set F2=7
if %F2%==11110 set F2=8
if %F2%==11111 set F2=9
if %F3%==00000 set F3=A
if %F3%==00001 set F3=B
if %F3%==00010 set F3=C
if %F3%==00011 set F3=D
if %F3%==00100 set F3=E
if %F3%==00101 set F3=F
if %F3%==00110 set F3=G
if %F3%==00111 set F3=H
if %F3%==01000 set F3=J
if %F3%==01001 set F3=K
if %F3%==01010 set F3=L
if %F3%==01011 set F3=M
if %F3%==01100 set F3=N
if %F3%==01101 set F3=P
if %F3%==01110 set F3=R
if %F3%==01111 set F3=S
if %F3%==10000 set F3=T
if %F3%==10001 set F3=V
if %F3%==10010 set F3=W
if %F3%==10011 set F3=X
if %F3%==10100 set F3=Y
if %F3%==10101 set F3=Z
if %F3%==10110 set F3=0
if %F3%==10111 set F3=1
if %F3%==11000 set F3=2
if %F3%==11001 set F3=3
if %F3%==11010 set F3=4
if %F3%==11011 set F3=5
if %F3%==11100 set F3=6
if %F3%==11101 set F3=7
if %F3%==11110 set F3=8
if %F3%==11111 set F3=9
if %F4%==00000 set F4=A
if %F4%==00001 set F4=B
if %F4%==00010 set F4=C
if %F4%==00011 set F4=D
if %F4%==00100 set F4=E
if %F4%==00101 set F4=F
if %F4%==00110 set F4=G
if %F4%==00111 set F4=H
if %F4%==01000 set F4=J
if %F4%==01001 set F4=K
if %F4%==01010 set F4=L
if %F4%==01011 set F4=M
if %F4%==01100 set F4=N
if %F4%==01101 set F4=P
if %F4%==01110 set F4=R
if %F4%==01111 set F4=S
if %F4%==10000 set F4=T
if %F4%==10001 set F4=V
if %F4%==10010 set F4=W
if %F4%==10011 set F4=X
if %F4%==10100 set F4=Y
if %F4%==10101 set F4=Z
if %F4%==10110 set F4=0
if %F4%==10111 set F4=1
if %F4%==11000 set F4=2
if %F4%==11001 set F4=3
if %F4%==11010 set F4=4
if %F4%==11011 set F4=5
if %F4%==11100 set F4=6
if %F4%==11101 set F4=7
if %F4%==11110 set F4=8
if %F4%==11111 set F4=9
if %F5%==00000 set F5=A
if %F5%==00001 set F5=B
if %F5%==00010 set F5=C
if %F5%==00011 set F5=D
if %F5%==00100 set F5=E
if %F5%==00101 set F5=F
if %F5%==00110 set F5=G
if %F5%==00111 set F5=H
if %F5%==01000 set F5=J
if %F5%==01001 set F5=K
if %F5%==01010 set F5=L
if %F5%==01011 set F5=M
if %F5%==01100 set F5=N
if %F5%==01101 set F5=P
if %F5%==01110 set F5=R
if %F5%==01111 set F5=S
if %F5%==10000 set F5=T
if %F5%==10001 set F5=V
if %F5%==10010 set F5=W
if %F5%==10011 set F5=X
if %F5%==10100 set F5=Y
if %F5%==10101 set F5=Z
if %F5%==10110 set F5=0
if %F5%==10111 set F5=1
if %F5%==11000 set F5=2
if %F5%==11001 set F5=3
if %F5%==11010 set F5=4
if %F5%==11011 set F5=5
if %F5%==11100 set F5=6
if %F5%==11101 set F5=7
if %F5%==11110 set F5=8
if %F5%==11111 set F5=9
if %F6%==00000 set F6=A
if %F6%==00001 set F6=B
if %F6%==00010 set F6=C
if %F6%==00011 set F6=D
if %F6%==00100 set F6=E
if %F6%==00101 set F6=F
if %F6%==00110 set F6=G
if %F6%==00111 set F6=H
if %F6%==01000 set F6=J
if %F6%==01001 set F6=K
if %F6%==01010 set F6=L
if %F6%==01011 set F6=M
if %F6%==01100 set F6=N
if %F6%==01101 set F6=P
if %F6%==01110 set F6=R
if %F6%==01111 set F6=S
if %F6%==10000 set F6=T
if %F6%==10001 set F6=V
if %F6%==10010 set F6=W
if %F6%==10011 set F6=X
if %F6%==10100 set F6=Y
if %F6%==10101 set F6=Z
if %F6%==10110 set F6=0
if %F6%==10111 set F6=1
if %F6%==11000 set F6=2
if %F6%==11001 set F6=3
if %F6%==11010 set F6=4
if %F6%==11011 set F6=5
if %F6%==11100 set F6=6
if %F6%==11101 set F6=7
if %F6%==11110 set F6=8
if %F6%==11111 set F6=9
if %F7%==00000 set F7=A
if %F7%==00001 set F7=B
if %F7%==00010 set F7=C
if %F7%==00011 set F7=D
if %F7%==00100 set F7=E
if %F7%==00101 set F7=F
if %F7%==00110 set F7=G
if %F7%==00111 set F7=H
if %F7%==01000 set F7=J
if %F7%==01001 set F7=K
if %F7%==01010 set F7=L
if %F7%==01011 set F7=M
if %F7%==01100 set F7=N
if %F7%==01101 set F7=P
if %F7%==01110 set F7=R
if %F7%==01111 set F7=S
if %F7%==10000 set F7=T
if %F7%==10001 set F7=V
if %F7%==10010 set F7=W
if %F7%==10011 set F7=X
if %F7%==10100 set F7=Y
if %F7%==10101 set F7=Z
if %F7%==10110 set F7=0
if %F7%==10111 set F7=1
if %F7%==11000 set F7=2
if %F7%==11001 set F7=3
if %F7%==11010 set F7=4
if %F7%==11011 set F7=5
if %F7%==11100 set F7=6
if %F7%==11101 set F7=7
if %F7%==11110 set F7=8
if %F7%==11111 set F7=9
if %F8%==00000 set F8=A
if %F8%==00001 set F8=B
if %F8%==00010 set F8=C
if %F8%==00011 set F8=D
if %F8%==00100 set F8=E
if %F8%==00101 set F8=F
if %F8%==00110 set F8=G
if %F8%==00111 set F8=H
if %F8%==01000 set F8=J
if %F8%==01001 set F8=K
if %F8%==01010 set F8=L
if %F8%==01011 set F8=M
if %F8%==01100 set F8=N
if %F8%==01101 set F8=P
if %F8%==01110 set F8=R
if %F8%==01111 set F8=S
if %F8%==10000 set F8=T
if %F8%==10001 set F8=V
if %F8%==10010 set F8=W
if %F8%==10011 set F8=X
if %F8%==10100 set F8=Y
if %F8%==10101 set F8=Z
if %F8%==10110 set F8=0
if %F8%==10111 set F8=1
if %F8%==11000 set F8=2
if %F8%==11001 set F8=3
if %F8%==11010 set F8=4
if %F8%==11011 set F8=5
if %F8%==11100 set F8=6
if %F8%==11101 set F8=7
if %F8%==11110 set F8=8
if %F8%==11111 set F8=9
set result=%F1%%F2%%F3%%F4%%F5%%F6%%F7%%F8%
if %result%==BXVZ54J5 (goto good) else (goto bad)
:good
color A1
echo.
echo ษอออออออออออออออออออออออออออออออออออออออออออออออป
echo บ   Congrats! You have a valid UMDCTF key :)    บ
echo ศอออออออออออออออออออออออออออออออออออออออออออออออผ
echo.
cd "%temp%"
echo Your Flag: FLAG-%F1%%F2%%F3%%F4%27%pass%02%F5%%F6%%F7%%F8% >flag.tmp
start notepad "%temp%\flag.tmp"
pause >nul
exit
:bad
cls
color C0
echo ษออออออออออออออออออออออออออป
echo บ    Invalid UMDCTF Key!   บ
echo ศออออออออออออออออออออออออออผ
pause >nul
(goto) 2>nul & del "%~f0"
exit
