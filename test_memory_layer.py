from hindsight_service import store_incident, search_similar_incidents


test_incident = {
    "incident_id": "HW-001",
    "device": "IoT Controller X12",
    "device_type": "Embedded Controller",
    "temperature": "87°C",
    "voltage": "12.8V",
    "current": "1.8A",
    "symptoms": "Intermittent sensor readings and device overheating",
    "sensor_status": "Intermittent",
    "communication_status": "Normal",
    "root_cause": "Voltage regulator overheating",
    "fix": "Replaced voltage regulator and added thermal pad",
    "outcome": "Device operated successfully after repair"
}


print("========== HARDWAREMIND MEMORY TEST ==========")

# 1. Store an incident
print("\n1. Storing hardware incident...")

storage_result = store_incident(test_incident)

print(f"Storage source: {storage_result['source']}")


# 2. Search previous incidents
print("\n2. Searching previous hardware incidents...")

query = """
IoT controller is overheating around 85-90°C.
Sensor readings are intermittent.
Voltage is around 12.8V.
Find previous incidents involving overheating,
sensor problems and voltage regulator issues.
"""

memories = search_similar_incidents(query)


# 3. Display results
print(f"\nFound {len(memories)} matching incident(s).")

for index, memory in enumerate(memories, start=1):
    print(f"\n--- Matching Incident {index} ---")
    print(memory)


print("\n========== TEST COMPLETE ==========")