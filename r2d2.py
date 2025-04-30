
# https://python-sounddevice.readthedocs.io/en/0.5.1/installation.html

import sounddevice as sd
import numpy as np
import time
import random

def generate_beep(frequency, duration, amplitude=0.5, sample_rate=44100):
    """Generates a simple sine wave beep."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = amplitude * np.sin(2 * np.pi * frequency * t)
    return note

def generate_boop(frequency, duration, amplitude=0.3, sample_rate=44100):
    """Generates a short, higher-pitched boop using a square wave."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))
    return note

def generate_warble(start_freq, end_freq, duration, amplitude=0.4, sample_rate=44100):
    """Generates a frequency sweep (warble)."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    frequencies = np.linspace(start_freq, end_freq, len(t))
    note = amplitude * np.sin(2 * np.pi * frequencies * t)
    return note

def play_sound(sound, sample_rate=44100):
    """Plays the generated sound."""
    sd.play(sound, sample_rate)
    sd.wait()

def r2d2_speak(num_sounds=5):
    """Generates a sequence of R2-D2-like sounds."""
    for _ in range(num_sounds):
        sound_type = random.choice(["beep", "boop", "warble"])
        duration = random.uniform(0.1, 0.5)

        if sound_type == "beep":
            frequency = random.uniform(300, 1000)
            sound = generate_beep(frequency, duration)
        elif sound_type == "boop":
            frequency = random.uniform(800, 1500)
            sound = generate_boop(frequency, duration * 0.6) # Shorter boop
        elif sound_type == "warble":
            start_freq = random.uniform(500, 1200)
            end_freq = random.uniform(start_freq - 400, start_freq + 400)
            sound = generate_warble(start_freq, end_freq, duration)

        play_sound(sound)
        time.sleep(random.uniform(0.05, 0.3))

if __name__ == "__main__":
    print("Generating R2-D2 sounds...")
    r2d2_speak(10)
    print("Done!")






"""

Explanation:

Import Libraries:

sounddevice (sd): This library allows you to play and record audio. You might need to install it (pip install sounddevice). It often relies on system audio libraries, so ensure those are set up correctly on your machine.
numpy (np): This library is essential for numerical operations, especially for creating the arrays that represent sound waves. Install it if you haven't (pip install numpy).
time: Used for adding pauses between sounds.
random: Used to introduce variation in the sounds, making them more R2-D2-like.
generate_beep(frequency, duration, amplitude=0.5, sample_rate=44100):

Creates a simple sine wave. Sine waves produce a clear, tonal sound.
frequency: The pitch of the beep (in Hertz).
duration: How long the beep lasts (in seconds).
amplitude: The loudness of the beep (between 0 and 1).
sample_rate: The number of samples per second (common audio quality).
np.linspace: Creates an array of evenly spaced time points.
np.sin: Generates the sine wave based on the frequency and time.
generate_boop(frequency, duration, amplitude=0.3, sample_rate=44100):

Creates a short, often higher-pitched sound using a square wave. Square waves have a buzzier, more digital quality.
np.sign(np.sin(...)): This is a way to generate a square wave. The sign function returns -1 or 1 based on the sign of the sine wave.
generate_warble(start_freq, end_freq, duration, amplitude=0.4, sample_rate=44100):

Creates a sound with a changing frequency (a sweep or warble). This is characteristic of some of R2-D2's vocalizations.
np.linspace(start_freq, end_freq, len(t)): Creates an array of frequencies that change linearly over the duration.
play_sound(sound, sample_rate=44100):

Uses sd.play() to send the generated NumPy array (representing the sound) to your speakers.
sd.wait(): Blocks the execution of the script until the sound has finished playing.
r2d2_speak(num_sounds=5):

This function generates a sequence of random R2-D2-like sounds.
It randomly chooses between a "beep," "boop," or "warble."
It assigns random frequencies and durations within certain ranges to make the sounds varied.
It calls the appropriate sound generation function and then play_sound() to play it.
time.sleep() adds a short pause between each sound.
if __name__ == "__main__": block:

This ensures that the r2d2_speak() function is called only when you run the script directly.


"""