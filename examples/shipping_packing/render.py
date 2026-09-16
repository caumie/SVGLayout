"""出荷指示兼梱包明細書のサンプルデータをレンダリングする。"""

from pathlib import Path

from svgreportbuilder import Data

from .template_spec import svg_report_template


data: Data = {
    "document": {"number": "SP-2026-0916-07", "date": "2026年9月16日"},
    "customer": {
        "code": "10028",
        "name": "株式会社田中商店 御中",
        "address": "〒530-0047\n大阪府大阪市北区西天満3-5-10",
    },
    "order": {"number": "TS-2609-017", "date": "2026年9月10日"},
    "shipping": {
        "date": "2026年9月17日",
        "time": "午前中",
        "method": "路線便・元払",
        "destination": "博多物流センター（福岡市）",
        "handling": "冷蔵",
        "priority": "通常",
    },
    "items": [
        {"no": 1, "code": "A-1001", "name": "だし 100g", "quantity": 15, "unit": "袋", "package": "ダンボール", "pack_count": 3, "amount": "4,050", "inspection": "✓", "packing": "✓"},
        {"no": 2, "code": "A-1002", "name": "だし 200g", "quantity": 20, "unit": "袋", "package": "ダンボール", "pack_count": 4, "amount": "6,800", "inspection": "✓", "packing": "✓"},
        {"no": 3, "code": "A-1003", "name": "ギフトセット", "quantity": 25, "unit": "袋", "package": "ダンボール", "pack_count": 5, "amount": "10,250", "inspection": "✓", "packing": ""},
        {"no": 4, "code": "B-2001", "name": "つゆ 300ml", "quantity": 30, "unit": "袋", "package": "保冷箱", "pack_count": 2, "amount": "14,400", "inspection": "✓", "packing": "✓"},
        {"no": 5, "code": "B-2002", "name": "つゆ 500ml", "quantity": 35, "unit": "袋", "package": "保冷箱", "pack_count": 3, "amount": "19,250", "inspection": "✓", "packing": ""},
        {"no": 6, "code": "B-2003", "name": "ぽん酢 300ml", "quantity": 40, "unit": "袋", "package": "保冷箱", "pack_count": 4, "amount": "24,800", "inspection": "", "packing": ""},
    ],
    "materials": [
        {"name": "ダンボール（大）", "quantity": 10, "amount": "1,200"},
        {"name": "発泡スチロール箱", "quantity": 15, "amount": "5,250"},
        {"name": "保冷剤", "quantity": 20, "amount": "1,000"},
    ],
    "resources": [{"mark": "✓"}, {"mark": "✓"}, {"mark": "✓"}],
    "special_handling": [{"mark": "✓"}, {"mark": ""}, {"mark": "✓"}, {"mark": "✓"}],
    "remarks": "9/17必着。冷蔵品は10℃以下を維持し、納品書を1部同梱すること。",
    "summary": {"subtotal": "66,550円", "shipping_fee": "2,000円", "total": "68,550円"},
    "staff": {"created_by": "山田", "checked_by": "鈴木", "shipping_confirmed": "中村"},
}


if __name__ == "__main__":
    output_path = Path(__file__).with_name("output.svg")
    output_path.write_text(svg_report_template.render(data), encoding="utf-8")
    print(output_path)
