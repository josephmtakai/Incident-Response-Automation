import json
import subprocess
import os

def load_config():
    """Loads configuration from the config.json file."""
    try:
        with open('config.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: config.json file not found.")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: JSON decode error: {e}")
        exit(1)

def run_recovery_commands(commands):
    """Runs the recovery commands specified in the config."""
    for command in commands:
        try:
            result = subprocess.run(command, check=True, shell=True, capture_output=True, text=True)
            print(f"Successfully ran: {command}")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error running {command}: {e}")
            print(e.stderr)

def main():
    config = load_config()
    recovery_commands = config.get('recovery_commands', [])
    
    if not recovery_commands:
        print("No recovery commands found in config.json.")
        exit(1)
    
    run_recovery_commands(recovery_commands)

if __name__ == "__main__":
    main()
