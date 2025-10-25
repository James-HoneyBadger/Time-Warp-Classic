REM BASIC Example Program - Number Guessing Game
REM This program demonstrates BASIC syntax with loops and conditionals

10 PRINT "🎯 Welcome to the Number Guessing Game!"
20 PRINT "I'm thinking of a number between 1 and 100."
30 PRINT ""

REM Generate random number
40 LET SECRET = INT(RND(1) * 100) + 1
50 LET GUESSES = 0

REM Main game loop
60 PRINT "Enter your guess (1-100), or 0 to quit:"
70 INPUT GUESS
80 IF GUESS = 0 THEN GOTO 150

90 LET GUESSES = GUESSES + 1

100 IF GUESS = SECRET THEN GOTO 130
110 IF GUESS < SECRET THEN PRINT "Too low! Try higher."
120 IF GUESS > SECRET THEN PRINT "Too high! Try lower."
125 GOTO 60

REM Win condition
130 PRINT ""
135 PRINT "🎉 Congratulations! You guessed it in"; GUESSES; "tries!"
140 PRINT "The number was"; SECRET
145 GOTO 160

REM Quit message
150 PRINT "Thanks for playing!"

REM Play again?
160 PRINT ""
165 PRINT "Would you like to play again? (Y/N)"
170 INPUT AGAIN$
175 IF AGAIN$ = "Y" OR AGAIN$ = "y" THEN GOTO 10
180 PRINT "Goodbye!"
190 END</content>
<parameter name="filePath">/home/james/Time_Warp_Classic/hello_basic.bas