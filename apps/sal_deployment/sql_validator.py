import re
from datetime import datetime, timedelta

MAX_FILE_AGE_MONTHS = 12


def validate_path(file_path):
    """
    Validates:
    sal/deployment/SCT-1234/anything.sql
    """
    pattern = r"^sal/deployment/SCT-[0-9]+/.+\.sql$"
    if not re.match(pattern, file_path):
        raise ValueError(f"Invalid path structure: {file_path}")


def validate_filename(filename):
    """
    Validates:
    name_YYYY_MM_DD_v1.sql
    """
    pattern = r".+_\d{4}_\d{2}_\d{2}_v\d+\.sql$"
    if not re.match(pattern, filename):
        raise ValueError(f"Invalid filename format: {filename}")


def extract_date(filename):
    """
    Extracts YYYY_MM_DD from filename
    """
    match = re.search(r"(\d{4}_\d{2}_\d{2})", filename)
    if not match:
        raise ValueError("Date not found in filename")

    date_str = match.group(1)

    try:
        return datetime.strptime(date_str, "%Y_%m_%d")
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")


def validate_not_future(date):
    if date.date() > datetime.utcnow().date():
        raise ValueError("Date in filename is in the future")


def validate_file_age(date):
    max_age = datetime.utcnow() - timedelta(days=MAX_FILE_AGE_MONTHS * 30)
    if date < max_age:
        raise ValueError("SQL file is older than allowed age")


def validate_sql_file(file_path):
    """
    Master validator (this is what Lambda will call later)
    """
    filename = file_path.split("/")[-1]

    validate_path(file_path)
    validate_filename(filename)

    file_date = extract_date(filename)
    validate_not_future(file_date)
    validate_file_age(file_date)

    return {
        "file": file_path,
        "date": file_date.strftime("%Y-%m-%d"),
        "status": "VALID"
    }
