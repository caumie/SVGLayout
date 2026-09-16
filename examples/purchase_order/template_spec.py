"""発注書のフィールド定義。"""

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
        TextField(
            target_id="vendor_name_box",
            value_path="vendor.name",
            container_style=STYLES,
        ),
        TextField(
            target_id="vendor_address_box",
            value_path="vendor.address",
            container_style=STYLES,
        ),
        TextField(
            target_id="requester_name_box",
            value_path="requester.name",
            container_style=STYLES,
        ),
        TextField(
            target_id="requester_department_box",
            value_path="requester.department",
            container_style=STYLES,
        ),
        TextField(
            target_id="requester_phone_box",
            value_path="requester.phone",
            default="（内線未登録）",
            container_style=STYLES,
        ),
        ImageField(
            target_id="requester_signature_box",
            value_path="requester.signature",
            image_style={"object-fit": "contain"},
        ),
        TextField(
            target_id="order_number_box",
            value_path="order.number",
            container_style=STYLES,
        ),
        TextField(
            target_id="order_date_box", value_path="order.date", container_style=STYLES
        ),
        TextField(
            target_id="delivery_date_box",
            value_path="order.delivery_date",
            container_style=STYLES,
        ),
        TextField(
            target_id="destination_box",
            value_path="order.destination",
            container_style=STYLES,
        ),
        TextField(
            target_id="priority_box",
            value_path="order.priority",
            container_style=STYLES | {"text-align": "right"},
        ),
        TextField(
            target_id="expedited_box",
            value_path="order.is_expedited",
            container_style=STYLES,
        ),
        FixedSlots(
            value_path="items",
            capacity=3,
            min_items=1,
            index="row",
            fields=[
                TextField(
                    value_path="name",
                    target_id="item_{row}_name_box",
                    container_style=STYLES,
                ),
                TextField(
                    value_path="quantity",
                    target_id="item_{row}_quantity_box",
                    container_style=STYLES | {"text-align": "right"},
                ),
                TextField(
                    value_path="unit",
                    target_id="item_{row}_unit_box",
                    container_style=STYLES,
                ),
                TextField(
                    value_path="price",
                    target_id="item_{row}_price_box",
                    container_style=STYLES | {"text-align": "right"},
                ),
                TextField(
                    value_path="amount",
                    target_id="item_{row}_amount_box",
                    container_style=STYLES | {"text-align": "right"},
                ),
            ],
        ),
        TextField(
            target_id="subtotal_box",
            value_path="subtotal",
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
        FixedSlots(
            value_path="approvals",
            capacity=2,
            min_items=1,
            index="approval",
            fields=[
                TextField(
                    value_path="role",
                    target_id="approval_{approval}_role_box",
                    container_style=STYLES,
                ),
                TextField(
                    value_path="name",
                    target_id="approval_{approval}_name_box",
                    container_style=STYLES,
                ),
            ],
        ),
        ImageField(
            target_id="approval_stamp_box",
            value_path="approval_stamp",
            container_style={"padding": "1px"},
            image_style={"object-fit": "contain"},
        ),
        TextField(
            target_id="remarks_box", value_path="remarks", container_style=STYLES
        ),
    ],
)
