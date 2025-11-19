# Automated Sales Performance Reporting System
**Deliverables included in this package**

## 1. Overview
Sistem otomatis untuk mengumpulkan, memproses, dan melaporkan data penjualan harian:
- ETL (Python)
- Penyimpanan hasil ke database / CSV
- Generator laporan (PDF/text)
- Pengiriman otomatis via email
- Dashboard mockup (image)

## 2. Arsitektur Singkat
Data Source → ETL Script (etl.py) → Output (database/CSV) → report_generator.py → Email Sender (email_sender.py) → Dashboard

## 3. File dalam folder
- README.md (petunjuk singkat)
- docs/project_documentation.md (this file)
- scripts/etl.py
- scripts/report_generator.py
- scripts/email_sender.py
- data/sample_sales.csv
- data/dashboard_sample.csv
- assets/dashboard_mock.png

## 4. Cara jalanin (local)
1. Pastikan Python 3.8+ terinstall dan dependencies: pandas, sqlalchemy, matplotlib
2. Jalankan: `python scripts/etl.py data/sample_sales.csv data/processed_sales.csv`
3. Jalankan: `python scripts/report_generator.py data/processed_sales.csv output/report_daily.txt`
4. Jalankan: `python scripts/email_sender.py output/report_daily.txt` (sesuaikan kredensial)

## 5. Catatan keamanan
Jangan menyimpan password langsung di script dalam produksi. Gunakan secret manager atau environment variables.

## 6. Kontak
Kamu bisa modifikasi script sesuai kebutuhan: scheduling (cron), Docker, dan integrasi ke BI tools seperti Power BI atau Looker Studio.
