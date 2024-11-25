import time
import winsound

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d} : {seconds_left:02d}")

    # Play sound when the alarm finishes
    winsound.Beep(1000, 1000)

minutes = int(input("Set the timer for minutes: "))
seconds = int(input("set the timer for seconds: "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)
