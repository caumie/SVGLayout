"""3ページに分かれる納品書のサンプルデータ。"""

from pathlib import Path

from svgreportbuilder import Data, ImageSource

from .template_spec import svg_report_template

barcode_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 48">
<rect width="160" height="48" fill="white"/>
<g fill="black">
  <rect x="8" y="4" width="2" height="32"/><rect x="14" y="4" width="4" height="32"/>
  <rect x="22" y="4" width="2" height="32"/><rect x="28" y="4" width="6" height="32"/>
  <rect x="38" y="4" width="2" height="32"/><rect x="44" y="4" width="4" height="32"/>
  <rect x="54" y="4" width="6" height="32"/><rect x="64" y="4" width="2" height="32"/>
  <rect x="70" y="4" width="4" height="32"/><rect x="80" y="4" width="2" height="32"/>
  <rect x="86" y="4" width="6" height="32"/><rect x="96" y="4" width="2" height="32"/>
  <rect x="102" y="4" width="4" height="32"/><rect x="112" y="4" width="6" height="32"/>
  <rect x="124" y="4" width="2" height="32"/><rect x="130" y="4" width="6" height="32"/>
</g><text x="80" y="44" text-anchor="middle" font-size="7">DN-2026-0042</text></svg>"""

received_stamp_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42 42">
<circle cx="21" cy="21" r="18" fill="none" stroke="#2266aa" stroke-width="2"/>
<text x="21" y="25" text-anchor="middle" fill="#2266aa" font-size="9">検収済</text>
</svg>"""

common_data: Data = {
    "shipper": {"name": "サンプル物流株式会社", "address": "東京都江東区辰巳3-3-3"},
    "destination": {"name": "株式会社未来産業", "address": "東京都渋谷区神宮前2-2-2\n物流センター気付"},
    "delivery": {"number": "DN-2026-0042", "date": "2026年9月14日", "order_number": "PO-2026-0088"},
    "barcode": ImageSource(data=barcode_svg.encode("utf-8"), mime_type="image/svg+xml"),
}


page_data: tuple[Data, ...] = (
    dict(common_data) | {
        "page": {"title": "納品書", "number": 1, "total": 3},
        "items": [
            {"name": "業務用ノートPC 14インチ", "code": "PC-14-STD", "quantity": 10, "unit": "台"},
            {"name": "USB-Cドッキングステーション", "code": "DOCK-01", "quantity": 10, "unit": "個"},
            {"name": "長期保証サービス（標準）", "code": "WARRANTY-STANDARD", "quantity": 10, "unit": "件"},
        ],
        "receiver": {"name": "", "stamp": None},
        "note": "1ページ目は機器本体と付属品です。\n数量をご確認ください。",
    },
    dict(common_data) | {
        "page": {"title": "物品受領書", "number": 2, "total": 3},
        "items": [
            {"name": "初期セットアップ作業（利用者10名分）", "code": "SETUP-10", "quantity": 1, "unit": "式"},
        ],
        "receiver": {"name": "株式会社未来産業　山田太郎", "stamp": ImageSource(data=received_stamp_svg.encode("utf-8"), mime_type="image/svg+xml")},
        "note": "2ページ目の内容を含めて納品完了とします。\n受領後の不足・破損は3営業日以内にご連絡ください。",
    },
    dict(common_data) | {
        "page": {"title": "仕入伝票", "number": 3, "total": 3},
        "items": [
            {"name": "仕入伝票一式（社内控え）", "code": "PURCHASE-SLIP", "quantity": 1, "unit": "部"},
        ],
        "receiver": {"name": "", "stamp": None},
        "note": "仕入処理用の社内控えです。\n※ 納品書・物品受領書と番号を照合してください。",
    },
)

data: Data = {"pages": list(page_data)}


if __name__ == "__main__":
    # 複数ページ分のデータを1ページずつ同じテンプレートへ差し込む。
    pages = data["pages"]
    if not isinstance(pages, list):
        raise TypeError("delivery note data.pages must be a list")

    for page_number, page in enumerate(pages, start=1):
        if not isinstance(page, dict):
            raise TypeError("delivery note data.pages must contain mappings")

        # ライブラリは1回のrenderで1枚のSVGを返すため、ページ単位で保存する。
        output_svg = svg_report_template.render(page)
        output_path = Path(__file__).with_name(f"output-{page_number}.svg")
        output_path.write_text(output_svg, encoding="utf-8")
        print(output_path)
