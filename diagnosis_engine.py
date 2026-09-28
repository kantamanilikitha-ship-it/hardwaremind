import os
from dotenv import load_dotenv
from groq import Groq

from hindsight_service import get_memory_context


# Load environment variables
load_dotenv()

# Get Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY was not found in .env")

# Create Groq client
client = Groq(api_key=GROQ_API_KEY)


def diagnose_hardware_failure(current_failure):
    """
    Analyze a hardware failure using the current failure
    and relevant historical failures from memory.
    """

    # Ask Member 2 memory layer for relevant past failures
    memory_context = get_memory_context(current_failure)

    # Create the AI prompt
    prompt = f"""
You are HardwareMind, an AI hardware failure investigation assistant.

Your job is to help an engineer diagnose an embedded or IoT hardware failure.

CURRENT HARDWARE FAILURE:
{current_failure}

HISTORICAL HARDWARE EXPERIENCES:
{memory_context}

Use both the current failure and the historical experiences
to investigate the problem.

Do not blindly copy a previous diagnosis.
Use historical incidents as supporting evidence.

Provide your answer using exactly these sections:

LIKELY ROOT CAUSE:
Give the most likely root cause.

EVIDENCE:
Explain the important evidence from the current failure
and relevant historical incidents.

RECOMMENDED TESTS:
1. Give the first diagnostic test.
2. Give the second diagnostic test.
3. Give the third diagnostic test.

RECOMMENDED FIX:
Give the recommended corrective action.

CONFIDENCE:
Choose High, Medium, or Low.

HISTORICAL REFERENCE:
Mention which historical incidents were useful and explain why.
"""

    # Send the prompt to the AI
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional hardware failure "
                    "investigation assistant. "
                    "Give concise and evidence-based engineering analysis."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    # Extract AI response
    diagnosis = response.choices[0].message.content

    return {
        "diagnosis": diagnosis,
        "memory_context": memory_context
    }