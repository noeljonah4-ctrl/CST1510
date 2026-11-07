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

import pandas as pd
import matplotlib.pyplot as plt


# ==================================================================== LOAD
# 1. Read the Cyber CSV file into a DataFrame.
#
# In the Cyber lane, the columns are different from the earlier Record Check.
# Instead of label/value/limit, we use source_ip, failed_logins and total_attempts.
# This matches the W06 lab instructions for the Cyber route.

df = pd.read_csv("cyber_records.csv")


# ================================================================= PROCESS
# 2. Add the percentage and status columns.
#
# For Cyber, we measure how close the failed logins are to the total attempts:
# percent = (failed_logins / total_attempts) * 100
# Then we use a lambda to label each row as OVER LIMIT, WARNING, or OK.

df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)


# ================================================================== OUTPUT
# 3. Print and save the results.
#
# We print the DataFrame to check the values and percentage. We then filter to
# rows that are not OK, print the group counts, save the full DataFrame to a new
# CSV, and create one bar chart of the counts by status.

print("Full Cyber data table:")
print(df)
print()

# Typical: show only the rows that need attention.
# This uses a boolean filter in [] and no loop.
needs_attention = df[df["status"] != "OK"]
print("Rows that are not OK:")
print(needs_attention)
print()

# Excellent: count how many entries fall into each status.
status_counts = df.groupby("status").size()
print("Count per status:")
print(status_counts)
print()

# Save the full DataFrame to a CSV file.
df.to_csv("cyber_records_report.csv", index=False)

# Draw and save a bar chart of the status counts.
status_counts.plot(kind="bar", color=["green", "orange", "red"])
plt.title("Cyber Status Counts")
plt.xlabel("Status")
plt.ylabel("Number of Sources")
plt.tight_layout()
plt.savefig("cyber_status_counts.png")
plt.show()


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
