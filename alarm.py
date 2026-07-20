from playsound import playsound
import time
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def clock(seconds):
    time_finished = 0

    print(CLEAR)
    while time_finished < seconds:
        time.sleep(1)
        time_finished += 1

        time_left = seconds - time_finished
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in : {minutes_left:02d}:{seconds_left:02d}")

    playsound("morning_alarm.mp3")

minutes = int(input("Enter the number of minutes you want to wait : "))
seconds = int(input("Enter the number of seconds you want to wait : "))
total_seconds = minutes * 60 + seconds
clock(total_seconds)