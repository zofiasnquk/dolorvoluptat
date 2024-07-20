import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Process VTT files")

# Add an argument for the input VTT file
parser.add_argument("input_vtt", help="Path to the input VTT file")

# Parse the command-line arguments
args = parser.parse_args()

# Access the value of the input_vtt argument
print("Input VTT file:", args.input_vtt)
