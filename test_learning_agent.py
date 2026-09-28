from hardware_agent import investigate_failure, learn_from_confirmed_resolution
from hindsight_service import _load_local_memory


# ============================================================
# STEP 1: NEW HARDWARE FAILURE
# ============================================================

current_incident = {
    "incident_id": "HW-009",
    "device": "IoT Controller Z50",
    "device_type": "Embedded Controller",
    "temperature": 89,
    "voltage": 12.8,
    "current": 1.9,
    "symptoms": "Overheating and intermittent sensor readings",
    "sensor_status": "Intermittent",
    "communication_status": "Normal"
}


print("\n")
print("============================================================")
print("HARDWAREMIND LEARNING LOOP")
print("============================================================")


# ============================================================
# STEP 2: AI INVESTIGATES USING MEMORY
# ============================================================

result = investigate_failure(current_incident)


# ============================================================
# STEP 3: ENGINEER CONFIRMS THE RESOLUTION
# ============================================================

confirmed_root_cause = "Voltage regulator overheating"

confirmed_fix = (
    "Replaced voltage regulator and added thermal pad"
)

outcome = "Device operated successfully after repair"


print("\n============================================================")
print("ENGINEER CONFIRMATION")
print("============================================================")

print(f"Confirmed Root Cause: {confirmed_root_cause}")
print(f"Confirmed Fix: {confirmed_fix}")
print(f"Outcome: {outcome}")


# ============================================================
# STEP 4: TEACH HARDWAREMIND
# ============================================================

learning_result = learn_from_confirmed_resolution(
    current_incident,
    confirmed_root_cause,
    confirmed_fix,
    outcome
)

print("\nLearning result:")
print(learning_result)


# ============================================================
# STEP 5: VERIFY DIRECTLY FROM LOCAL MEMORY
# ============================================================

print("\n============================================================")
print("VERIFYING LEARNING")
print("============================================================")

all_memories = _load_local_memory()

learned_incident = None

for incident in all_memories:

    if incident.get("incident_id") == "HW-009":
        learned_incident = incident
        break


if learned_incident:

    print("\nNEW LEARNED EXPERIENCE FOUND!")

    print(
        f"Incident ID: "
        f"{learned_incident.get('incident_id')}"
    )

    print(
        f"Device: "
        f"{learned_incident.get('device')}"
    )

    print(
        f"Root Cause: "
        f"{learned_incident.get('root_cause')}"
    )

    print(
        f"Fix: "
        f"{learned_incident.get('fix')}"
    )

    print(
        f"Outcome: "
        f"{learned_incident.get('outcome')}"
    )

else:

    print("\nERROR: HW-009 was not found in local memory.")


# ============================================================
# FINAL RESULT
# ============================================================

print("\n============================================================")
print("FINAL RESULT")
print("============================================================")

if learned_incident:

    print("SUCCESS!")
    print("HardwareMind successfully learned from the confirmed failure.")
    print("The learned experience is stored for future investigations.")

else:

    print("LEARNING VERIFICATION FAILED.")

print("============================================================")