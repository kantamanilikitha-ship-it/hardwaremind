from diagnosis_engine import diagnose_hardware_failure
from hindsight_service import learn_from_resolution


# ==================================================
# 1. NEW HARDWARE FAILURE
# ==================================================

current_incident = {
    "incident_id": "HW-007",
    "device": "IoT Controller Z40",
    "device_type": "Embedded Controller",
    "temperature": "88°C",
    "voltage": "12.9V",
    "current": "1.9A",
    "symptoms": "Device overheating and intermittent sensor readings",
    "sensor_status": "Intermittent",
    "communication_status": "Normal"
}


print("==============================================")
print("       HARDWAREMIND FULL WORKFLOW TEST")
print("==============================================")


# ==================================================
# 2. PREPARE FAILURE INFORMATION
# ==================================================

failure_text = f"""
Device: {current_incident['device']}
Device Type: {current_incident['device_type']}
Temperature: {current_incident['temperature']}
Voltage: {current_incident['voltage']}
Current: {current_incident['current']}
Symptoms: {current_incident['symptoms']}
Sensor Status: {current_incident['sensor_status']}
Communication Status: {current_incident['communication_status']}
"""


# ==================================================
# 3. AI INVESTIGATION
# ==================================================

print("\n[1] INVESTIGATING NEW HARDWARE FAILURE...\n")

result = diagnose_hardware_failure(failure_text)

print("========== AI DIAGNOSIS ==========")
print(result["diagnosis"])


# ==================================================
# 4. ENGINEER CONFIRMATION
# ==================================================

print("\n==============================================")
print("ENGINEER CONFIRMATION")
print("==============================================")

# In this test, we simulate the engineer confirming
# the actual repair result.

confirmed_root_cause = "Voltage regulator overheating"

confirmed_fix = (
    "Replaced voltage regulator and added thermal pad"
)

outcome = (
    "Device operated successfully after repair"
)

print("\nConfirmed Root Cause:")
print(confirmed_root_cause)

print("\nConfirmed Fix:")
print(confirmed_fix)

print("\nOutcome:")
print(outcome)


# ==================================================
# 5. LEARN FROM CONFIRMED RESULT
# ==================================================

print("\n==============================================")
print("STORING CONFIRMED EXPERIENCE")
print("==============================================")

learning_result = learn_from_resolution(
    current_incident,
    confirmed_root_cause,
    confirmed_fix,
    outcome
)


print("\n========== LEARNING RESULT ==========")
print(learning_result)


# ==================================================
# 6. COMPLETE
# ==================================================

print("\n==============================================")
print("       FULL WORKFLOW COMPLETE")
print("==============================================")