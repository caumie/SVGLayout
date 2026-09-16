"""変形小型伝票のフィールド定義。"""

from pathlib import Path

from svgreportbuilder import FixedSlots, SvgReportTemplate, TextField


TEXT = {
    "font-family": '"Yu Gothic", "Meiryo", sans-serif',
    "font-size": "2.6px",
    "line-height": "1.1",
    "padding": "0.4px",
    "white-space": "nowrap",
    "box-sizing": "border-box",
    "display": "flex",
    "flex-direction": "column",
    "justify-content": "center",
    "overflow": "hidden",
}
CENTER = TEXT | {"text-align": "center"}


svg_report_template = SvgReportTemplate(
    svg=Path(__file__).with_name("template.svg").read_text(encoding="utf-8"),
    fields=[
        TextField(target_id="ticket_number_box", value_path="ticket.number", container_style=TEXT),
        TextField(target_id="date_box", value_path="ticket.date", container_style=TEXT),
        TextField(target_id="customer_box", value_path="customer.name", container_style=TEXT),
        TextField(target_id="item_box", value_path="order.item", container_style=TEXT),
        TextField(target_id="quantity_box", value_path="order.quantity", container_style=CENTER),
        TextField(target_id="amount_box", value_path="order.amount", container_style=CENTER),
        TextField(target_id="due_date_box", value_path="order.due_date", container_style=CENTER),
        TextField(target_id="received_by_box", value_path="staff.received_by", container_style=CENTER),
        FixedSlots(
            value_path="services",
            capacity=4,
            min_items=1,
            index="row",
            fields=[TextField(value_path="mark", target_id="service_{row}_box", default="", container_style=CENTER)],
        ),
        TextField(target_id="due_date_mini_box", value_path="order.due_date", container_style=CENTER),
        FixedSlots(
            value_path="payments",
            capacity=3,
            min_items=1,
            index="row",
            fields=[TextField(value_path="mark", target_id="payment_{row}_box", default="", container_style=CENTER)],
        ),
        TextField(target_id="stub_ticket_number_box", value_path="ticket.number", container_style=CENTER),
        TextField(target_id="stub_customer_box", value_path="customer.name", container_style=CENTER),
        TextField(target_id="stub_item_box", value_path="order.short_item", container_style=CENTER),
        TextField(target_id="stub_due_date_box", value_path="order.due_date_short", container_style=CENTER),
    ],
)
