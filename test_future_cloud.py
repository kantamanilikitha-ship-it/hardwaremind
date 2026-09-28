from diagnosis_engine import diagnose_hardware_failure


# ============================================================
# NEW FAILURE AFTER HARDWAREMIND HAS LEARNED
# ============================================================

future_failure = """
Incident ID: HW-010
Device: IoT Controller Z60
Device Type: Embedded Controller

Temperature: 88°C
Voltage: 12.9V
Current: 1.9A

Symptoms: Overheating and intermittent sensor readings
Sensor Status: Intermittent
Communication Status: Normal
"""


print("\n")
print("============================================================")
print("HARDWAREMIND FUTURE FAILURE TEST")
print("============================================================")

print("\nNew Failure:")
print(future_failure)


# ============================================================
# MEMBER 2 + MEMBER 3
# ============================================================

result = diagnose_hardware_failure(future_failure)


# ============================================================
# SHOW AI DIAGNOSIS
# ============================================================

print("\n")
print("============================================================")
print("AI DIAGNOSIS FOR FUTURE FAILURE")
print("============================================================")

print(result["diagnosis"])


# ============================================================
# SHOW HINDSIGHT MEMORY USED
# ============================================================

print("\n")
print("============================================================")
print("HINDSIGHT MEMORY USED BY AI")
print("============================================================")

print(result["memory_context"])


# ============================================================
# FINAL CHECK
# ============================================================

print("\n")
print("============================================================")
print("FINAL TEST RESULT")
print("============================================================")

memory_context = result["memory_context"].lower()

if (
    "z50" in memory_context
    and "voltage regulator overheating" in memory_context
):
    print("SUCCESS!")
    print("Hindsight memory was retrieved for the new failure.")
    print("Member 3 AI used the retrieved experience.")
    print("HardwareMind demonstrated the learning loop.")

else:
    print("Memory was not detected in the final context.")

print("============================================================")