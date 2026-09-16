"""請求書テンプレートのフィールド定義。"""

from pathlib import Path

from svgreportbuilder import FixedSlots, ImageField, SvgReportTemplate, TextField


STYLES = {
    "font-family": '"Yu Gothic", "Meiryo", sans-serif',
    "font-size": "3.2px",
    "line-height": "1.35",
    "padding": "1px 1.5px",
    "white-space": "pre-wrap",
    "box-sizing": "border-box",
}


svg_report_template = SvgReportTemplate(
    svg=Path(__file__).with_name("template.svg").read_text(encoding="utf-8"),
    fields=[
        ImageField(
            target_id="issuer_logo_box",
            value_path="issuer.logo",
            container_style={"padding": "1px"},
            remove_stroke=True,
            target_fill_path="appearance.issuer_logo_fill",
        ),
        TextField(
            target_id="issuer_name_box",
            value_path="issuer.name",
            remove_stroke=True,
            target_fill_path="appearance.issuer_name_fill",
            container_style=STYLES,
        ),
        TextField(
            target_id="issuer_address_box",
            value_path="issuer.address",
            remove_stroke=True,
            target_fill_path="appearance.issuer_address_fill",
            container_style=STYLES,
        ),
        TextField(target_id="customer_name_box", value_path="customer.name", container_style=STYLES),
        TextField(target_id="customer_address_box", value_path="customer.address", container_style=STYLES),
        TextField(target_id="invoice_number_box", value_path="invoice.number", container_style=STYLES),
        TextField(target_id="issue_date_box", value_path="invoice.issue_date", container_style=STYLES),
        TextField(target_id="due_date_box", value_path="invoice.due_date", container_style=STYLES),
        FixedSlots(
            value_path="items",
            capacity=12,
            min_items=1,
            index="row",
            fields=[
                TextField(value_path="name", target_id="item_{row}_name_box", container_style=STYLES),
                TextField(value_path="quantity", target_id="item_{row}_quantity_box", container_style=STYLES),
                TextField(value_path="unit_price", target_id="item_{row}_unit_price_box", container_style=STYLES | {"text-align": "right"}),
                TextField(value_path="amount", target_id="item_{row}_amount_box", container_style=STYLES | {"text-align": "right"}),
            ],
        ),
        TextField(
            target_id="subtotal_box",
            value_path="subtotal",
            container_style=STYLES | {"text-align": "right", "font-weight": "700"},
        ),
        TextField(
            target_id="tax_box",
            value_path="tax",
            container_style=STYLES | {"text-align": "right"},
        ),
        TextField(
            target_id="total_box",
            value_path="total",
            container_style=STYLES | {"text-align": "right", "font-size": "5px", "font-weight": "700"},
        ),
        TextField(target_id="note_box", value_path="note", container_style=STYLES),
        ImageField(
            target_id="payment_qr_box",
            value_path="payment_qr",
            container_style={"padding": "2px"},
            image_style={"object-fit": "contain"},
            foreign_object_style={"overflow": "visible"},
        ),
    ],
)
