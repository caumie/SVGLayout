"""見積書のフィールド定義。"""

from pathlib import Path

from svgreportbuilder import FixedSlots, ImageField, SvgReportTemplate, TextField

STYLES = {
    "font-family": '"Yu Gothic", "Meiryo", sans-serif',
    "font-size": "3.2px",
    "line-height": "1.35",
    "padding": "1px",
    "white-space": "pre-wrap",
    "box-sizing": "border-box",
}


svg_report_template = SvgReportTemplate(
    svg=Path(__file__).with_name("template.svg").read_text(encoding="utf-8"),
    fields=[
        TextField(target_id="seller_name_box", value_path="seller.name", container_style=STYLES),
        TextField(target_id="seller_address_box", value_path="seller.address", container_style=STYLES),
        TextField(
            target_id="seller_representative_box", value_path="seller.representative", container_style=STYLES
        ),
        ImageField(
            target_id="seller_seal_box",
            value_path="seller.seal",
            container_style={"padding": "1px"},
            image_style={"object-fit": "contain"},
            remove_stroke=True,
            target_fill_path="appearance.seller_seal_fill",
        ),
        TextField(
            target_id="buyer_name_box",
            value_path="buyer.name",
            container_style=STYLES | {"font-weight": "700"},
            target_fill_path="appearance.buyer_fill",
            target_stroke_path="appearance.buyer_stroke",
        ),
        TextField(target_id="buyer_person_box", value_path="buyer.person", container_style=STYLES),
        TextField(target_id="quote_number_box", value_path="quote.number", container_style=STYLES),
        TextField(target_id="quote_date_box", value_path="quote.date", container_style=STYLES),
        TextField(
            target_id="quote_validity_box",
            value_path="quote.validity_days",
            container_style=STYLES | {"text-align": "right"},
        ),
        TextField(target_id="quote_valid_until_box", value_path="quote.valid_until", container_style=STYLES),
        FixedSlots(
            value_path="items",
            capacity=3,
            min_items=1,
            index="row",
            fields=[
                TextField(value_path="name", target_id="item_{row}_name_box", container_style=STYLES),
                TextField(value_path="quantity", target_id="item_{row}_quantity_box", container_style=STYLES | {"text-align": "right"}),
                TextField(value_path="unit", target_id="item_{row}_unit_box", container_style=STYLES),
                TextField(value_path="price", target_id="item_{row}_price_box", container_style=STYLES | {"text-align": "right"}),
                TextField(value_path="amount", target_id="item_{row}_amount_box", container_style=STYLES | {"text-align": "right"}),
            ],
        ),
        TextField(
            target_id="subtotal_box",
            value_path="subtotal",
            container_style=STYLES | {"text-align": "right"},
        ),
        TextField(
            target_id="discount_box",
            value_path="discount",
            default="",
            container_style=STYLES | {"text-align": "right"},
        ),
        TextField(
            target_id="tax_box",
            value_path="tax",
            container_style=STYLES | {"text-align": "right"},
        ),
        TextField(
            target_id="total_box",
            value_path="total",
            container_style=STYLES
            | {"text-align": "right", "font-size": "5px", "font-weight": "700"},
        ),
        TextField(target_id="terms_box", value_path="terms", container_style=STYLES),
    ],
)
