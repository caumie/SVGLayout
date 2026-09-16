"""車両点検表のフィールド定義。"""

from pathlib import Path

from svgreportbuilder import FixedSlots, SvgReportTemplate, TextField

TEXT = {
    "font-family": '"Yu Gothic", "Meiryo", sans-serif',
    "font-size": "3px",
    "line-height": "1",
    "padding": "1px",
    "white-space": "pre-wrap",
    "box-sizing": "border-box",
    "display": "flex",
    "flex-direction": "column",
    "justify-content": "center",
    "overflow": "hidden",
}
CENTER = TEXT | {"font-size": "0.1em", "text-align": "center"}


svg_report_template = SvgReportTemplate(
    svg=Path(__file__).with_name("template.svg").read_text(encoding="utf-8"),
    fields=[
        TextField(
            target_id="inspection_date_box",
            value_path="inspection.date",
            container_style=CENTER
            | {
                "color": "#f8f9fc",
                "font-weight": "700",
            },
            hide_target=True,
        ),
        TextField(
            target_id="inspection_type_box",
            value_path="inspection.type",
            container_style=CENTER
            | {
                "color": "#f8f9fc",
                "font-weight": "700",
            },
            hide_target=True,
        ),
        TextField(
            target_id="vehicle_id_box", value_path="vehicle.id", container_style=TEXT
        ),
        TextField(
            target_id="vehicle_type_box",
            value_path="vehicle.type",
            container_style=TEXT,
            remove_stroke=True,
        ),
        TextField(
            target_id="registration_box",
            value_path="vehicle.registration",
            container_style=TEXT,
            remove_stroke=True,
        ),
        TextField(
            target_id="driver_box", value_path="vehicle.driver", container_style=TEXT
        ),
        TextField(
            target_id="inspection_time_box",
            value_path="inspection.time",
            container_style=TEXT,
            remove_stroke=True,
        ),
        TextField(
            target_id="mileage_box",
            value_path="vehicle.mileage",
            container_style=CENTER,
            remove_stroke=True,
        ),
        TextField(
            target_id="inspector_box",
            value_path="people.inspector",
            container_style=TEXT,
            remove_stroke=True,
        ),
        TextField(
            target_id="manager_box", value_path="people.manager", container_style=TEXT
        ),
        TextField(
            target_id="record_number_box",
            value_path="inspection.record_number",
            container_style=CENTER,
            remove_stroke=True,
        ),
        FixedSlots(
            value_path="items",
            capacity=18,
            min_items=1,
            index="row",
            fields=[
                TextField(
                    value_path="category",
                    target_id="item_{row}_category_box",
                    container_style=TEXT,
                ),
                TextField(
                    value_path="name",
                    target_id="item_{row}_name_box",
                    container_style=TEXT,
                ),
                TextField(
                    value_path="status",
                    target_id="item_{row}_status_box",
                    container_style=CENTER,
                    target_fill_path="status_fill",
                ),
                TextField(
                    value_path="remarks",
                    target_id="item_{row}_remarks_box",
                    default="",
                    container_style=TEXT,
                ),
            ],
        ),
        TextField(
            target_id="notes_box", value_path="notes", default="", container_style=TEXT
        ),
        TextField(
            target_id="inspector_sign_box",
            value_path="people.inspector",
            container_style=CENTER,
            remove_stroke=True,
        ),
        TextField(
            target_id="manager_sign_box",
            value_path="people.manager",
            default="",
            container_style=CENTER,
            remove_stroke=True,
        ),
        TextField(
            target_id="next_inspection_box",
            value_path="inspection.next_date",
            container_style=CENTER,
            remove_stroke=True,
        ),
    ],
)
