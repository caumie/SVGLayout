"""納品書のサンプルデータをテンプレートへ差し込む。"""

from pathlib import Path

from svgreportbuilder import Data, ImageSource

from .template_spec import svg_report_template


BARCODE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 42">
<rect width="180" height="42" fill="white"/>
<g fill="#111">
  <rect x="8" y="4" width="2" height="27"/><rect x="14" y="4" width="5" height="27"/>
  <rect x="24" y="4" width="2" height="27"/><rect x="30" y="4" width="7" height="27"/>
  <rect x="42" y="4" width="3" height="27"/><rect x="50" y="4" width="5" height="27"/>
  <rect x="61" y="4" width="2" height="27"/><rect x="67" y="4" width="7" height="27"/>
  <rect x="80" y="4" width="3" height="27"/><rect x="88" y="4" width="5" height="27"/>
  <rect x="99" y="4" width="2" height="27"/><rect x="105" y="4" width="7" height="27"/>
  <rect x="118" y="4" width="3" height="27"/><rect x="126" y="4" width="5" height="27"/>
  <rect x="137" y="4" width="2" height="27"/><rect x="143" y="4" width="7" height="27"/>
</g><text x="90" y="38" text-anchor="middle" font-size="7">DS-2026-0916-018</text></svg>"""

STAMP = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 56 32">
<rect width="56" height="32" fill="none"/><circle cx="28" cy="16" r="12" fill="none" stroke="#2367a8" stroke-width="1.5"/>
<text x="28" y="19" text-anchor="middle" fill="#2367a8" font-size="7">検収済</text></svg>"""


data: Data = {
    "document": {"number": "DS-2026-0916-018", "date": "2026年9月16日", "page": "1 / 1"},
    "destination": {
        "name": "株式会社未来産業 御中",
        "address": "〒150-0001\n東京都渋谷区神宮前2-2-2\n購買部 山田太郎様",
    },
    "shipper": {
        "name": "株式会社サンプル商事",
        "address": "〒100-0001\n東京都千代田区千代田1-1\n物流管理課",
    },
    "delivery": {"order_number": "PO-2026-0088", "place": "貴社指定倉庫", "method": "路線便"},
    "items": [
        {"no": 1, "code": "PC-14-STD", "name": "業務用ノートPC 14インチ", "quantity": 10, "unit": "台", "amount": "", "note": ""},
        {"no": 2, "code": "DOCK-01", "name": "USB-Cドッキングステーション", "quantity": 10, "unit": "個", "amount": "", "note": ""},
        {"no": 3, "code": "BAG-15", "name": "PCキャリングバッグ 15インチ対応", "quantity": 10, "unit": "個", "amount": "", "note": "付属品"},
        {"no": 4, "code": "SETUP-10", "name": "初期セットアップ作業（利用者10名分）", "quantity": 1, "unit": "式", "amount": "", "note": ""},
        {"no": 5, "code": "WARRANTY-3Y", "name": "延長保証サービス 3年", "quantity": 10, "unit": "件", "amount": "", "note": ""},
    ],
    "summary": {"subtotal": "納品確認用", "tax": "金額欄なし", "total": "無償納品"},
    "note": "納品内容をご確認ください。数量の不足・破損がある場合は、受領後3営業日以内にご連絡ください。",
    "staff": {"name": "鈴木", "confirmation": "出荷記録と注文番号を照合済み"},
    "receiver": {
        "name": "山田太郎",
        "stamp": ImageSource(data=STAMP.encode("utf-8"), mime_type="image/svg+xml"),
    },
    "barcode": ImageSource(data=BARCODE.encode("utf-8"), mime_type="image/svg+xml"),
}


if __name__ == "__main__":
    output_path = Path(__file__).with_name("output.svg")
    output_path.write_text(svg_report_template.render(data), encoding="utf-8")
    print(output_path)
