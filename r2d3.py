
# https://github.com/bastibe/python-soundfile
# https://python-soundfile.readthedocs.io/en/0.13.1/


import sounddevice as sd
import numpy as np
import time
import random
import soundfile as sf  # Import the soundfile library

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

def play_and_save_sound(sound, filename="r2d2_sound.wav", sample_rate=44100, save_mp3=False):
    """Plays the generated sound and optionally saves it."""
    sd.play(sound, sample_rate)
    if save_mp3:
        try:
            sf.write(f"{filename}.mp3", sound, sample_rate, format='MP3', subtype='MPEG-1')
            print(f"Saved as {filename}.mp3")
        except Exception as e:
            print(f"Error saving as MP3: {e}")
            print("Make sure lameenc is installed and accessible.")
    else:
        sf.write(f"{filename}.wav", sound, sample_rate)
        print(f"Saved as {filename}.wav")
    sd.wait()

def r2d2_speak_and_save(num_sounds=5, save_mp3=False):
    """Generates a sequence of R2-D2-like sounds and saves them."""
    for i in range(num_sounds):
        sound_type = random.choice(["beep", "boop", "warble"])
        duration = random.uniform(0.1, 0.5)
        filename = f"r2d2_sound_{i+1}"

        if sound_type == "beep":
            frequency = random.uniform(300, 1000)
            sound = generate_beep(frequency, duration)
        elif sound_type == "boop":
            frequency = random.uniform(800, 1500)
            sound = generate_boop(frequency, duration * 0.6)
        elif sound_type == "warble":
            start_freq = random.uniform(500, 1200)
            end_freq = random.uniform(start_freq - 400, start_freq + 400)
            sound = generate_warble(start_freq, end_freq, duration)

        play_and_save_sound(sound, filename=filename, save_mp3=save_mp3)
        time.sleep(random.uniform(0.05, 0.3))

if __name__ == "__main__":
    print("Generating and saving R2-D2 sounds...")
    r2d2_speak_and_save(num_sounds=3, save_mp3=True)  # Set save_mp3 to True to save as MP3
    print("Done!")