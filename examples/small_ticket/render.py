"""変形小型伝票のサンプルデータをレンダリングする。"""

from pathlib import Path

from svgreportbuilder import Data

from .template_spec import svg_report_template


data: Data = {
    "ticket": {"number": "028734", "date": "2026 / 9 / 16"},
    "customer": {"name": "田中"},
    "order": {
        "item": "ジャケット（紺）",
        "short_item": "JACKET",
        "quantity": 1,
        "amount": "¥ 2,800",
        "due_date": "2026 / 9 / 20",
        "due_date_short": "9 / 20",
    },
    "services": [{"mark": "✓"}, {"mark": ""}, {"mark": ""}, {"mark": ""}],
    "payments": [{"mark": ""}, {"mark": "✓"}, {"mark": ""}],
    "staff": {"received_by": "M.S."},
}


if __name__ == "__main__":
    output_path = Path(__file__).with_name("output.svg")
    output_path.write_text(svg_report_template.render(data), encoding="utf-8")
    print(output_path)
