import os
import subprocess

# Path to folder containing people
folder_path = "people/"

# Loop through files and run each
for filename in os.listdir(folder_path):
    if filename.endswith(".py"):
        file_path = os.path.join(folder_path, filename)
        print(f"Running {filename}...")

        # Run the file
        result = subprocess.run(["python", file_path], capture_output=True, text=True)

        # Print output and errors (if any)
        print(result.stdout)
        if result.stderr:
            print(f"Error in {filename}:\n{result.stderr}")
