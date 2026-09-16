"""納品書1ページ分のフィールド定義。"""

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

TITLE = {
    "font-size": "8px",
    "font-weight": "700",
    "color": "#fff",
    "display": "flex",
    "align-items": "center",
    "justify-content": "flex-start",
    "text-align": "left",
    "padding": "0",
    "white-space": "nowrap",
}


svg_report_template = SvgReportTemplate(
    svg=Path(__file__).with_name("template.svg").read_text(encoding="utf-8"),
    fields=[
        TextField(
            target_id="page_title_box",
            value_path="page.title",
            container_style=STYLES | TITLE,
        ),
        TextField(target_id="delivery_number_box", value_path="delivery.number", container_style=STYLES),
        TextField(target_id="delivery_date_box", value_path="delivery.date", container_style=STYLES),
        TextField(target_id="order_number_box", value_path="delivery.order_number", container_style=STYLES),
        TextField(target_id="shipper_name_box", value_path="shipper.name", container_style=STYLES),
        TextField(target_id="shipper_address_box", value_path="shipper.address", container_style=STYLES),
        TextField(target_id="destination_name_box", value_path="destination.name", container_style=STYLES),
        TextField(target_id="destination_address_box", value_path="destination.address", container_style=STYLES),
        TextField(
            target_id="page_number_box",
            value_path="page.number",
            container_style=STYLES | {"text-align": "right"},
        ),
        TextField(
            target_id="page_total_box",
            value_path="page.total",
            container_style=STYLES | {"text-align": "right"},
        ),
        FixedSlots(
            value_path="items",
            capacity=3,
            min_items=1,
            index="row",
            fields=[
                lambda row: TextField(
                    value_path="name",
                    target_id="item_{row}_name_box",
                    container_style=STYLES,
                    foreign_object_style={"overflow": "visible"} if row == 0 else {},
                ),
                TextField(value_path="code", target_id="item_{row}_code_box", container_style=STYLES),
                TextField(value_path="quantity", target_id="item_{row}_quantity_box", container_style=STYLES | {"text-align": "right"}),
                TextField(value_path="unit", target_id="item_{row}_unit_box", container_style=STYLES),
            ],
        ),
        TextField(target_id="note_box", value_path="note", container_style=STYLES),
        TextField(target_id="receiver_name_box", value_path="receiver.name", default="", container_style=STYLES),
        ImageField(target_id="barcode_box", value_path="barcode", container_style={"padding": "1px"}, image_style={"object-fit": "contain"}),
        ImageField(target_id="receiver_stamp_box", value_path="receiver.stamp", default=None, container_style={"padding": "1px"}, image_style={"object-fit": "contain"}),
    ],
)
