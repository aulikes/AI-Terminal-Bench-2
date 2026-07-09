import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")

EXPECTED_REPORT = {
    "total_requests": 6,
    "unique_ips": 3,
    "top_path": "/index.html",
}


def load_report():
    try:
        return json.loads(REPORT_PATH.read_text())
    except json.JSONDecodeError as exc:
        raise AssertionError("report.json is not valid JSON") from exc


def test_report_exists_and_is_valid_json():
    """Success criterion 1: /app/report.json exists and contains a valid JSON object."""
    assert REPORT_PATH.exists(), "no report.json found"
    assert REPORT_PATH.stat().st_size > 0, "report.json is empty"

    data = load_report()
    assert isinstance(data, dict), "report.json must contain a JSON object"


def test_report_has_exact_required_keys():
    """Success criterion 2: report.json contains exactly total_requests, unique_ips, and top_path."""
    data = load_report()
    assert set(data.keys()) == set(EXPECTED_REPORT.keys())


def test_report_has_expected_values():
    """Success criterion 3: report.json values match the expected summary computed from /app/access.log."""
    data = load_report()
    assert data == EXPECTED_REPORT