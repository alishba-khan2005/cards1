
playername =str(input("enter player name:"))
matchesplayed=int(input("enter No of matches played:"))
runscored=int(input("enter runs scored:"))
wicketstaken=int(input("enter No of wickets taken:"))


batting_average = runscored/matchesplayed
if matchesplayed > 0:
  batting_average= runscored/ matchesplayed
else :
  batting_average= 0

if matchesplayed >= 50 and batting_average >= 50:
  print(f"{playername} is a world-class batsman!")
elif matchesplayed >= 30 and batting_average >= 40:
  print(f"{playername} is a promising batsman!")
elif wicketstaken >= 50:
  print(f"{playername} is a world-class bowler!")
elif wicketstaken >= 20:
  print(f"{playername} is a developing bowler!")
else :
  print(f"{playername} is a promisiong player!")
