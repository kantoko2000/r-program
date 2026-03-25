from datetime import date, timedelta

# 2024年1月1日〜2025年12月31日まで
start_date = date(2024, 1, 1)
end_date = date(2030, 12, 31)

# 土曜日（weekday() == 5）を探す
saturdays = []
current_date = start_date
while current_date <= end_date:
    if current_date.weekday() == 5:
        saturdays.append(current_date.strftime('%Y%m%d'))
    current_date += timedelta(days=1)

# 全件出力
for s in saturdays:
    print(s)
