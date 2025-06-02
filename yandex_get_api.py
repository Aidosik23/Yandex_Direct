#------------------------------------------------------------------------------------Таблица fact_account_stats — показатели на уровне аккаунта
import requests
import time
import pandas as pd
from io import StringIO

# --- Настройки ---
ReportsURL = "https://api.direct.yandex.com/json/v5/reports"
token = "token"
clientLogin = "login"
output_file = r"C:/python scripts/load_to_stg_raw/yandex_api/result/yandex_account_stats.xlsx"

# --- Заголовки ---
headers = {
    "Authorization": f"Bearer {token}",
    "Client-Login": clientLogin,
    "Accept-Language": "ru",
    "Content-Type": "application/json",
    "processingMode": "auto",
    "returnMoneyInMicros": "false",
    "skipReportHeader": "true",
    "skipColumnHeader": "false",
    "skipReportSummary": "true"
}

# --- Тело запроса ---
body = {
    "params": {
        "SelectionCriteria": {
            "DateFrom": "2024-01-01",
            "DateTo": "2025-12-01"
        },
        "FieldNames": [
            "Date",
            "Impressions",
            "Clicks",
            "Cost",
            "Ctr",
            "AvgCpc",
            "Conversions"
        ],
        "ReportName": "Account_Performance",
        "ReportType": "ACCOUNT_PERFORMANCE_REPORT",
        "DateRangeType": "CUSTOM_DATE",
        "Format": "TSV",
        "IncludeVAT": "NO"
    }
}

# --- Запрос отчёта (с ожиданием) ---
while True:
    response = requests.post(ReportsURL, json=body, headers=headers, verify=False)

    if response.status_code == 200:
        print("✅ Отчёт готов! Сохраняем в Excel...")

        report_data = StringIO(response.text)
        df = pd.read_csv(report_data, sep="\t", header=0)

        df.to_excel(output_file, index=False, engine="openpyxl")
        print(f"📂 Отчёт сохранён: {output_file}")
        break

    elif response.status_code == 201:
        print("🔄 Отчёт ещё формируется, ждём 5 секунд...")
        time.sleep(5)

    else:
        print(f"❌ Ошибка API: {response.status_code}")
        print(response.text)
        break
