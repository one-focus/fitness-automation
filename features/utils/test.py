from datetime import datetime, timezone, timedelta

dt = datetime.now(timezone.utc) + timedelta(hours=3)

date = dt.strftime('%H:%M:%S')
print(date)
