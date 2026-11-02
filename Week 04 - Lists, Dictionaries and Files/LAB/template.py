"""
RECORD CHECK  -  my version
===========================

Name  : Noel Jonah Alito
Lane  : Cyber
Date  : 02/11/2026

Run it:   python template.py
"""


def status_of(percent):
    """Return the status for a percentage of the limit."""
    # Check the highest threshold first.
    if percent >= 100:
        return "OVER LIMIT"
    if percent >= 90:
        return "WARNING"
    return "OK"


def check_record(value, limit):
    """Return a record's difference, percentage, and status."""
    difference = value - limit
    percent = (value / limit) * 100
    status = status_of(percent)
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print a bordered report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    # Align numbers and show two decimal places, like the Week 3 report.
    print(f"  Failed logins    : {value:>10.2f}")
    print(f"  Total attempts   : {limit:>10.2f}")
    print(f"  Difference       : {difference:>+10.2f}")
    print(f"  Percent of limit : {percent:>10.2f}%")
    print(f"  Status           : {status:>10}")
    print("=" * 34)


def load_records(path):
    """Read comma-separated labels, values, and limits into a list of dictionaries."""
    records = []
    with open(path, "r") as records_file:
        for line in records_file:
            label, value, limit = line.strip().split(",")
            records.append(
                {"label": label, "value": float(value), "limit": float(limit)}
            )
    return records


# Load the Cyber Security records from the data file beside this program.
try:
    records = load_records("records.txt")
except FileNotFoundError:
    print("Could not find records.txt. Starting with no records.")
    records = []

over_limit_count = 0

# Save one label and status per record while printing its full report.
with open("record_results.txt", "w") as results_file:
    for record in records:
        difference, percent, status = check_record(
            record["value"], record["limit"]
        )
        print_report(
            record["label"],
            record["value"],
            record["limit"],
            difference,
            percent,
            status,
        )
        results_file.write(f"{record['label']},{status}\n")

        if status == "OVER LIMIT":
            over_limit_count += 1

print(f"Number of records over limit: {over_limit_count}")
