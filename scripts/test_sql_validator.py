from apps.sal_deployment.sql_validator import validate_sql_file

test_files = [
    # ✅ valid
    "sal/deployment/SCT-1111/add_col_2026_01_27_v1.sql",

    # ❌ future date
    "sal/deployment/SCT-1111/add_col_2030_01_01_v1.sql",

    # ❌ too old (older than 12 months)
    "sal/deployment/SCT-1111/add_col_2023_01_01_v1.sql",

    # ❌ bad path
    "sal/deploy/SCT-1111/bad_path_2026_01_27_v1.sql",

    # ❌ bad filename
    "sal/deployment/SCT-1111/badname_v1.sql"
]

for file in test_files:
    try:
        result = validate_sql_file(file)
        print("✅ VALID:", result)
    except Exception as e:
        print("❌ INVALID:", file)
        print("   Reason:", e)
