#!/bin/bash

# ---- https://www.freecodecamp.org/news/bash-if-statement-linux-shell-if-else-syntax-example/



# echo -n "Enter a name: "

# read name

# if [[ "$name" == "sudo" ]]; 
# then
#   printf "\nHello ${name}!\n"
# else
#   printf "\nHello Anonymous\n"
# fi



# ---------------------
# a=99
# b=23
# if [ $a -lt $b ]
# then
#   printf "a is less than b\n"
# else 
#   printf "a is greater than b\n"
# fi




# --- make a Go lang script   main.go --> go build  ==> ./gofile
# ./gofile




# shopping_list[*] for printing all elements of shopping_list

shopping_list=("apples", "bananas", "milk")
# printf "Shopping List: ${shopping_list[*]}\n"




# Define default behavior (optional)
action="none"

# Parse flags and arguments
while getopts ":jn:" opt; do
  case $opt in
    j)
      action="joke"
      ;;
    n)
      action="numpy"
      # script_name="$OPTARG"  # Store the provided script name
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

# Check if any flag was provided
if [[ "$action" == "none" ]]; then
  echo "No flag provided. Use -j for a joke or -n nums to run a NumPy script."
  exit 1
fi

# Perform actions based on flags
if [[ "$action" == "joke" ]]; then
  # Replace this with your favorite way to get a joke (URL fetching, API call, etc.)
  echo "Here's a (hopefully) funny joke: Why did the scarecrow win an award? Because he was outstanding in his field!"
fi

if [[ "$action" == "nums" ]]; then
  # Check if script name is provided
  if [[ -z "$script_name" ]]; then
    echo "Error: Please specify a script name after -n flag."
    exit 1
  fi
  python3 numpynum.py
fi