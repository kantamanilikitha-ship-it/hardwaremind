import os
import time
from dotenv import load_dotenv
from hindsight_client import Hindsight

# Load API key from .env
load_dotenv()

api_key = os.getenv("HINDSIGHT_API_KEY")

if not api_key:
    raise ValueError("HINDSIGHT_API_KEY was not found in .env")

# Connect to Hindsight
client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=api_key
)

# Our Hindsight memory bank
BANK_ID = "hardwaremind"

print("Connected to Hindsight!")

# Store a test hardware failure
print("Storing test memory...")

client.retain(
    bank_id=BANK_ID,
    content=(
        "Hardware incident HW-001: IoT controller overheated to 87°C. "
        "The voltage was 12.8V and the temperature sensor showed intermittent "
        "readings. Investigation found that the voltage regulator was overheating. "
        "The regulator was replaced and a thermal pad was added. "
        "The device worked successfully after the repair."
    )
)

print("Test memory stored!")

# Give Hindsight a few seconds to process the memory
print("Waiting for Hindsight to process the memory...")
time.sleep(5)

# Search our memory
print("Searching Hindsight memory...")

result = client.recall(
    bank_id=BANK_ID,
    query="What previous hardware failure involved overheating, unstable sensor readings and a voltage regulator?"
)

print("\n===== HINDSIGHT RESULTS =====")

for memory in result.results:
    print(memory.text)

print("\n===== TEST COMPLETE =====")