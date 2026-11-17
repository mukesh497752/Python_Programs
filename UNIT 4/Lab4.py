
import json
import os

try:
    # Get the folder where Lab4.py is saved
    folder_path = os.path.dirname(os.path.abspath(__file__))

    # Locate logs.json in the same folder
    file_path = os.path.join(folder_path, "logs.json")

    print("Looking for file:", file_path)

    # Open and read JSON file
    with open(file_path, "r") as file:
        logs = json.load(file)

    # Initialize counters
    info_count = 0
    warning_count = 0
    error_count = 0

    print("\n===== APPLICATION LOG RECORDS =====")

    # Display all log records
    for log in logs:
        print("\nTimestamp:", log["timestamp"])
        print("Log Level:", log["level"])
        print("Message:", log["message"])

        # Count log categories
        level = log["level"].upper()

        if level == "INFO":
            info_count += 1
        elif level == "WARNING":
            warning_count += 1
        elif level == "ERROR":
            error_count += 1

        print("-----------------------------")

    # Display summary
    print("\n===== LOG SUMMARY =====")
    print("Total INFO messages:", info_count)
    print("Total WARNING messages:", warning_count)
    print("Total ERROR messages:", error_count)
    print("Total log records:", len(logs))

except FileNotFoundError:
    print("Error: logs.json file does not exist.")
    print("Please check whether logs.json is inside the UNIT 4 folder.")

except json.JSONDecodeError:
    print("Error: Invalid JSON data in the file.")

except (KeyError, TypeError, AttributeError):
    print("Error: Invalid log record format.")
