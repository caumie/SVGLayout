"""月間予定表の固定31日分のフィールド定義。"""

from pathlib import Path

from svgreportbuilder import FixedSlots, SvgReportTemplate, TextField


TEXT = {
    "font-family": '"Yu Gothic", "Meiryo", sans-serif',
    "font-size": "2.35px",
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
        TextField(target_id="month_box", value_path="period.month", container_style=CENTER),
        TextField(target_id="department_box", value_path="period.department", container_style=TEXT),
        TextField(target_id="author_box", value_path="period.author", container_style=TEXT),
        FixedSlots(
            value_path="days",
            capacity=31,
            min_items=1,
            index="day",
            fields=[
                TextField(value_path="week", target_id="day_{day}_week_box", container_style=CENTER),
                TextField(value_path="date", target_id="day_{day}_date_box", container_style=CENTER),
                TextField(
                    value_path="weekday",
                    target_id="day_{day}_weekday_box",
                    container_style=CENTER,
                    target_fill_path="row_fill",
                ),
                TextField(value_path="am", target_id="day_{day}_am_box", container_style=TEXT),
                TextField(value_path="pm", target_id="day_{day}_pm_box", container_style=TEXT),
                TextField(value_path="category", target_id="day_{day}_category_box", container_style=CENTER),
                TextField(value_path="memo", target_id="day_{day}_memo_box", default="", container_style=TEXT),
            ],
        ),
        TextField(target_id="notes_box", value_path="notes", default="", container_style=TEXT),
        TextField(target_id="created_by_box", value_path="approval.created_by", container_style=CENTER),
        TextField(target_id="checked_by_box", value_path="approval.checked_by", container_style=CENTER),
        TextField(target_id="created_date_box", value_path="approval.created_date", container_style=CENTER),
    ],
)
