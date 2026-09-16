"""印刷工程進行票の固定工程と数量欄の定義。"""

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


svg_report_template = SvgReportTemplate(
    svg=Path(__file__).with_name("template.svg").read_text(encoding="utf-8"),
    fields=[
        TextField(target_id="job_number_box", value_path="job.number", container_style=CENTER),
        TextField(target_id="created_date_box", value_path="job.created_date", container_style=CENTER),
        TextField(target_id="customer_box", value_path="job.customer", container_style=TEXT),
        TextField(target_id="product_box", value_path="job.product", container_style=TEXT),
        TextField(target_id="due_date_box", value_path="job.due_date", container_style=CENTER),
        TextField(target_id="specification_box", value_path="job.specification", container_style=TEXT),
        TextField(target_id="quantity_box", value_path="job.quantity", container_style=CENTER),
        TextField(target_id="operator_box", value_path="job.operator", container_style=CENTER),
        TextField(target_id="job_note_box", value_path="job.note", default="", container_style=TEXT),
        FixedSlots(
            value_path="processes",
            capacity=7,
            min_items=1,
            index="row",
            fields=[
                TextField(value_path="name", target_id="process_{row}_name_box", container_style=TEXT),
                TextField(
                    value_path="status",
                    target_id="process_{row}_status_box",
                    container_style=CENTER,
                    target_fill_path="status_fill",
                ),
                TextField(value_path="plan", target_id="process_{row}_plan_box", container_style=CENTER),
                TextField(value_path="actual", target_id="process_{row}_actual_box", default="", container_style=CENTER),
                TextField(value_path="operator", target_id="process_{row}_operator_box", container_style=TEXT),
            ],
        ),
        FixedSlots(
            value_path="materials",
            capacity=4,
            min_items=0,
            index="row",
            fields=[
                TextField(value_path="name", target_id="material_{row}_name_box", container_style=TEXT),
                TextField(value_path="spec", target_id="material_{row}_spec_box", container_style=TEXT),
                TextField(value_path="quantity", target_id="material_{row}_quantity_box", container_style=CENTER),
            ],
        ),
        TextField(target_id="shipping_method_box", value_path="shipping.method", container_style=TEXT),
        TextField(target_id="destination_box", value_path="shipping.destination", container_style=TEXT),
        TextField(target_id="delivery_time_box", value_path="shipping.time", container_style=CENTER),
        TextField(target_id="printed_count_box", value_path="output.printed", container_style=CENTER),
        TextField(target_id="good_count_box", value_path="output.good", container_style=CENTER),
        TextField(target_id="spare_count_box", value_path="output.spare", container_style=CENTER),
        TextField(target_id="waste_count_box", value_path="output.waste", container_style=CENTER),
        TextField(target_id="box_count_box", value_path="output.boxes", container_style=CENTER),
        TextField(target_id="weight_box", value_path="output.weight", container_style=CENTER),
        TextField(target_id="slip_box", value_path="output.slip", container_style=CENTER),
        TextField(target_id="notes_box", value_path="notes", default="", container_style=TEXT),
        TextField(target_id="final_check_box", value_path="final_check", default="", container_style=TEXT),
        TextField(target_id="inspector_box", value_path="people.inspector", container_style=CENTER),
        TextField(target_id="packer_box", value_path="people.packer", container_style=CENTER),
        TextField(target_id="shipper_check_box", value_path="people.shipper", default="", container_style=CENTER),
    ],
)
