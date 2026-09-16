"""印刷工程進行票のサンプルデータをレンダリングする。"""

from pathlib import Path

from svgreportbuilder import Data

from .template_spec import svg_report_template


data: Data = {
    "job": {
        "number": "P-260916-042",
        "created_date": "2026年9月16日",
        "customer": "○○出版株式会社",
        "product": "秋号パンフレット",
        "due_date": "9月20日 午前",
        "specification": "A4 / 24P / 中綴じ",
        "quantity": "3,000部",
        "operator": "佐藤",
        "note": "表紙は色校正の承認後に本刷りへ進む。",
    },
    "processes": [
        {"name": "入稿・プリフライト", "status": "完了", "status_fill": "#e7f5ec", "plan": "9/16", "actual": "9/16", "operator": "佐藤／PDF・フォント確認"},
        {"name": "面付・RIP", "status": "完了", "status_fill": "#e7f5ec", "plan": "9/16", "actual": "9/16", "operator": "田中／8面付"},
        {"name": "校正", "status": "完了", "status_fill": "#e7f5ec", "plan": "9/17", "actual": "9/17", "operator": "鈴木／校了"},
        {"name": "用紙・資材", "status": "準備済", "status_fill": "#e7f5ec", "plan": "9/17", "actual": "9/17", "operator": "中村"},
        {"name": "印刷", "status": "完了", "status_fill": "#e7f5ec", "plan": "9/18", "actual": "9/18 13:30", "operator": "4色機 #2"},
        {"name": "後加工", "status": "進行中", "status_fill": "#fff3cd", "plan": "9/19", "actual": "", "operator": "中綴じ・三方断裁"},
        {"name": "出荷・納品", "status": "未着手", "status_fill": "#f1f3f5", "plan": "9/20", "actual": "", "operator": "自社便"},
    ],
    "materials": [
        {"name": "本文用紙", "spec": "マット90kg", "quantity": "3,240枚"},
        {"name": "表紙用紙", "spec": "コート135kg", "quantity": "3,120枚"},
        {"name": "針金", "spec": "No.18", "quantity": "3,100本"},
    ],
    "shipping": {"method": "自社便", "destination": "本社3F", "time": "10:00まで"},
    "output": {"printed": 3120, "good": 3042, "spare": 42, "waste": 36, "boxes": 6, "weight": "86kg", "slip": "同梱"},
    "notes": "後加工後に良品数を再確認し、6箱へ500部ずつ梱包する。",
    "final_check": "校正紙・刷了数・納品先を照合済み。",
    "people": {"inspector": "高橋", "packer": "中村", "shipper": ""},
}


if __name__ == "__main__":
    output_path = Path(__file__).with_name("output.svg")
    output_path.write_text(svg_report_template.render(data), encoding="utf-8")
    print(output_path)
