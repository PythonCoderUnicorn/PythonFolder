

from tqdm import tqdm
from termcolor import colored

# Simulate a long-running process with a loop
for i in tqdm(range(100)):  # tqdm wraps the loop
  # Simulate some work being done
  import time
  time.sleep(0.1)

# Print a message after the loop finishes
print(colored("Process completed!", "green") )


import os

os.system('say "hello prog bar" ')


