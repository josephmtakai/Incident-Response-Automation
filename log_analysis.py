import json

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def analyze_logs(log_file_path):
    with open(log_file_path, 'r') as log_file:
        logs = log_file.readlines()

    suspicious_entries = [log for log in logs if "suspicious" in log]

    return suspicious_entries

def main():
    config = load_config()
    log_file_path = config['log_file_path']
    
    suspicious_entries = analyze_logs(log_file_path)
    
    if suspicious_entries:
        print("Suspicious log entries found:")
        for entry in suspicious_entries:
            print(entry)
    else:
        print("No suspicious entries found.")

if __name__ == "__main__":
    main()
