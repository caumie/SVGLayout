"""出荷指示兼梱包明細書のフィールド定義。"""

from pathlib import Path

from svgreportbuilder import FixedSlots, SvgReportTemplate, TextField


TEXT = {
    "font-family": '"Yu Gothic", "Meiryo", sans-serif',
    "font-size": "2.55px",
    "line-height": "1.15",
    "padding": "0.7px",
    "white-space": "pre-wrap",
    "box-sizing": "border-box",
    "display": "flex",
    "flex-direction": "column",
    "justify-content": "center",
    "overflow": "hidden",
}
CENTER = TEXT | {"text-align": "center"}
RIGHT = TEXT | {"text-align": "right"}


def item_fields(row: int) -> list[TextField]:
    return [
        TextField(value_path="no", target_id=f"item_{{row}}_no_box", container_style=CENTER),
        TextField(value_path="code", target_id=f"item_{{row}}_code_box", container_style=TEXT),
        TextField(value_path="name", target_id=f"item_{{row}}_name_box", container_style=TEXT),
        TextField(value_path="quantity", target_id=f"item_{{row}}_quantity_box", container_style=RIGHT),
        TextField(value_path="unit", target_id=f"item_{{row}}_unit_box", container_style=CENTER),
        TextField(value_path="package", target_id=f"item_{{row}}_package_box", container_style=TEXT),
        TextField(value_path="pack_count", target_id=f"item_{{row}}_pack_count_box", container_style=RIGHT),
        TextField(value_path="amount", target_id=f"item_{{row}}_amount_box", default="", container_style=RIGHT),
        TextField(value_path="inspection", target_id=f"item_{{row}}_inspection_box", container_style=CENTER),
        TextField(value_path="packing", target_id=f"item_{{row}}_packing_box", container_style=CENTER),
    ]


svg_report_template = SvgReportTemplate(
    svg=Path(__file__).with_name("template.svg").read_text(encoding="utf-8"),
    fields=[
        TextField(target_id="document_number_box", value_path="document.number", container_style=RIGHT),
        TextField(target_id="document_date_box", value_path="document.date", container_style=RIGHT),
        TextField(target_id="customer_code_box", value_path="customer.code", container_style=CENTER),
        TextField(target_id="customer_name_box", value_path="customer.name", container_style=TEXT),
        TextField(target_id="customer_address_box", value_path="customer.address", container_style=TEXT),
        TextField(target_id="order_number_box", value_path="order.number", container_style=TEXT),
        TextField(target_id="order_date_box", value_path="order.date", container_style=CENTER),
        TextField(target_id="shipping_date_box", value_path="shipping.date", container_style=CENTER),
        TextField(target_id="delivery_time_box", value_path="shipping.time", container_style=CENTER),
        TextField(target_id="shipping_method_box", value_path="shipping.method", container_style=TEXT),
        TextField(target_id="destination_box", value_path="shipping.destination", container_style=TEXT),
        TextField(target_id="handling_box", value_path="shipping.handling", container_style=CENTER),
        TextField(target_id="priority_box", value_path="shipping.priority", container_style=CENTER),
        FixedSlots(value_path="items", capacity=9, min_items=1, index="row", fields=item_fields(0)),
        FixedSlots(
            value_path="materials",
            capacity=4,
            min_items=0,
            index="material",
            fields=[
                TextField(value_path="name", target_id="material_{material}_name_box", container_style=TEXT),
                TextField(value_path="quantity", target_id="material_{material}_quantity_box", container_style=RIGHT),
                TextField(value_path="amount", target_id="material_{material}_amount_box", default="", container_style=RIGHT),
            ],
        ),
        FixedSlots(
            value_path="resources",
            capacity=4,
            min_items=0,
            index="resource",
            fields=[TextField(value_path="mark", target_id="resource_{resource}_box", default="", container_style=CENTER)],
        ),
        FixedSlots(
            value_path="special_handling",
            capacity=4,
            min_items=0,
            index="special",
            fields=[TextField(value_path="mark", target_id="special_{special}_box", default="", container_style=CENTER)],
        ),
        TextField(target_id="remarks_box", value_path="remarks", default="", container_style=TEXT),
        TextField(target_id="subtotal_box", value_path="summary.subtotal", container_style=RIGHT),
        TextField(target_id="shipping_fee_box", value_path="summary.shipping_fee", container_style=RIGHT),
        TextField(target_id="total_box", value_path="summary.total", container_style=RIGHT),
        TextField(target_id="created_by_box", value_path="staff.created_by", container_style=CENTER),
        TextField(target_id="checked_by_box", value_path="staff.checked_by", container_style=CENTER),
        TextField(target_id="shipping_confirmed_box", value_path="staff.shipping_confirmed", container_style=CENTER),
    ],
)
