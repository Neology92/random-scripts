#!/bin/bash

# Check if at least one argument is provided
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <input_file> [-s <suffix>] <output_file1> [<output_file2> ...]"
    exit 1
fi

# Input file containing content to be copied
input_file="$1"
shift # Remove the first argument from the list

# Check if the input file exists
if [ ! -e "$input_file" ]; then
    echo "Error: Input file '$input_file' not found."
    exit 1
fi

suffix="" # Default suffix is an empty string

# Check if the next argument is the suffix option
if [ "$1" == "-s" ]; then
    # Shift to the next argument to get the suffix
    shift
    suffix="$1"
    shift # Remove the suffix from the list
fi

# Get the extension of the input file
input_extension="${input_file##*.}"

# Loop through the remaining arguments and create files with the input extension and suffix
for output_file in "$@"; do
    # Use the input extension for the output files
    echo "$(cat "$input_file")" > "$output_file$suffix.$input_extension"
    echo "Created file: $output_file$suffix.$input_extension"
done

echo "Script completed successfully."
