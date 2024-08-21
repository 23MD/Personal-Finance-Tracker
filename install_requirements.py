import subprocess
import sys

def install_requirements():
    try:
        # Check if pip is installed
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])

        # Install the packages from requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

        print("All libraries installed successfully.")

    except subprocess.CalledProcessError as e:
        print("An error occurred while installing packages.")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()
