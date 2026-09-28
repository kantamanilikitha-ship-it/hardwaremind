from hardware_agent import investigate_failure


# Simulated new hardware failure
current_incident = {
    "incident_id": "HW-008",
    "device": "IoT Controller Z50",
    "device_type": "Embedded Controller",
    "temperature": 87,
    "voltage": 12.8,
    "current": 1.8,
    "symptoms": "Overheating and intermittent sensor readings",
    "sensor_status": "Intermittent",
    "communication_status": "Normal"
}


# Run the complete investigation
result = investigate_failure(current_incident)


print("\n========================================")
print("TEST COMPLETED")
print("========================================")

print("\nHardwareMind successfully connected:")

print("\nMember 2 → Memory retrieval")
print("Member 3 → AI diagnosis")

print("\nThe system is now able to investigate a hardware failure using")
print("historical hardware experiences.")