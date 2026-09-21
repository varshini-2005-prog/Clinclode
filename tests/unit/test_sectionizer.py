from services.pipeline.src.stages.sectionize import sectionize


def test_section_spans_are_preserved():
    text = """DISCHARGE SUMMARY
Patient presented with pneumonia and fever.

MEDICATIONS
Amoxicillin was prescribed.

FOLLOW-UP
Follow up in one week.
"""

    sections = sectionize(text)

    assert len(sections) == 3

    for section in sections:
        assert text[section["start"]:section["end"]] == section["text"]

    assert sections[0]["section"] == "discharge_summary"
    assert sections[1]["section"] == "medications"
    assert sections[2]["section"] == "follow_up"


if __name__ == "__main__":
    test_section_spans_are_preserved()
    print("Sectionizer span test: PASSED")
