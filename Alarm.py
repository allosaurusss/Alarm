import datetime
import time
import pygame

def set_alarm(interval_hours):
    # Get the current time
    now = datetime.datetime.now()

    # Calculate the time for the first alarm
    alarm_time = now + datetime.timedelta(hours=interval_hours)

    print(f"Alarm set for {alarm_time.strftime('%Y-%m-%d %H:%M:%S')}")

    while True:
        current_time = datetime.datetime.now()

        # Check if it's time for the alarm
        if current_time >= alarm_time:
            print("It's time to feed!")
            play_alarm_sound()

            # Set the time for the next alarm
            alarm_time = current_time + datetime.timedelta(hours=interval_hours)
            print(f"Next alarm set for {alarm_time.strftime('%Y-%m-%d %H:%M:%S')}")

        # Wait for a short duration before checking again
        time.sleep(60)  # Check every minute

def play_alarm_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm_sound.mp3")  # Replace with the path to your alarm sound file
    pygame.mixer.music.play()

# Set the interval for the alarm (every 2.5 hours - change as needed)
interval_hours = 2.5

# Start the alarm
set_alarm(interval_hours)
