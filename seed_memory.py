from hindsight_service import store_incident


historical_incidents = [

    {
        "incident_id": "HW-001",
        "device": "IoT Controller X12",
        "device_type": "Embedded Controller",
        "temperature": "87°C",
        "voltage": "12.8V",
        "current": "1.8A",
        "symptoms": "Intermittent sensor readings and device overheating",
        "sensor_status": "Intermittent",
        "communication_status": "Normal",
        "root_cause": "Voltage regulator overheating",
        "fix": "Replaced voltage regulator and added thermal pad",
        "outcome": "Device operated successfully after repair"
    },

    {
        "incident_id": "HW-002",
        "device": "Industrial Gateway G20",
        "device_type": "IoT Gateway",
        "temperature": "52°C",
        "voltage": "10.9V",
        "current": "2.4A",
        "symptoms": "Random shutdowns and system resets during operation",
        "sensor_status": "Normal",
        "communication_status": "Intermittent",
        "root_cause": "Unstable power supply",
        "fix": "Replaced faulty power supply and checked voltage regulation",
        "outcome": "System remained stable during extended testing"
    },

    {
        "incident_id": "HW-003",
        "device": "Environmental Monitor E5",
        "device_type": "Sensor Controller",
        "temperature": "31°C",
        "voltage": "5.1V",
        "current": "0.6A",
        "symptoms": "Temperature readings were consistently incorrect",
        "sensor_status": "Faulty temperature sensor",
        "communication_status": "Normal",
        "root_cause": "Temperature sensor failure",
        "fix": "Replaced temperature sensor and recalibrated the device",
        "outcome": "Temperature readings returned to expected values"
    },

    {
        "incident_id": "HW-004",
        "device": "Factory Node F8",
        "device_type": "Industrial IoT Node",
        "temperature": "44°C",
        "voltage": "12.1V",
        "current": "1.2A",
        "symptoms": "Device stopped communicating with the central gateway",
        "sensor_status": "Normal",
        "communication_status": "Communication lost",
        "root_cause": "Damaged communication interface",
        "fix": "Replaced communication interface component and verified connections",
        "outcome": "Communication restored successfully"
    },

    {
        "incident_id": "HW-005",
        "device": "Edge Controller C30",
        "device_type": "Embedded Controller",
        "temperature": "91°C",
        "voltage": "12.6V",
        "current": "2.1A",
        "symptoms": "Device overheated during high processing load",
        "sensor_status": "Normal",
        "communication_status": "Normal",
        "root_cause": "Poor thermal interface between processor and heatsink",
        "fix": "Reapplied thermal compound and improved heatsink mounting",
        "outcome": "Operating temperature reduced and device remained stable"
    }
]


print("========== HARDWAREMIND MEMORY SEED ==========")

for incident in historical_incidents:

    print(
        f"\nStoring {incident['incident_id']} "
        f"- {incident['device']}..."
    )

    result = store_incident(incident)

    print(
        f"Storage source: {result['source']}"
    )


print("\n========== SEEDING COMPLETE ==========")
print(
    f"Processed {len(historical_incidents)} historical incidents."
)