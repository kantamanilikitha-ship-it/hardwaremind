from diagnosis_engine import diagnose_hardware_failure


# ============================================================
# NEW FAILURE
# ============================================================

new_failure = """
Incident ID: NEW-001
Device: IoT Controller Z90
Device Type: Embedded Controller

Temperature: 92°C
Voltage: 12.7V
Current: 2.0A

Symptoms: Device overheating and intermittent sensor readings
Sensor Status: Intermittent
Communication Status: Normal
"""


print()
print("============================================================")
print("HARDWAREMIND DATASET LEARNING TEST")
print("============================================================")

print("\nNEW HARDWARE FAILURE:")
print(new_failure)


# ============================================================
# AI INVESTIGATION
# ============================================================

result = diagnose_hardware_failure(new_failure)


# ============================================================
# SHOW DIAGNOSIS
# ============================================================

print()
print("============================================================")
print("AI DIAGNOSIS")
print("============================================================")

print(result["diagnosis"])


# ============================================================
# SHOW HINDSIGHT MEMORY
# ============================================================

print()
print("============================================================")
print("HINDSIGHT MEMORY RETRIEVED")
print("============================================================")

print(result["memory_context"])


# ============================================================
# FINAL CHECK
# ============================================================

print()
print("============================================================")
print("DATASET LEARNING TEST COMPLETE")
print("============================================================")

if (
    "Historical Incident" in result["memory_context"]
    and "No similar historical" not in result["memory_context"]
):

    print("SUCCESS!")
    print("Historical hardware experiences were retrieved.")
    print("The AI used Hindsight memory for the new failure.")

else:

    print("WARNING:")
    print("No relevant historical memory was detected.")

print("============================================================")