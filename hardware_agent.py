from diagnosis_engine import diagnose_hardware_failure
from hindsight_service import learn_from_resolution


def investigate_failure(current_incident):
    """
    Investigate a new hardware failure using
    Hindsight memory + Groq reasoning.
    """

    result = diagnose_hardware_failure(current_incident)

    return {
        "success": True,
        "diagnosis": result["diagnosis"],
        "memory_context": result["memory_context"]
    }


def learn_from_confirmed_resolution(
    current_incident,
    confirmed_root_cause,
    confirmed_fix,
    outcome
):
    """
    Store the engineer-confirmed hardware failure
    resolution back into Hindsight.
    """

    result = learn_from_resolution(
        current_incident,
        confirmed_root_cause,
        confirmed_fix,
        outcome
    )

    return {
        "success": True,
        "message": "HardwareMind learned from the confirmed resolution.",
        "memory_source": result.get("source")
    }