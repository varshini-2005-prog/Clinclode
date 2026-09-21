import re


def deidentify(text):
    phi_map = {}
    counter = 1

    def replace_email(match):
        nonlocal counter
        key = f"[EMAIL_{counter}]"
        phi_map[key] = match.group(0)
        counter += 1
        return key

    def replace_phone(match):
        nonlocal counter
        key = f"[PHONE_{counter}]"
        phi_map[key] = match.group(0)
        counter += 1
        return key

    def replace_date(match):
        nonlocal counter
        key = f"[DATE_{counter}]"
        phi_map[key] = match.group(0)
        counter += 1
        return key

    text = re.sub(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
        replace_email,
        text
    )

    text = re.sub(
        r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\d{3}[-.\s]?)?\d{3}[-.\s]?\d{4}\b",
        replace_phone,
        text
    )

    text = re.sub(
        r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",
        replace_date,
        text
    )

    return text, phi_map


if __name__ == "__main__":
    sample = (
        "Patient email is test@example.com and phone is "
        "9876543210. Visit date: 21/09/2026."
    )

    deidentified, phi_map = deidentify(sample)

    print("De-identified text:")
    print(deidentified)
    print("PHI map:")
    print(phi_map)
