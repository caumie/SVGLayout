"""見積書のサンプルデータ。"""

from pathlib import Path

from svgreportbuilder import Data, ImageSource

from .template_spec import svg_report_template


SEAL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">
<circle cx="24" cy="24" r="21" fill="none" stroke="#c33" stroke-width="2"/>
<text x="24" y="20" text-anchor="middle" fill="#c33" font-size="10">承認</text>
<text x="24" y="32" text-anchor="middle" fill="#c33" font-size="8">SAMPLE</text>
</svg>"""


data: Data = {
    "seller": {
        "name": "サンプルソリューション株式会社",
        "address": "〒100-0001\n東京都千代田区千代田1-1",
        "representative": "営業部　佐藤花子",
        "seal": ImageSource(data=SEAL.encode("utf-8"), mime_type="image/svg+xml"),
    },
    "buyer": {"name": "株式会社未来産業 御中", "person": "購買部　山田太郎様"},
    "appearance": {
        "seller_seal_fill": "none",
        "buyer_fill": "#fff3cd",
        "buyer_stroke": "#b7791f",
    },
    "quote": {
        "number": "Q-2026-0018",
        "date": "2026年9月14日",
        "validity_days": 30,
        "valid_until": "2026年10月14日",
    },
    # tupleもvalue_pathのlist/tuple添字で参照できることを示す。
    "items": (
        {"name": "業務システム初期設定", "quantity": 1, "unit": "式", "price": "300,000円", "amount": "300,000円"},
        {"name": "操作研修（オンライン）", "quantity": 2, "unit": "回", "price": "50,000円", "amount": "100,000円"},
    ),
    "subtotal": "400,000円",
    "discount": "▲20,000円",
    "tax": "38,000円",
    "total": "418,000円",
    "terms": "納期：ご発注から4週間\n作業時間は平日9:00〜18:00を基本とします。\n本見積の有効期限は発行日から30日です。",
}


if __name__ == "__main__":
    # テンプレートへサンプルデータを差し込み、確認用のSVGを書き出す。
    output_svg = svg_report_template.render(data)
    output_path = Path(__file__).with_name("output.svg")
    output_path.write_text(output_svg, encoding="utf-8")
    print(output_path)
