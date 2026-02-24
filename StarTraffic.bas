100 REM Project Starflight Traffic Control
105 DIM FLEET$ ( 10 ) 
106 DIM PLANET$ ( 10 ) 
107 DIM STAR$ ( 10 ) 
110 GOSUB 8120 
120 PRINT "Do you need instructions? (y/n)" 
122 PRINT 
125 INPUT ANS$ 
126 TRNS = 0 : REM number of transits 
130 IF ANS$ = "y" OR ANS$ = "Y" THEN GOSUB 900 
135 PRINT 
150 REM TRANSIT LOOP
155 rem  pick a ship
160 ship = int(1+int(9*rnd(1)+.5))
162 FRM = 0: ARV = 0 : DEST= 0 :rem clear ship states
163 if sloc(ship)<1 then print Fleet$(ship) + " arrived!!":goto 600
170 FRM = sloc(ship)
175 p = 1+int(2*rnd(1)+.5) : rem pick destination
180 DEST  = EXT(ship,p)
200 rem display departure
205 print "Departing from "+planet$(sloc(ship)) + " Vessel: " +fleet$(ship)
210 print "heading for " +star$(DEST) +"."
220 sloc(ship) = -DEST :rem negative marks arrival
222 gosub 2000
225 goto 150
600 print fleet$(ship) + " arriving at " + STAR$(abs(sloc(ship))
605 sloc(ship) = abs(sloc(ship))
610 gosub 2000
800 goto  150
900 PRINT "This system will display current starship traffic"
920 PRINT "across a span of ten interconnected systems."
940 PRINT 
960 PRINT "Ships travel from system to system via hyperspace lanes"
980 PRINT "and you will see arrivals and departures."
985 PRINT  
1000 RETURN
2000 j = 0 : rem delay loop
2010 for i = 1 to 1000
2020 j = j + i
2025 next i
2030 return
8120 FOR I = 1 TO 10 
8125 READ SHIP$ 
8126 FLEET$ ( I ) = SHIP$ 
8127 NEXT I 
8220 FOR I = 1 TO 10 
8225 READ PL$ 
8226 PLANET$ ( I ) = PL$ 
8227 NEXT I 
8231 FOR I = 1 TO 10 
8235 READ ST$ 
8236 STAR$ ( I ) = ST$ 
8237 NEXT I 
8300 DIM EXT ( 10 , 3 ) 
8310 FOR I = 1 TO 10 
8315 FOR T = 1 TO 3 
8320 E = 1 + INT ( RND ( 1 ) * 9 + .5 ) 
8325 IF E = I THEN GOTO 8320 
8330 EXT ( I , T ) = E 
8335 NEXT T 
8340 NEXT I
8500 dim sloc(10): rem ship locations
8520 for s = 1 to 10
8540 sloc(s) = 1+int(9*rnd(1)+.5): rem each ship initial location
8560 next s
8900 RETURN 
9000 DATA "Adventurer" , "Omen" , "The Jellyfish" , "Saber" , "Hellhound" , "SC Providence" , "CS Shade" , "BS Khan" , "SS Andromeda" , "BS Nuria" 
9020 DATA "Vuthadoh", "Lesti", "Uverrooith", "Veohpo", "Codachaa", "Yorar", "Guvor", "Bincussial", "Uusnes", "Trah"
9040 DATA "Deey", "Uguaks", "Eceub", "Vret", "Sleak", "Krithuc", "Olutsos", "Huqein", "Pluedurs", "Isliursil"
