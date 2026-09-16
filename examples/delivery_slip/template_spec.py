"""納品書の固定枠とデータ項目の対応。"""

from pathlib import Path

from svgreportbuilder import FixedSlots, ImageField, SvgReportTemplate, TextField


TEXT = {
    "font-family": '"Yu Gothic", "Meiryo", sans-serif',
    "font-size": "3px",
    "line-height": "1.25",
    "padding": "1px",
    "white-space": "pre-wrap",
    "box-sizing": "border-box",
    "display": "flex",
    "flex-direction": "column",
    "justify-content": "center",
    "overflow": "hidden",
}
RIGHT = TEXT | {"text-align": "right"}
CENTER = TEXT | {"text-align": "center"}


svg_report_template = SvgReportTemplate(
    svg=Path(__file__).with_name("template.svg").read_text(encoding="utf-8"),
    fields=[
        TextField(target_id="delivery_number_box", value_path="document.number", container_style=RIGHT),
        TextField(target_id="delivery_date_box", value_path="document.date", container_style=RIGHT),
        TextField(target_id="destination_name_box", value_path="destination.name", container_style=TEXT),
        TextField(target_id="destination_address_box", value_path="destination.address", container_style=TEXT),
        TextField(target_id="shipper_name_box", value_path="shipper.name", container_style=TEXT),
        TextField(target_id="shipper_address_box", value_path="shipper.address", container_style=TEXT),
        TextField(target_id="order_number_box", value_path="delivery.order_number", container_style=TEXT),
        TextField(target_id="delivery_place_box", value_path="delivery.place", container_style=TEXT),
        TextField(target_id="delivery_method_box", value_path="delivery.method", container_style=TEXT),
        FixedSlots(
            value_path="items",
            capacity=8,
            min_items=1,
            index="row",
            fields=[
                TextField(value_path="no", target_id="item_{row}_no_box", container_style=CENTER),
                TextField(value_path="code", target_id="item_{row}_code_box", container_style=TEXT),
                TextField(
                    value_path="name",
                    target_id="item_{row}_name_box",
                    container_style=TEXT,
                    foreign_object_style={"overflow": "hidden"},
                ),
                TextField(value_path="quantity", target_id="item_{row}_quantity_box", container_style=RIGHT),
                TextField(value_path="unit", target_id="item_{row}_unit_box", container_style=CENTER),
                TextField(value_path="amount", target_id="item_{row}_amount_box", container_style=RIGHT),
                TextField(value_path="note", target_id="item_{row}_note_box", default="", container_style=TEXT),
            ],
        ),
        TextField(target_id="note_box", value_path="note", container_style=TEXT),
        TextField(target_id="subtotal_box", value_path="summary.subtotal", container_style=RIGHT),
        TextField(target_id="tax_box", value_path="summary.tax", container_style=RIGHT),
        TextField(target_id="total_box", value_path="summary.total", container_style=RIGHT),
        TextField(target_id="staff_box", value_path="staff.name", container_style=TEXT),
        TextField(target_id="receiver_box", value_path="receiver.name", default="", container_style=TEXT),
        ImageField(
            target_id="receiver_stamp_box",
            value_path="receiver.stamp",
            default=None,
            container_style={"padding": "1px"},
            image_style={"object-fit": "contain"},
        ),
        ImageField(
            target_id="barcode_box",
            value_path="barcode",
            container_style={"padding": "1px"},
            image_style={"object-fit": "contain"},
        ),
        TextField(target_id="page_box", value_path="document.page", container_style=CENTER),
        TextField(target_id="issuer_confirmation_box", value_path="staff.confirmation", container_style=TEXT),
    ],
)
