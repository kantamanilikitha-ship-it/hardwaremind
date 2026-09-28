from diagnosis_engine import diagnose_hardware_failure
from hindsight_service import learn_from_resolution


def investigate_failure(current_incident):
    """
    Complete HardwareMind investigation workflow.

    Member 2:
        Retrieves relevant historical hardware failures.

    Member 3:
        Uses the historical failures + current failure
        to generate an AI diagnosis.
    """

    # Convert the incident into text for the AI
    failure_text = f"""
Incident ID: {current_incident.get('incident_id')}
Device: {current_incident.get('device')}
Device Type: {current_incident.get('device_type')}
Temperature: {current_incident.get('temperature')}°C
Voltage: {current_incident.get('voltage')}V
Current: {current_incident.get('current')}A
Symptoms: {current_incident.get('symptoms')}
Sensor Status: {current_incident.get('sensor_status')}
Communication Status: {current_incident.get('communication_status')}
"""

    print("\n========================================")
    print("HARDWAREMIND INVESTIGATION")
    print("========================================")

    print("\nCurrent Failure:")
    print(failure_text)

    # Member 3 AI diagnosis
    result = diagnose_hardware_failure(failure_text)

    print("\n========================================")
    print("AI DIAGNOSIS")
    print("========================================")

    print(result["diagnosis"])

    print("\n========================================")
    print("HISTORICAL MEMORY USED")
    print("========================================")

    print(result["memory_context"])

    return result


def learn_from_confirmed_resolution(
    current_incident,
    confirmed_root_cause,
    confirmed_fix,
    outcome
):
    """
    Send the engineer-confirmed result back to Member 2.

    This closes the learning loop:
    
    Failure
        ↓
    AI Diagnosis
        ↓
    Engineer Confirmation
        ↓
    Memory
    """

    print("\n========================================")
    print("LEARNING FROM CONFIRMED RESOLUTION")
    print("========================================")

    result = learn_from_resolution(
        current_incident,
        confirmed_root_cause,
        confirmed_fix,
        outcome
    )

    print("Learning result:")
    print(result)

    return result