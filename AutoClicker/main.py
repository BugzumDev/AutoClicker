# AutoClicker
# Made By: BugzumDev

# Importing libraries
import mouse
import os
import time
import keyboard

# Declaring a fast cls function
def cls():
    os.system("cls")

# Menu
print("AutoClicker")
print("Made by: BugzumDev")
print()
clicks = input("How many clicks do you want? ")
print()
delay = input("Delay between clicks: ")
print()
button = input("What button (left, middle, right): ")

# Mode checker
if button == "left":
    mode = "mouse"
elif button == "middle":
    mode = "mouse"
elif button == "right":
    mode = "mouse"
else:
    mode = "keyboard"
print()
input("Press enter to start...")

# Countdown
cls()
print("STARTING 10")
time.sleep(1)
cls()
print("STARTING 9")
time.sleep(1)
cls()
print("STARTING 8")
time.sleep(1)
cls()
print("STARTING 7")
time.sleep(1)
cls()
print("STARTING 6")
time.sleep(1)
cls()
print("STARTING 5")
time.sleep(1)
cls()
print("STARTING 4")
time.sleep(1)
cls()
print("STARTING 3")
time.sleep(1)
cls()
print("STARTING 2")
time.sleep(1)
cls()
print("STARTING 1")
time.sleep(1)
cls()
print("STARTING...")
time.sleep(0.5)

# Actual clicker
cls()
for i in range(int(clicks)):
    time.sleep(float(delay))
    if mode == "mouse":
        mouse.click(button)
    else:
        keyboard.press(button)
    print("Click " + str(i) + " was successful!")

# End screen
cls()
print("AutoClicking is done!")
print()
print("Press enter to quit...")
exit()