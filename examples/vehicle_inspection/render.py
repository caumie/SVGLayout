"""車両点検表のサンプルデータをレンダリングする。"""

from pathlib import Path

from svgreportbuilder import Data

from .template_spec import svg_report_template


data: Data = {
    "inspection": {
        "date": "2026年9月16日",
        "type": "始業前点検",
        "time": "8:00 ～ 8:20",
        "record_number": "VI-2026-0916-04",
        "next_date": "2026年10月1日",
    },
    "vehicle": {
        "id": "TR-0123",
        "type": "2t冷凍トラック",
        "registration": "品川100 あ1234",
        "driver": "山田 太郎",
        "mileage": "125,430 km",
    },
    "people": {"inspector": "山田 太郎", "manager": "鈴木 一郎"},
    "items": [
        {"category": "外観・車体", "name": "車体の損傷・変形", "status": "○", "status_fill": "#e7f5ec", "remarks": ""},
        {"category": "外観・車体", "name": "ガラス・ミラーの損傷", "status": "○", "status_fill": "#e7f5ec", "remarks": ""},
        {"category": "外観・車体", "name": "ナンバープレート", "status": "○", "status_fill": "#e7f5ec", "remarks": ""},
        {"category": "タイヤ・足回り", "name": "タイヤの空気圧", "status": "△", "status_fill": "#fff3cd", "remarks": "左前を補充"},
        {"category": "タイヤ・足回り", "name": "タイヤの摩耗・亀裂", "status": "○", "status_fill": "#e7f5ec", "remarks": ""},
        {"category": "タイヤ・足回り", "name": "ホイールナットの緩み", "status": "○", "status_fill": "#e7f5ec", "remarks": ""},
        {"category": "灯火・電装", "name": "ヘッドライト", "status": "○", "status_fill": "#e7f5ec", "remarks": ""},
        {"category": "灯火・電装", "name": "ウィンカー・ハザード", "status": "○", "status_fill": "#e7f5ec", "remarks": ""},
        {"category": "灯火・電装", "name": "ブレーキランプ", "status": "○", "status_fill": "#e7f5ec", "remarks": ""},
        {"category": "エンジン・油脂", "name": "始動・異音", "status": "○", "status_fill": "#e7f5ec", "remarks": ""},
        {"category": "エンジン・油脂", "name": "エンジンオイル", "status": "○", "status_fill": "#e7f5ec", "remarks": ""},
        {"category": "エンジン・油脂", "name": "冷却水（LLC）", "status": "○", "status_fill": "#e7f5ec", "remarks": ""},
        {"category": "制動・操舵", "name": "ブレーキの効き", "status": "○", "status_fill": "#e7f5ec", "remarks": ""},
        {"category": "制動・操舵", "name": "パーキングブレーキ", "status": "○", "status_fill": "#e7f5ec", "remarks": ""},
        {"category": "制動・操舵", "name": "ハンドルの遊び", "status": "○", "status_fill": "#e7f5ec", "remarks": ""},
    ],
    "notes": "タイヤ空気圧の左右差を確認し、左前輪へ補充。次回点検時に再確認する。",
}


if __name__ == "__main__":
    output_path = Path(__file__).with_name("output.svg")
    output_path.write_text(svg_report_template.render(data), encoding="utf-8")
    print(output_path)
