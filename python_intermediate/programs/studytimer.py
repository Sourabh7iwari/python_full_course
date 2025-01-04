import numpy as np
import sounddevice as sd
import time
import sys

frequency = 440
duration = 1.0
sample_rate = 44100

def generate_beep(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    beep = 0.5 * np.sin(2 * np.pi * freq * t)
    return beep

def play_beep():
    beep = generate_beep(frequency, duration, sample_rate)
    sd.play(beep, sample_rate)
    sd.wait()

def countdown_timer(seconds):
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer = f"{mins:02}:{secs:02}"
        sys.stdout.write(f"\r{timer}")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rTime's up!        \n")

def study_timer(study_time, break_time):
    print("Starting study timer!")
    while True:
        print(f"Study for {study_time} minutes.")
        s_s = int(study_time*60)
        countdown_timer(s_s)
        play_beep()
        print("Take a break.")

        print(f"Take a {break_time} minute break.")
        b_S = int(break_time * 60)
        countdown_timer(b_S)
        play_beep()
        print("Back to studying.\n")

study_timer(study_time=30, break_time=10)