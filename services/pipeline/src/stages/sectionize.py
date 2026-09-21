import re


SECTION_HEADERS = {
    "discharge summary": "discharge_summary",
    "medications": "medications",
    "follow-up": "follow_up",
    "history": "history",
    "assessment": "assessment",
    "plan": "plan",
}


def sectionize(text):
    matches = []

    pattern = re.compile(
        r"(?im)^(discharge summary|medications|follow-up|history|assessment|plan)\s*$"
    )

    for match in pattern.finditer(text):
        header = match.group(1).strip().lower()
        section_name = SECTION_HEADERS[header]

        matches.append({
            "section": section_name,
            "header_end": match.end(),
        })

    sections = []

    for index, match in enumerate(matches):
        raw_start = match["header_end"]

        if index + 1 < len(matches):
            raw_end = matches[index + 1]["header_end"]
            next_header_start = matches[index + 1]["header_end"]

            next_match = pattern.search(text, raw_start)
            if next_match:
                raw_end = next_match.start()
        else:
            raw_end = len(text)

        start = raw_start
        end = raw_end

        while start < end and text[start] in "\r\n":
            start += 1

        while end > start and text[end - 1] in "\r\n":
            end -= 1

        sections.append({
            "section": match["section"],
            "start": start,
            "end": end,
            "text": text[start:end],
        })

    return sections


if __name__ == "__main__":
    sample = """DISCHARGE SUMMARY
Patient presented with pneumonia and fever.

MEDICATIONS
Amoxicillin was prescribed.

FOLLOW-UP
Follow up in one week.
"""

    sections = sectionize(sample)

    for section in sections:
        print(section)
