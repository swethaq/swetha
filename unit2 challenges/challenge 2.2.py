''' Implement a class called Player that represent a cricket player. The Player should have a 
method called play() Which prints "The player is playing cricket.Derive two classes, Batsman and 
Bowler, from the player class. Override the play() method in each derived class to print "The batsman
is batting " and "The boeler is bowling", respectively.Write a program to create objects of both the
Batsman and Bowler Classes and call the play() method for each object.'''
class player:
      def play(self):
          print("THE PLAYER IS PLAYINF CRICKET. ")
class Batsman(player):
      def play(self):
          print("THE BATS MAN IS BATTING. ")
class Bowler(player):
      def play(self):
          print("THE BOWLER IS BOWLING. ")
batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()