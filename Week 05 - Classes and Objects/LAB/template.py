"""
RECORD CHECK  -  my version
===========================

Name  : Alito noel Jonah
Lane  :   Cyber 
Date  : 23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

from pathlib import Path


# ====================================================================== CLASS
# 1. Define a class called Record.
#
# A Record stores the label, current value and limit for one check.
# The class also calculates whether the value is OK, WARNING, or OVER LIMIT.

class Record:
    """Stores a label, numeric value and limit."""

    # Class-level counter: shared by all Record objects, not copied into each one.
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Store the record details for one item."""
        self.label = label          # the record name (for example R-001)
        self.value = float(value)   # convert the stored value to a number
        self.limit = float(limit)   # convert the limit to a number

    def percent(self):
        """Return the value as a percentage of the limit."""
        return (self.value / self.limit) * 100

    def status(self):
        """Return OVER LIMIT, WARNING or OK for this record."""
        percentage = self.percent()
        if percentage >= 100:
            return "OVER LIMIT"
        if percentage >= 90:
            return "WARNING"
        return "OK"

    def is_over(self):
        """Return True if the value is greater than the limit."""
        return self.value > self.limit


# ==================================================================== RECORDS
# 2. Create your records.
#
# The file contains one line per record in the format:
# label,value,limit
# For example: R-001,87,100
# We read those values and turn each one into a Record object.


def load_records(path):
    """Read label,value,limit lines from a file and return Record objects."""
    records = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            label, value, limit = [part.strip() for part in line.split(",")]
            records.append(Record(label, value, limit))
    return records


# Use the file in the same folder as this script.
records = load_records(Path(__file__).with_name("records_sample.txt"))


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
# This loop checks each Record object and prints the label, value, limit,
# and the status for that record. It also counts how many records are over limit.

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"Label : {record.label}")
    print(f"Value : {record.value}")
    print(f"Limit : {record.limit}")
    print(f"Status: {record.status()}")
    print(f"Percent: {record.percent():.1f}%")

    # Keep a running total of how many records are over the limit.
    if record.is_over():
        Record.over_limit_count += 1

    print("=" * 34)

# Final summary after all records have been checked.
print()
print("=" * 34)
print(f"TOTAL OVER LIMIT: {Record.over_limit_count}")
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
