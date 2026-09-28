from diagnosis_engine import diagnose_hardware_failure


# A NEW failure after HardwareMind has already learned HW-007
future_failure = """
Device: IoT Controller Z50
Device Type: Embedded Controller
Temperature: 87°C
Voltage: 12.8V
Current: 1.8A
Symptoms: Controller is overheating and sensor readings are becoming intermittent
Sensor Status: Intermittent
Communication Status: Normal
"""


print("==============================================")
print("       FUTURE FAILURE TEST")
print("==============================================")


print("\nNEW FAILURE:")
print(future_failure)


print("\n[1] Searching learned memory and running AI diagnosis...\n")


result = diagnose_hardware_failure(future_failure)


print("========== AI DIAGNOSIS ==========")
print(result["diagnosis"])


print("\n========== MEMORY USED BY AI ==========")
print(result["memory_context"])


print("\n==============================================")
print("       FUTURE FAILURE TEST COMPLETE")
print("==============================================")