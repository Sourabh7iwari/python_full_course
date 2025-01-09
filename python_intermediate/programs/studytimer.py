import numpy as np
import sounddevice as sd
import time
import sys
import threading

frequency = 440
duration = 1.0
sample_rate = 44100
paused = False
pause_flag = threading.Event()

def generate_beep(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    beep = 0.5 * np.sin(2 * np.pi * freq * t)
    return beep

def play_beep():
    beep = generate_beep(frequency, duration, sample_rate)
    sd.play(beep, sample_rate)
    sd.wait()

def countdown_timer(seconds):
    global paused
    for remaining in range(seconds, 0, -1):
        while paused:
            pause_flag.wait()  # Wait until the timer is resumed
        mins, secs = divmod(remaining, 60)
        timer = f"{mins:02}:{secs:02}"
        sys.stdout.write(f"\r{timer}")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rTime's up!        \n")

def study_timer(study_time, break_time):
    global paused
    print("Starting study timer!")
    while True:
        i = input("Let's start grinding now. Reply with y/n for yes/no: ")
        if i == 'y':
            pause_thread = threading.Thread(target=pause_handler, daemon=True)
            pause_thread.start()
            print(f"Study for {study_time} minutes.")
            s_s = int(study_time * 60)
            countdown_timer(s_s)
            play_beep()
            print("Take a break.")

            print(f"Take a {break_time} minute break.")
            b_s = int(break_time * 60)
            countdown_timer(b_s)
            play_beep()
            print("\nBack to studying.\n")
        elif i == 'n':
            print("Sale kaamchor.\n")
        else:
            print("Enter y/n for yes/no.\n")

def pause_handler():
    global paused
    while True:
        key = input("Press 'p' to pause or 'c' to continue: \n")
        if key == 'p':
            paused = True
            print("Timer paused.")
        elif key == 'c':
            paused = False
            pause_flag.set()  # Resume the timer
            pause_flag.clear()
            print("Timer resumed.")

# Start the pause handler in a separate thread


study_timer(study_time=35, break_time=10)