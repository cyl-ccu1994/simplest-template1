# 🧾 Python Analysis Simplest Template — 自動批改版

這是一個簡單的 Python 專案，用來：
- 讓學生練習 `input()` 輸入
- 輸出成 `data/submissions.txt`
- 🚀 GitHub Actions 自動批改

---

## 📌 學生使用方式

1. 執行程式：
   ```bash
   python input_info.py
   ```

2. 依序輸入：
   - 年月日（例如：2025-10-21）
   - 姓名（例如：王小明）
   - 學號（例如：s1234567）

3. 程式會自動產生：
   ```
   data/submissions.txt
   ```

4. push 回 GitHub，Actions 會自動批改 ✅

---

## 📊 評分檢查項目

- ✅ 是否有輸出檔案
- ✅ 檔案是否不為空
- ✅ 格式是否包含三個欄位（日期、姓名、學號）
