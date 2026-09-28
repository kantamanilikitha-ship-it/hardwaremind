from diagnosis_engine import diagnose_hardware_failure


current_failure = """
Device: IoT Controller Z30
Device Type: Embedded Controller
Temperature: 86°C
Voltage: 12.8V
Current: 1.8A
Symptoms: Device overheating and intermittent sensor readings
Sensor Status: Intermittent
Communication Status: Normal
"""


print("========== HARDWAREMIND AI DIAGNOSIS TEST ==========")

print("\nCURRENT FAILURE:")
print(current_failure)

print("\nRunning AI diagnosis...\n")

result = diagnose_hardware_failure(current_failure)

print("========== AI DIAGNOSIS ==========")
print(result["diagnosis"])

print("\n========== MEMORY PROVIDED TO AI ==========")
print(result["memory_context"])

print("\n========== TEST COMPLETE ==========")