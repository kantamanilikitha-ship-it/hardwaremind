import streamlit as st
import uuid

from hardware_agent import (
    investigate_failure,
    learn_from_confirmed_resolution
)

# ============================================================
# PAGE SETUP
# ============================================================

st.set_page_config(
    page_title="HardwareMind",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 AI-Powered Hardware Failure Investigator")

st.write(
    "Analyze hardware failures, review similar past incidents, "
    "and teach HardwareMind confirmed fixes."
)

# ============================================================
# BACKEND STATUS
# ============================================================

st.subheader("Backend Status")

if st.button("Check Backend Status"):
    try:
        st.success("HardwareMind backend is available.")

        st.json({
            "status": "online",
            "service": "HardwareMind",
            "memory": "Hindsight",
            "reasoning": "Groq"
        })

    except Exception as error:
        st.error(f"Backend check failed: {error}")

st.divider()

# ============================================================
# DEVICE INFORMATION / INVESTIGATION
# ============================================================

st.header("📋 Device Information")

with st.form("investigation_form"):

    left, right = st.columns(2)

    with left:

        incident_id = st.text_input(
            "Incident ID",
            value=f"HW-{uuid.uuid4().hex[:6].upper()}"
        )

        device = st.text_input(
            "Device",
            value="IoT Controller Z60"
        )

        device_type = st.selectbox(
            "Device Type",
            [
                "Embedded Controller",
                "IoT Sensor",
                "Power Supply"
            ]
        )

        temperature = st.number_input(
            "Temperature (°C)",
            value=88.0,
            step=1.0
        )

        voltage = st.number_input(
            "Voltage (V)",
            value=12.9,
            step=0.1
        )

    with right:

        current = st.number_input(
            "Current (A)",
            value=1.9,
            step=0.1
        )

        sensor_status = st.selectbox(
            "Sensor Status",
            [
                "Normal",
                "Intermittent",
                "Failed"
            ]
        )

        communication_status = st.selectbox(
            "Communication Status",
            [
                "Normal",
                "Unstable",
                "Disconnected"
            ]
        )

    symptoms = st.text_area(
        "Describe the symptoms",
        value="Overheating and intermittent sensor readings"
    )

    investigate_clicked = st.form_submit_button(
        "🔍 Analyze Failure"
    )

# ============================================================
# INVESTIGATION
# ============================================================

if investigate_clicked:

    payload = {
        "incident_id": incident_id.strip(),
        "device": device.strip(),
        "device_type": device_type,
        "temperature": temperature,
        "voltage": voltage,
        "current": current,
        "symptoms": symptoms.strip(),
        "sensor_status": sensor_status,
        "communication_status": communication_status
    }

    if (
        not payload["incident_id"]
        or not payload["device"]
        or not payload["symptoms"]
    ):

        st.error(
            "Please enter the Incident ID, Device, and Symptoms."
        )

    else:

        try:

            with st.spinner(
                "Investigating the failure..."
            ):

                result = investigate_failure(payload)

            if result.get("success", True):

                st.session_state[
                    "investigation_payload"
                ] = payload

                st.session_state[
                    "investigation_result"
                ] = result

                st.success(
                    "Investigation completed!"
                )

            else:

                st.error(
                    "The investigation was unsuccessful."
                )

                st.json(result)

        except Exception as error:

            st.error(
                f"Investigation failed: {error}"
            )

# ============================================================
# SHOW INVESTIGATION RESULT
# ============================================================

if "investigation_result" in st.session_state:

    result = st.session_state["investigation_result"]

    st.divider()

    st.header("🧠 Investigation Results")

    # --------------------------------------------------------
    # AI DIAGNOSIS
    # --------------------------------------------------------

    st.subheader("AI Diagnosis")

    if "diagnosis" in result:

        diagnosis = result["diagnosis"]

        if isinstance(
            diagnosis,
            (dict, list)
        ):

            st.json(diagnosis)

        else:

            st.write(diagnosis)

    else:

        st.info(
            "The response did not include a 'diagnosis' field."
        )

        st.json(result)

    # --------------------------------------------------------
    # HINDSIGHT MEMORY
    # --------------------------------------------------------

    st.subheader("Hindsight Memory Context")

    if "memory_context" in result:

        memory_context = result["memory_context"]

        if isinstance(
            memory_context,
            (dict, list)
        ):

            st.json(memory_context)

        else:

            st.write(memory_context)

    else:

        st.info(
            "The response did not include a 'memory_context' field."
        )

    # ========================================================
    # CONFIRM & TEACH
    # ========================================================

    st.divider()

    st.header("✅ Confirm & Teach")

    st.write(
        "After an engineer verifies the actual cause and repair, "
        "enter the confirmed details and submit them so "
        "HardwareMind can learn."
    )

    with st.form("learn_form"):

        confirmed_root_cause = st.text_input(
            "Confirmed root cause",
            placeholder="Example: Voltage regulator overheating"
        )

        confirmed_fix = st.text_area(
            "Confirmed fix",
            placeholder="Describe the repair that was actually completed"
        )

        outcome = st.text_area(
            "Outcome",
            placeholder="Describe how the device performed after repair"
        )

        teach_clicked = st.form_submit_button(
            "Confirm & Teach"
        )

    # ========================================================
    # LEARNING
    # ========================================================

    if teach_clicked:

        if (
            not confirmed_root_cause.strip()
            or not confirmed_fix.strip()
            or not outcome.strip()
        ):

            st.error(
                "Please fill in the confirmed root cause, "
                "fix, and outcome."
            )

        else:

            try:

                with st.spinner(
                    "Saving the confirmed resolution..."
                ):

                    learn_result = (
                        learn_from_confirmed_resolution(
                            st.session_state[
                                "investigation_payload"
                            ],
                            confirmed_root_cause.strip(),
                            confirmed_fix.strip(),
                            outcome.strip()
                        )
                    )

                if learn_result.get("success") is True:

                    st.success(
                        "HardwareMind learned from the confirmed resolution!"
                    )

                else:

                    st.error(
                        "HardwareMind did not confirm that learning succeeded."
                    )

                st.json(learn_result)

            except Exception as error:

                st.error(
                    f"Learning failed: {error}"
                )