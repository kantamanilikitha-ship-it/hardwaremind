import csv

from hindsight_service import store_incident


DATASET_FILE = "hardware_failures.csv"


def load_dataset():
    incidents = []

    with open(
        DATASET_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            incident = {
                "incident_id": row["incident_id"],
                "device": row["device"],
                "device_type": row["device_type"],
                "temperature": row["temperature"],
                "voltage": row["voltage"],
                "current": row["current"],
                "symptoms": row["symptoms"],
                "sensor_status": row["sensor_status"],
                "communication_status": row["communication_status"],
                "root_cause": row["root_cause"],
                "fix": row["fix_applied"],
                "outcome": row["outcome"],
            }

            incidents.append(incident)

    return incidents


def seed_hindsight():

    incidents = load_dataset()

    print()
    print("============================================================")
    print("HARDWAREMIND DATASET -> HINDSIGHT")
    print("============================================================")

    print(f"Dataset incidents found: {len(incidents)}")

    successful = 0
    failed = 0

    for index, incident in enumerate(incidents, start=1):

        print(
            f"\n[{index}/{len(incidents)}] "
            f"Storing {incident['incident_id']}..."
        )

        try:

            result = store_incident(incident)

            if result.get("success"):

                successful += 1

                print(
                    f"SUCCESS: {incident['incident_id']} "
                    f"-> {result.get('source')}"
                )

            else:

                failed += 1

                print(
                    f"FAILED: {incident['incident_id']}"
                )

        except Exception as error:

            failed += 1

            print(
                f"ERROR: {incident['incident_id']}: {error}"
            )

    print()
    print("============================================================")
    print("SEEDING COMPLETE")
    print("============================================================")

    print(f"Total incidents: {len(incidents)}")
    print(f"Successfully stored: {successful}")
    print(f"Failed: {failed}")

    print("============================================================")


if __name__ == "__main__":
    seed_hindsight()
    