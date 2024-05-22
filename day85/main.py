import argparse
import subprocess

# Initialize the parser
parser = argparse.ArgumentParser(description="Download a file from a URL and save it with a specified name.")

# Add arguments
parser.add_argument("URL", help="URL of the file to download")
parser.add_argument("Output", help="Name to save the downloaded file")

# Parse the arguments
args = parser.parse_args()

# Print the arguments (for debugging purposes)
print(f"URL: {args.URL}")
print(f"Output: {args.Output}")

# Use the arguments in the curl command
subprocess.run(["curl", "-o", args.Output, args.URL])
