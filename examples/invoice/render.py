"""請求書のサンプルデータ。表示用の整形は呼び出し側で済ませる。"""

from pathlib import Path

from svgreportbuilder import Data, ImageSource

from .template_spec import svg_report_template


COMPANY_LOGO = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 36">
<rect width="120" height="36" rx="5" fill="#1d4e89"/>
<circle cx="18" cy="18" r="10" fill="#ffffff"/>
<path d="M12 18h12M18 12v12" stroke="#1d4e89" stroke-width="3"/>
<text x="34" y="23" fill="#ffffff" font-size="13" font-family="sans-serif">SAMPLE INC.</text>
</svg>"""

PAYMENT_QR = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 29 29">
<rect width="29" height="29" fill="white"/>
<g fill="black">
  <path d="M1 1h8v8H1zm2 2v4h4V3zM20 1h8v8h-8zm2 2v4h4V3zM1 20h8v8H1zm2 2v4h4v-4z"/>
  <path d="M11 2h2v2h-2zm3 0h2v4h-2zm3 0h2v2h-2zM11 7h2v3h-2zm3-2h2v2h-2zm3 3h2v2h-2zM11 11h3v3h-3zm5 0h2v5h-2zm3 1h3v2h-3zm5 0h3v5h-3zM11 16h2v3h-2zm3 1h2v2h-2zm4 1h3v3h-3zm5 3h2v2h-2zM11 22h2v5h-2zm3 0h2v2h-2zm3 3h3v2h-3zm4-3h2v4h-2z"/>
</g></svg>"""


data: Data = {
    "issuer": {
        "name": "株式会社サンプル商事",
        "address": "〒100-0001\n東京都千代田区千代田1-1\n経理部 ご担当者様",
        "logo": ImageSource(data=COMPANY_LOGO.encode("utf-8"), mime_type="image/svg+xml"),
    },
    "appearance": {
        "issuer_logo_fill": "none",
        "issuer_name_fill": "none",
        "issuer_address_fill": "none",
    },
    "customer": {
        "name": "株式会社未来産業 御中",
        "address": "〒150-0001\n東京都渋谷区神宮前2-2-2\n購買部 山田太郎様",
    },
    "invoice": {
        "number": "INV-2026-00042",
        "issue_date": "2026年9月13日",
        "due_date": "2026年10月31日",
    },
    "items": [
        {"name": "システム利用料（2026年9月分）", "quantity": "1式", "unit_price": "110,000円", "amount": "110,000円"},
        {"name": "導入支援作業", "quantity": "2時間", "unit_price": "11,000円", "amount": "22,000円"},
        {"name": "追加ユーザーライセンス（◆管理者）", "quantity": "3名", "unit_price": "8,000円", "amount": "24,000円"},
        {"name": "データ移行オプション", "quantity": "1式", "unit_price": "35,000円", "amount": "35,000円"},
        {
            "name": "帳票カスタマイズ：請求明細一覧表（品目・数量・単価・金額・税率・備考）",
            "quantity": "1式",
            "unit_price": "48,000円",
            "amount": "48,000円",
        },
        {"name": "帳票カスタマイズ：入出庫一覧（CSV）", "quantity": "1式", "unit_price": "32,000円", "amount": "32,000円"},
        {"name": "運用サポート（平日）", "quantity": "4時間", "unit_price": "9,000円", "amount": "36,000円"},
        {"name": "運用サポート（休日）", "quantity": "1時間", "unit_price": "14,000円", "amount": "14,000円"},
        {"name": "API連携設定（受注→出荷）", "quantity": "1式", "unit_price": "60,000円", "amount": "60,000円"},
        {"name": "バーコード出力対応（CODE128）", "quantity": "1式", "unit_price": "18,000円", "amount": "18,000円"},
        {"name": "電子帳簿保存対応 ※要社内確認", "quantity": "1式", "unit_price": "25,000円", "amount": "25,000円"},
        {"name": "月次データバックアップ保管", "quantity": "1ヶ月", "unit_price": "5,000円", "amount": "5,000円"},
    ],
    "subtotal": "429,000円",
    "tax": "42,900円",
    "total": "471,900円",
    "note": "お支払期限：2026年10月31日\n振込手数料はご負担ください。\nご不明点は経理部までお問い合わせください。",
    "payment_qr": ImageSource(data=PAYMENT_QR.encode("utf-8"), mime_type="image/svg+xml"),
}


if __name__ == "__main__":
    # テンプレートへサンプルデータを差し込み、確認用のSVGを書き出す。
    output_svg = svg_report_template.render(data)
    output_path = Path(__file__).with_name("output.svg")
    output_path.write_text(output_svg, encoding="utf-8")
    print(output_path)
