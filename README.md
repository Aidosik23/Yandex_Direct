# 📊 Yandex Direct Report Downloader

Скрипт на Python для получения отчётов из API Яндекс.Директа и сохранения их в Excel-таблицу.

## 📌 Назначение

Этот скрипт позволяет автоматически запрашивать отчёты по рекламным кампаниям через [API Yandex Direct](https://yandex.ru/dev/direct/), обрабатывает их и сохраняет в формате `.xlsx`.

## ⚙️ Используемые параметры

- **[ReportType](https://yandex.ru/dev/direct/doc/ru/type)** — тип отчёта (например, `CAMPAIGN_PERFORMANCE_REPORT`). Влияет на набор доступных полей и группировку данных.
- **[FieldNames](https://yandex.ru/dev/direct/doc/ru/report-format)** — список полей, которые будут включены в отчёт (например: `Date`, `CampaignName`, `Clicks`, `Cost`).
- **DateFrom / DateTo** — диапазон дат, указывается вручную в теле запроса.
- **Format** — формат данных. В коде используется `TSV` (табличный формат с табуляцией), затем сохраняется в Excel.
- **[Несовместимые поля](https://yandex.ru/dev/direct/doc/ru/compatibility)** — важно сверяться при добавлении новых полей, чтобы избежать ошибок.
- **[Полный список полей](https://yandex.ru/dev/direct/doc/ru/fields-list)** — актуальный список всех доступных полей для разных типов отчётов.


## 📥 Установка зависимостей

Убедитесь, что у вас установлен Python 3. Затем установите зависимости:

```bash
pip install -r requirements.txt
