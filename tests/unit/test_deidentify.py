from services.pipeline.src.stages.deidentify import deidentify


def test_deidentify_replaces_phi():
    text = "Patient email is test@example.com and phone is 9876543210. Visit date: 21/09/2026."

    deid_text, phi_map = deidentify(text)

    assert "test@example.com" not in deid_text
    assert "9876543210" not in deid_text
    assert "21/09/2026" not in deid_text

    assert "[EMAIL_1]" in deid_text
    assert "[PHONE_2]" in deid_text
    assert "[DATE_3]" in deid_text

    assert phi_map["[EMAIL_1]"] == "test@example.com"
    assert phi_map["[PHONE_2]"] == "9876543210"
    assert phi_map["[DATE_3]"] == "21/09/2026"


if __name__ == "__main__":
    test_deidentify_replaces_phi()
    print("De-identification test: PASSED")
