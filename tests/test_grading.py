from pathlib import Path

def test_output_file_exists():
    """檢查是否有輸出檔案"""
    assert Path("data/submissions.txt").exists(), "❌ 沒有找到 data/submissions.txt"

def test_output_file_not_empty():
    """檢查輸出檔案是否不為空"""
    content = Path("data/submissions.txt").read_text(encoding="utf-8").strip()
    assert content != "", "❌ 輸出檔案是空的"

def test_output_format():
    """檢查輸出格式是否包含三個欄位"""
    content = Path("data/submissions.txt").read_text(encoding="utf-8").strip().split("\n")
    first_line = content[-1]
    parts = first_line.split("\t")
    assert len(parts) >= 3, "❌ 格式錯誤，請確保有 日期、姓名、學號 三個欄位"
