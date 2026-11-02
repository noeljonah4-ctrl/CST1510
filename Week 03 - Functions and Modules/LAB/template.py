"""
RECORD CHECK  -  my version
===========================

Name  : Noel Jonah Alito
Lane  :   Cyber
Date  : 10/10/2026

Run it:   python template.py
"""


def status_of(percent):
    """Return the status for a percentage of the limit."""
    # Check the highest threshold first so it is not labelled WARNING.
    if percent >= 100:
        return "OVER LIMIT"
    if percent >= 90:
        return "WARNING"
    return "OK"


def check(value, limit):
    """Return the difference from the limit and the percentage of the limit."""
    # A positive difference means the value is over the limit.
    difference = value - limit
    # The percentage makes records comparable even when limits differ.
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print a bordered report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    # Format numeric values to two decimals and align them for readability.
    print(f"  Value            : {value:>10.2f}")
    print(f"  Limit            : {limit:>10.2f}")
    print(f"  Difference       : {difference:>+10.2f}")
    print(f"  Percent of limit : {percent:>10.2f}%")
    print(f"  Status           : {status:>10}")
    print("=" * 34)


over_limit_count = 0

# Keep checking records until the user enters "quit".
while True:
    label = input("Enter a label (or 'quit' to finish): ")
    if label.lower() == "quit":
        break

    value = float(input("Enter the value: "))
    limit = float(input("Enter the limit: "))

    difference, percent = check(value, limit)
    status = status_of(percent)
    if status == "OVER LIMIT":
        # Count only records at or above their limit.
        over_limit_count += 1

    print_report(label, value, limit, difference, percent, status)

print(f"Number of records over limit: {over_limit_count}")
