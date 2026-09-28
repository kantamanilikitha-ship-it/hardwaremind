from hindsight_service import get_memory_context


current_failure = """
IoT Controller Z25 is overheating at 84°C.
Voltage is 12.7V.
Current is 1.7A.
Sensor readings are intermittent.
Communication is normal.
"""


print("========== HARDWAREMIND MEMORY CONTEXT TEST ==========")

memory_context = get_memory_context(current_failure)

print("\nGenerated memory context:\n")
print(memory_context)

print("\n========== TEST COMPLETE ==========")