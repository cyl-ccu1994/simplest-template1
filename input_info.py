from datetime import datetime
from pathlib import Path

# 建立 data 資料夾
Path("data").mkdir(exist_ok=True)
outfile = Path("data/submissions.txt")

# 使用者輸入
date_str = input("請輸入日期（例如 2025-10-21）：")
name = input("請輸入姓名：")
student_id = input("請輸入學號（Student ID）：")

# 時間戳
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 寫入檔案
with open(outfile, "a", encoding="utf-8") as f:
    f.write(f"日期：{date_str}\t姓名：{name}\t學號：{student_id}\t時間戳：{timestamp}\n")

print(f"\n✅ 已儲存輸入資料至 {outfile}")
