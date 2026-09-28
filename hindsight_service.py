import os
import json
import re
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

API_KEY = os.getenv("HINDSIGHT_API_KEY")
BASE_URL = "https://api.hindsight.vectorize.io"
BANK_ID = "hardwaremind"

LOCAL_MEMORY_FILE = "local_memory.json"

client = None

if API_KEY:
    client = Hindsight(
        base_url=BASE_URL,
        api_key=API_KEY
    )


def _save_local_memory(incident):
    """Save one incident locally without duplicates."""

    memories = []

    if os.path.exists(LOCAL_MEMORY_FILE):
        try:
            with open(LOCAL_MEMORY_FILE, "r", encoding="utf-8") as file:
                memories = json.load(file)
        except (json.JSONDecodeError, OSError):
            memories = []

    incident_id = incident.get("incident_id")

    # Remove older copy of the same incident
    memories = [
        memory
        for memory in memories
        if memory.get("incident_id") != incident_id
    ]

    # Add latest version
    memories.append(incident)

    with open(LOCAL_MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memories, file, indent=4)

    print("Incident saved to local development memory.")


def _load_local_memory():
    """Load all locally stored incidents."""

    if not os.path.exists(LOCAL_MEMORY_FILE):
        return []

    try:
        with open(LOCAL_MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def store_incident(incident):
    """Store a hardware failure incident."""

    content = f"""
Hardware Failure Incident

Incident ID: {incident.get("incident_id")}
Device: {incident.get("device")}
Device Type: {incident.get("device_type")}

Temperature: {incident.get("temperature")}
Voltage: {incident.get("voltage")}
Current: {incident.get("current")}

Symptoms: {incident.get("symptoms")}
Sensor Status: {incident.get("sensor_status")}
Communication Status: {incident.get("communication_status")}

Root Cause: {incident.get("root_cause")}
Fix Applied: {incident.get("fix")}
Outcome: {incident.get("outcome")}
"""

    # Try real Hindsight
    if client:
        try:
            result = client.retain(
                bank_id=BANK_ID,
                content=content
            )

            print("Incident stored in Hindsight.")

            return {
                "success": True,
                "source": "hindsight",
                "result": result
            }

        except Exception as error:
            print(f"Hindsight unavailable: {error}")
            print("Using local development memory instead.")

    # Local fallback
    _save_local_memory(incident)

    return {
        "success": True,
        "source": "local",
        "result": None
    }


def search_similar_incidents(query):
    """Search previous hardware incidents."""

    # Try real Hindsight
    if client:
        try:
            result = client.recall(
                bank_id=BANK_ID,
                query=query
            )

            memories = []

            for memory in result.results:
                memories.append(memory.text)

            print(f"Found {len(memories)} memories in Hindsight.")

            return memories

        except Exception as error:
            print(f"Hindsight recall unavailable: {error}")
            print("Searching local development memory instead.")

    # Local fallback
    incidents = _load_local_memory()

    query_lower = str(query).lower()

    matches = []

    # Important hardware keywords
    keywords = [
        "overheating",
        "overheated",
        "temperature",
        "sensor",
        "intermittent",
        "voltage",
        "power",
        "shutdown",
        "reset",
        "communication",
        "thermal",
        "regulator",
        "heatsink"
    ]

    for incident in incidents:

        incident_text = json.dumps(
            incident
        ).lower()

        score = 0

        # Keyword similarity
        for keyword in keywords:
            if keyword in query_lower and keyword in incident_text:
                score += 2

        # Temperature similarity
        query_temperatures = re.findall(
            r"(\d+(?:\.\d+)?)\s*°?c",
            query_lower
        )

        # Convert numeric temperature to string
        incident_temperature = str(
            incident.get("temperature", "")
        ).lower()

        incident_temperatures = re.findall(
            r"(\d+(?:\.\d+)?)\s*°?c",
            incident_temperature
        )

        if query_temperatures and incident_temperatures:

            query_temp = float(query_temperatures[0])
            incident_temp = float(incident_temperatures[0])

            if abs(query_temp - incident_temp) <= 5:
                score += 3

        # Voltage similarity
        query_voltages = re.findall(
            r"(\d+(?:\.\d+)?)\s*v",
            query_lower
        )

        # Convert numeric voltage to string
        incident_voltage = str(
            incident.get("voltage", "")
        ).lower()

        incident_voltages = re.findall(
            r"(\d+(?:\.\d+)?)\s*v",
            incident_voltage
        )

        if query_voltages and incident_voltages:

            query_voltage = float(query_voltages[0])
            incident_voltage_value = float(
                incident_voltages[0]
            )

            if abs(
                query_voltage - incident_voltage_value
            ) <= 0.5:
                score += 3

        # Current similarity
        query_currents = re.findall(
            r"(\d+(?:\.\d+)?)\s*a",
            query_lower
        )

        incident_current = str(
            incident.get("current", "")
        ).lower()

        incident_currents = re.findall(
            r"(\d+(?:\.\d+)?)\s*a",
            incident_current
        )

        if query_currents and incident_currents:

            query_current = float(query_currents[0])
            incident_current_value = float(
                incident_currents[0]
            )

            if abs(
                query_current - incident_current_value
            ) <= 0.3:
                score += 2

        if score > 0:
            matches.append(
                {
                    "incident": incident,
                    "score": score
                }
            )

    # Highest similarity first
    matches.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return [
        item["incident"]
        for item in matches[:3]
    ]


def get_memory_context(current_failure):
    """
    Retrieve relevant past hardware failures and format them
    as context for the AI diagnosis system.
    """

    memories = search_similar_incidents(current_failure)

    if not memories:
        return "No similar historical hardware failures were found."

    context = "Relevant historical hardware failures:\n\n"

    for index, memory in enumerate(memories, start=1):

        context += f"--- Historical Incident {index} ---\n"

        if isinstance(memory, dict):

            context += f"Incident ID: {memory.get('incident_id')}\n"
            context += f"Device: {memory.get('device')}\n"
            context += f"Symptoms: {memory.get('symptoms')}\n"
            context += f"Root Cause: {memory.get('root_cause')}\n"
            context += f"Fix Applied: {memory.get('fix')}\n"
            context += f"Outcome: {memory.get('outcome')}\n"

        else:

            context += str(memory) + "\n"

        context += "\n"

    return context


def learn_from_resolution(
    incident,
    confirmed_root_cause,
    confirmed_fix,
    outcome
):
    """
    Store the confirmed result of a hardware failure investigation.
    This allows HardwareMind to learn from new failures.
    """

    learned_incident = incident.copy()

    learned_incident["root_cause"] = confirmed_root_cause
    learned_incident["fix"] = confirmed_fix
    learned_incident["outcome"] = outcome

    print("\nLearning from confirmed resolution...")

    result = store_incident(learned_incident)

    print("New hardware experience stored.")

    return result