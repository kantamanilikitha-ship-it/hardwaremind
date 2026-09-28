from hindsight_service import get_memory_context

new_failure = (
    "A new IoT controller is overheating at 85°C with intermittent "
    "sensor readings. Voltage is 12.8V and communication is normal."
)

print("========== HARDWAREMIND LEARNING RECALL TEST ==========")

print("\nNew hardware failure:")
print(new_failure)

print("\nSearching historical memory...")

context = get_memory_context(new_failure)

print("\n===== RETRIEVED MEMORY =====")
print(context)

print("\n========== TEST COMPLETE ==========")