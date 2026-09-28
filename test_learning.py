from hardware_agent import investigate_failure, learn_from_confirmed_resolution
from hindsight_service import search_similar_incidents, _load_local_memory


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
# STEP 2: AI INVESTIGATES USING EXISTING MEMORY
# ============================================================

result = investigate_failure(current_incident)


# ============================================================
# STEP 3: ENGINEER CONFIRMS THE ACTUAL RESOLUTION
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
# STEP 5: VERIFY THAT HW-009 WAS STORED
# ============================================================

print("\n============================================================")
print("VERIFYING THAT HARDWAREMIND LEARNED")
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
# STEP 6: TEST A FUTURE FAILURE
# ============================================================

print("\n============================================================")
print("TESTING FUTURE FAILURE")
print("============================================================")

future_failure = """
IoT Controller Z60
Device Type: Embedded Controller
Temperature: 88°C
Voltage: 12.9V
Current: 1.9A
Symptoms: Overheating and intermittent sensor readings
Sensor Status: Intermittent
Communication Status: Normal
"""

print("\nFuture failure:")
print(future_failure)


# Search historical experiences
future_memories = search_similar_incidents(
    future_failure
)


print("\nHistorical incidents retrieved for future failure:")

for index, memory in enumerate(
    future_memories,
    start=1
):

    if isinstance(memory, dict):

        print(
            f"\n{index}. "
            f"{memory.get('incident_id')}"
        )

        print(
            f"   Root Cause: "
            f"{memory.get('root_cause')}"
        )

        print(
            f"   Fix: "
            f"{memory.get('fix')}"
        )


# ============================================================
# FINAL RESULT
# ============================================================

print("\n============================================================")
print("FINAL RESULT")
print("============================================================")

if learned_incident:

    print("SUCCESS!")

    print(
        "HardwareMind successfully learned "
        "from the confirmed hardware failure."
    )

    print(
        "The learned experience is stored "
        "for future investigations."
    )

else:

    print("LEARNING VERIFICATION FAILED.")


print("============================================================")