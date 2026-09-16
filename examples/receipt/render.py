"""小型の領収書サンプルデータ。"""

import base64
from pathlib import Path

from svgreportbuilder import Data, ImageSource

from .template_spec import svg_report_template


LOGO = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 24">
<rect width="100" height="24" rx="4" fill="#3f526b"/><text x="50" y="16" text-anchor="middle" fill="white" font-size="10">SAMPLE STORE</text>
</svg>"""

QR = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 21 21">
<rect width="21" height="21" fill="white"/><g fill="black"><path d="M1 1h6v6H1zm2 2v2h2V3zM14 1h6v6h-6zm2 2v2h2V3zM1 14h6v6H1zm2 2v2h2v-2z"/><path d="M9 2h2v3H9zm3 3h2v3h-2zM9 9h3v3H9zm5 1h2v4h-2zm-5 5h2v5H9zm3 2h3v2h-3z"/></g>
</svg>"""

E_RECEIPT_MARK = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
)


data: Data = {
    "store": {
        "name": "株式会社サンプル商会",
        "address": "東京都中央区銀座5-5-5",
        "logo": ImageSource(data=LOGO.encode("utf-8"), mime_type="image/svg+xml"),
    },
    "appearance": {"store_logo_fill": "none"},
    "receipt": {"number": "R-2026-0914-0031", "date": "2026年9月14日 15:42", "payment_method": "☑ カード"},
    "customer": {"name": "山田太郎 様", "memo": None},
    "description": "業務用品一式",
    "amount": 132000,
    "tax_rate": 10.0,
    "tax_included": "（消費税10%を含む）",
    "electronic_mark": ImageSource(data=E_RECEIPT_MARK, mime_type="image/png"),
    "payment_qr": ImageSource(data=QR.encode("utf-8"), mime_type="image/svg+xml"),
}


if __name__ == "__main__":
    # テンプレートへサンプルデータを差し込み、確認用のSVGを書き出す。
    output_svg = svg_report_template.render(data)
    output_path = Path(__file__).with_name("output.svg")
    output_path.write_text(output_svg, encoding="utf-8")
    print(output_path)
