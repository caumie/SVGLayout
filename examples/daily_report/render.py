"""作業日報のサンプルデータをレンダリングする。"""

from pathlib import Path

from svgreportbuilder import Data

from .template_spec import svg_report_template


data: Data = {
    "report": {"number": "DR-2026-0916-1043", "submit_date": "2026年9月16日"},
    "worker": {"department": "製造課", "name": "山田 太郎", "employee_number": "3187"},
    "work": {
        "date": "2026年9月16日",
        "weather": "晴れ",
        "shift": "日勤",
        "start": "8:00",
        "end": "17:00",
        "actual": "8:00",
        "break": "1:00",
        "place": "第2工場・組立ライン",
    },
    "tasks": [
        {"time": "8:00～10:00", "content": "部品の切断・加工", "job_number": "A-101", "hours": "2:00"},
        {"time": "10:00～12:00", "content": "組立作業", "job_number": "A-102", "hours": "2:00"},
        {"time": "13:00～15:00", "content": "検査・寸法確認", "job_number": "A-103", "hours": "2:00"},
        {"time": "15:00～17:00", "content": "梱包・出荷準備", "job_number": "A-104", "hours": "2:00"},
    ],
    "materials": [
        {"name": "アルミ板", "spec": "A5052 t2.0", "quantity": 5, "unit": "枚", "note": ""},
        {"name": "ボルト", "spec": "M6×20", "quantity": 20, "unit": "個", "note": ""},
        {"name": "潤滑油", "spec": "L-100", "quantity": 0.1, "unit": "L", "note": "メンテナンス用"},
    ],
    "machines": [
        {"name": "NC切断機", "model": "NC-3000", "hours": "2:00", "note": ""},
        {"name": "ボール盤", "model": "BD-450", "hours": "2:00", "note": ""},
        {"name": "組立ライン", "model": "AL-1", "hours": "4:00", "note": "異常なし"},
    ],
    "allocation": [
        {"name": "加工", "hours": "2:00"},
        {"name": "組立", "hours": "2:00"},
        {"name": "検査", "hours": "2:00"},
        {"name": "梱包", "hours": "2:00"},
        {"name": "合計", "hours": "8:00"},
    ],
    "notes": "特になし。組立ラインの安全カバーを清掃し、次班へ引き継いだ。",
    "approval": {"leader": "佐藤", "date": "2026年9月16日"},
}


if __name__ == "__main__":
    output_path = Path(__file__).with_name("output.svg")
    output_path.write_text(svg_report_template.render(data), encoding="utf-8")
    print(output_path)
