from pathlib import Path
import csv
import json

INPUT_FILE = Path("data/icd10cm/icd10_demo.csv")
OUTPUT_FILE = Path("data/icd10cm/icd10_records.json")

records = []

with INPUT_FILE.open("r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        records.append({
            "code": row["code"].strip(),
            "description": row["description"].strip()
        })

OUTPUT_FILE.write_text(
    json.dumps(records, indent=2),
    encoding="utf-8"
)

print(f"ICD-10 records processed: {len(records)}")
print(f"Output: {OUTPUT_FILE}")
