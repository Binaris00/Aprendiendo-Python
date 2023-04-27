import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

delay_print
print("Welcome to my madlib game, I change a little things about how play a madlib game for more comfort(remember this is a practice for my c:\n Firts I need a some information about you\n")
print("")
name = input("Whats is your name? ")
objetive = input("Select your objetive in the castle\n Rescue the princess\n Explore the castle\n You are lost and you want to stay in any place")

print(f"{name} enter in a castle and you are surprise for the how ")