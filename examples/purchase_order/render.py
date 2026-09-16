"""発注書のサンプルデータ。"""

from pathlib import Path

from svgreportbuilder import Data, ImageSource

from .template_spec import svg_report_template


STAMP = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50">
<circle cx="25" cy="25" r="21" fill="none" stroke="#b33" stroke-width="2"/>
<text x="25" y="22" text-anchor="middle" fill="#b33" font-size="10">承認</text><text x="25" y="33" text-anchor="middle" fill="#b33" font-size="8">経理</text>
</svg>"""

SIGNATURE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 40">
<path d="M5 28c18-25 16 10 28-7 8-11 8 11 18-3 7-10 10 8 19-5 6-8 12 7 22-4" fill="none" stroke="#173e73" stroke-width="2"/>
</svg>"""


data: Data = {
    "vendor": {"name": "株式会社パーツサプライ 御中", "address": "〒530-0001\n大阪府大阪市北区梅田4-4-4"},
    "requester": {"name": "鈴木一郎", "department": "開発部", "signature": ImageSource(data=SIGNATURE.encode("utf-8"), mime_type="image/svg+xml")},
    "order": {
        "number": "PO-2026-0088",
        "date": "2026年9月14日",
        "delivery_date": "2026年10月5日",
        "destination": "本社開発フロア（東京都千代田区）",
        "priority": 2,
        "is_expedited": True,
    },
    "items": [
        {"name": "交換用センサー A型", "quantity": "20", "unit": "個", "price": "8,500円", "amount": "170,000円"},
        {"name": "保守用ケーブル（5m）", "quantity": "20", "unit": "本", "price": "1,200円", "amount": "24,000円"},
    ],
    "subtotal": "194,000円",
    "tax": "19,400円",
    "total": "213,400円",
    "approvals": (
        {"role": "申請者", "name": "鈴木一郎"},
        {"role": "承認者", "name": "高橋次郎"},
    ),
    "approval_stamp": ImageSource(data=STAMP.encode("utf-8"), mime_type="image/svg+xml"),
    "remarks": "納品時に注文番号を明記してください。\n分納する場合は事前にご連絡ください。\n優先度は社内基準の2（通常）です。",
}


if __name__ == "__main__":
    # テンプレートへサンプルデータを差し込み、確認用のSVGを書き出す。
    output_svg = svg_report_template.render(data)
    output_path = Path(__file__).with_name("output.svg")
    output_path.write_text(output_svg, encoding="utf-8")
    print(output_path)
