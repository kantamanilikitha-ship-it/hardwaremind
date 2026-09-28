from hindsight_service import search_similar_incidents


# ============================================================
# TEST: CAN HINDSIGHT REMEMBER THE PREVIOUSLY STORED FAILURE?
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
print("HARDWAREMIND HINDSIGHT LEARNING TEST")
print("============================================================")

print("\nNew future failure:")
print(future_failure)


# Ask Hindsight for similar historical experiences
memories = search_similar_incidents(future_failure)


print("\n============================================================")
print("HINDSIGHT MEMORIES RETRIEVED")
print("============================================================")


if memories:

    for index, memory in enumerate(memories, start=1):

        print(f"\n--- Memory {index} ---")

        if isinstance(memory, dict):

            print(
                f"Incident ID: "
                f"{memory.get('incident_id')}"
            )

            print(
                f"Device: "
                f"{memory.get('device')}"
            )

            print(
                f"Root Cause: "
                f"{memory.get('root_cause')}"
            )

            print(
                f"Fix: "
                f"{memory.get('fix')}"
            )

            print(
                f"Outcome: "
                f"{memory.get('outcome')}"
            )

        else:

            print(memory)


else:

    print("No memories were retrieved.")


print("\n============================================================")
print("TEST RESULT")
print("============================================================")


found_hw009 = False

for memory in memories:

    if isinstance(memory, str):

        if "HW-009" in memory:
            found_hw009 = True

    elif isinstance(memory, dict):

        if memory.get("incident_id") == "HW-009":
            found_hw009 = True


if found_hw009:

    print("SUCCESS!")
    print("Hindsight remembered HW-009.")
    print("The stored hardware experience can be used")
    print("for a future hardware failure.")

else:

    print("HW-009 was not found in the retrieved memories.")

print("============================================================")