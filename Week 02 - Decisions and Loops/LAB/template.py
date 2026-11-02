"""
RECORD CHECK  -  my version
===========================

Name  : Noel Jonah Alito
Lane  :  Cyber       
Date  : 3/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

over_limit_count = 0

while True:
    label = input("Enter a label (or 'quit' to finish): ")
    if label.lower() == "quit":
        break

    value = float(input("Enter the value: "))
    limit = float(input("Enter the limit: "))

    # ================================================================== PROCESS
    # 2. Work out the difference and the percentage.
    difference = value - limit
    percent = (value / limit) * 100

    # 3. Decide a status and store it in a variable called status.
    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # =================================================================== OUTPUT
    # 4. Print the report.
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Value            : {value:>10.2f}")
    print(f"  Limit            : {limit:>10.2f}")
    print(f"  Difference       : {difference:>+10.2f}")
    print(f"  Percent of limit : {percent:>10.2f}%")
    print(f"  Status           : {status:>10}")
    print("=" * 34)

print(f"Number of records over limit: {over_limit_count}")

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
