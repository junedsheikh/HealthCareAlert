import time
import winsound

print("<<<<<<<<<< Welcome To Health Care Alert >>>>>>>>>>")
print("I will give you remainder for task while you programming in office to stay healthy.")
def water():
    winsound.PlaySound("water.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    inp = input("Drink Water and Press Enter")
    if inp != None:
        winsound.PlaySound(None, winsound.SND_PURGE)
        with open("Health Log.txt", "a") as f:
            f.write(time.asctime(time.localtime(time.time())) + " " + "Drank Water" + "\n")
def eye():
    winsound.PlaySound("water.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    inp = input("Move eyes and Press Enter")
    if inp != None:
        winsound.PlaySound(None, winsound.SND_PURGE)
        with open("Health Log.txt", "a") as f:
            f.write(time.asctime(time.localtime(time.time())) + " " + "Drank Water" + "\n")
def ex():
    winsound.PlaySound("water.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    inp = input("Do body exercise and Press Enter")
    if inp != None:
        winsound.PlaySound(None, winsound.SND_PURGE)
        with open("Health Log.txt", "a") as f:
            f.write(time.asctime(time.localtime(time.time())) + " " + "Drank Water" + "\n")
while True:
    if time.localtime(time.time()).tm_hour > 9 and time.localtime(time.time()).tm_hour < 17:
        while True:
            water()
            time.sleep(1200)
            break
        while True:
            eye()
            time.sleep(1800)
            break
        while True:
            ex()
            time.sleep(2700)
            break
    else:
        print("You are out of office time")
        break
print(">>>>>>>>>>\tBye! and take care of your health.")
