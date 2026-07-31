import platform
import os
from datetime import datetime

def inspect_environment():
    print("=== Python Environment Test ===")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Current Directory: {os.getcwd()}")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("================================")

if __name__ == "__main__":
    inspect_environment()