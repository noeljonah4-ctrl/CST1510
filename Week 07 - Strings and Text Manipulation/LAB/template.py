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

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.
#
#    This version uses the Cyber lane from the lab: the data is shaped like
#    source_ip, failed_logins=..., total_attempts=... and the status is based on
#    the failed login percentage.


def parse_line(raw_line):
    """Clean one messy Cyber record and return a dictionary of parsed values."""
    line = raw_line.strip()

    # Split once at the first comma so the source IP is separated cleanly.
    source_part, remainder = line.split(",", 1)
    source_ip = source_part.strip().lower()

    # Convert pieces like "failed_logins=12" and "total_attempts=400" to floats.
    parsed = {}
    for item in remainder.split(","):
        key, value = item.split("=", 1)
        clean_key = key.strip().lower()
        clean_value = float(value.strip())
        parsed[clean_key] = clean_value

    parsed["source_ip"] = source_ip
    return parsed


def status_of(record):
    """Return OVER LIMIT, WARNING or OK based on the failed login percentage."""
    total_attempts = record.get("total_attempts", 0)
    failed_logins = record.get("failed_logins", 0)

    if total_attempts == 0:
        return "OK"

    percent = (failed_logins / total_attempts) * 100
    if percent >= 100:
        return "OVER LIMIT"
    if percent >= 90:
        return "WARNING"
    return "OK"


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.
#
#    This version reads a file containing messy Cyber log entries.

raw_records = []
with open("cyber_messy_records.txt", "r", encoding="utf-8") as file:
    for line in file:
        raw_records.append(line.strip())


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.
#
#    The program checks each Cyber record and reports whether the attack rate is
#    a warning or an over-limit event.

total_records = 0
flagged_count = 0

for raw_record in raw_records:
    try:
        record = parse_line(raw_record)
    except ValueError:
        print(f"Could not parse: {raw_record}")
        continue

    total_records += 1
    status = status_of(record)

    if status != "OK":
        flagged_count += 1

    print(f"{record['source_ip']} -> {record} | {status}")

print()
print(f"Summary: {total_records} records checked, {flagged_count} flagged.")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
