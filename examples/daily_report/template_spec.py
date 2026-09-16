"""作業日報の各固定行を定義する。"""

from pathlib import Path

from svgreportbuilder import FixedSlots, SvgReportTemplate, TextField


TEXT = {
    "font-family": '"Yu Gothic", "Meiryo", sans-serif',
    "font-size": "2.5px",
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
        TextField(target_id="report_number_box", value_path="report.number", container_style=CENTER),
        TextField(target_id="submit_date_box", value_path="report.submit_date", container_style=CENTER),
        TextField(target_id="department_box", value_path="worker.department", container_style=TEXT),
        TextField(target_id="employee_name_box", value_path="worker.name", container_style=TEXT),
        TextField(target_id="employee_number_box", value_path="worker.employee_number", container_style=CENTER),
        TextField(target_id="shift_box", value_path="work.shift", container_style=CENTER),
        TextField(target_id="work_date_box", value_path="work.date", container_style=CENTER),
        TextField(target_id="weather_box", value_path="work.weather", container_style=CENTER),
        TextField(target_id="start_time_box", value_path="work.start", container_style=CENTER),
        TextField(target_id="end_time_box", value_path="work.end", container_style=CENTER),
        TextField(target_id="actual_hours_box", value_path="work.actual", container_style=CENTER),
        TextField(target_id="break_time_box", value_path="work.break", container_style=CENTER),
        TextField(target_id="workplace_box", value_path="work.place", container_style=TEXT),
        FixedSlots(
            value_path="tasks",
            capacity=6,
            min_items=1,
            index="row",
            fields=[
                TextField(value_path="time", target_id="work_{row}_time_box", container_style=CENTER),
                TextField(value_path="content", target_id="work_{row}_content_box", container_style=TEXT),
                TextField(value_path="job_number", target_id="work_{row}_job_number_box", container_style=CENTER),
                TextField(value_path="hours", target_id="work_{row}_hours_box", container_style=CENTER),
            ],
        ),
        FixedSlots(
            value_path="materials",
            capacity=5,
            min_items=0,
            index="row",
            fields=[
                TextField(value_path="name", target_id="material_{row}_name_box", container_style=TEXT),
                TextField(value_path="spec", target_id="material_{row}_spec_box", container_style=TEXT),
                TextField(value_path="quantity", target_id="material_{row}_quantity_box", container_style=CENTER),
                TextField(value_path="unit", target_id="material_{row}_unit_box", container_style=CENTER),
                TextField(value_path="note", target_id="material_{row}_note_box", default="", container_style=TEXT),
            ],
        ),
        FixedSlots(
            value_path="machines",
            capacity=4,
            min_items=0,
            index="row",
            fields=[
                TextField(value_path="name", target_id="machine_{row}_name_box", container_style=TEXT),
                TextField(value_path="model", target_id="machine_{row}_model_box", container_style=TEXT),
                TextField(value_path="hours", target_id="machine_{row}_hours_box", container_style=CENTER),
                TextField(value_path="note", target_id="machine_{row}_note_box", default="", container_style=TEXT),
            ],
        ),
        FixedSlots(
            value_path="allocation",
            capacity=5,
            min_items=1,
            index="row",
            fields=[
                TextField(value_path="name", target_id="allocation_{row}_name_box", container_style=CENTER),
                TextField(value_path="hours", target_id="allocation_{row}_hours_box", container_style=CENTER),
            ],
        ),
        TextField(target_id="notes_box", value_path="notes", default="", container_style=TEXT),
        TextField(target_id="worker_sign_box", value_path="worker.name", container_style=CENTER),
        TextField(target_id="leader_sign_box", value_path="approval.leader", default="", container_style=CENTER),
        TextField(target_id="confirmed_date_box", value_path="approval.date", default="", container_style=CENTER),
    ],
)
