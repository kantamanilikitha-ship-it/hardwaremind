from hindsight_service import search_similar_incidents


print("========== HARDWAREMIND RECALL TEST ==========")

new_failure = """
New hardware failure:

Device: IoT Controller Z25
Device Type: Embedded Controller
Temperature: 84°C
Voltage: 12.7V
Current: 1.7A

Symptoms:
The device is overheating and sensor readings are intermittent.

Sensor Status:
Intermittent

Communication Status:
Normal

Find previous hardware failures that are similar
to this problem. Pay particular attention to
overheating, intermittent sensors, and voltage
around 12-13V.
"""


print("\nCurrent failure:")
print(new_failure)

print("\nSearching historical memory...")

memories = search_similar_incidents(new_failure)

print(f"\nFound {len(memories)} similar incident(s).")


for index, memory in enumerate(memories, start=1):

    print(f"\n========== SIMILAR INCIDENT {index} ==========")

    print(memory)


print("\n========== RECALL TEST COMPLETE ==========")