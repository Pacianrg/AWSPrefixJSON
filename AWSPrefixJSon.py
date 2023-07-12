import csv
import json
import urllib.request

# URL of JSON page
url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
csvFile = r"C:\inetpub\wwwroot\ebl\AWSGlobalAccelerator.csv"

# Fetch JSON

try:
    response = urllib.request.urlopen(url)
    data = json.load(response)

    # Filter for GLOBALACCELERATOR
    filteredData = [entry["ip_prefix"] for entry in data["prefixes"] if entry["service"] == "GLOBALACCELERATOR"]

    # Write the filtered values
    with open(csvFile, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows([[ip_prefix] for ip_prefix in filteredData])

    print(f"Output written to {csvFile}")

except Exception as e:
    print(f"Error: {e}")
