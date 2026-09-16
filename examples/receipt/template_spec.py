"""領収書のフィールド定義。"""

from pathlib import Path

from svgreportbuilder import ImageField, SvgReportTemplate, TextField


STYLES = {
    "font-family": '"Yu Gothic", "Meiryo", sans-serif',
    "font-size": "3.4px",
    "line-height": "1.3",
    "padding": "1px",
    "white-space": "pre-wrap",
    "box-sizing": "border-box",
}


svg_report_template = SvgReportTemplate(
    svg=Path(__file__).with_name("template.svg").read_text(encoding="utf-8"),
    fields=[
        ImageField(
            target_id="store_logo_box",
            value_path="store.logo",
            container_style={"padding": "1px"},
            image_style={"object-fit": "contain"},
            remove_stroke=True,
            target_fill_path="appearance.store_logo_fill",
        ),
        TextField(target_id="store_name_box", value_path="store.name", container_style=STYLES),
        TextField(target_id="store_address_box", value_path="store.address", container_style=STYLES),
        TextField(
            target_id="receipt_number_box",
            value_path="receipt.number",
            container_style=STYLES | {"text-align": "right"},
        ),
        TextField(
            target_id="receipt_date_box",
            value_path="receipt.date",
            container_style=STYLES | {"text-align": "right"},
        ),
        TextField(target_id="customer_name_box", value_path="customer.name", container_style=STYLES),
        TextField(target_id="description_box", value_path="description", container_style=STYLES),
        TextField(
            target_id="amount_box",
            value_path="amount",
            container_style=STYLES
            | {"text-align": "right", "font-size": "8px", "font-weight": "700"},
        ),
        TextField(
            target_id="tax_rate_box",
            value_path="tax_rate",
            container_style=STYLES | {"text-align": "right"},
        ),
        TextField(
            target_id="tax_included_box",
            value_path="tax_included",
            container_style=STYLES | {"text-align": "center"},
        ),
        TextField(target_id="payment_method_box", value_path="receipt.payment_method", container_style=STYLES),
        TextField(target_id="customer_memo_box", value_path="customer.memo", container_style=STYLES),
        ImageField(target_id="optional_seal_box", value_path="store.seal", default=None, image_style={"object-fit": "contain"}),
        ImageField(target_id="electronic_mark_box", value_path="electronic_mark", image_style={"object-fit": "contain"}),
        ImageField(target_id="payment_qr_box", value_path="payment_qr", container_style={"padding": "1px"}, image_style={"object-fit": "contain"}),
    ],
)
