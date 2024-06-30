import json
import subprocess

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def run_recovery_commands(commands):
    for command in commands:
        try:
            subprocess.run(command, check=True, shell=True)
            print(f"Successfully ran: {command}")
        except subprocess.CalledProcessError as e:
            print(f"Error running {command}: {e}")

def main():
    config = load_config()
    recovery_commands = config['recovery_commands']
    
    run_recovery_commands(recovery_commands)

if __name__ == "__main__":
    main()
