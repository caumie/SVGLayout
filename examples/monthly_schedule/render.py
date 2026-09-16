"""月間予定表のサンプルデータをレンダリングする。"""

from pathlib import Path

from svgreportbuilder import Data

from .template_spec import svg_report_template


def _day(
    date: int,
    weekday: str,
    *,
    week: str,
    am: str = "",
    pm: str = "",
    category: str = "",
    memo: str = "",
    weekend: bool = False,
) -> Data:
    return {
        "week": week,
        "date": date,
        "weekday": weekday,
        "am": am,
        "pm": pm,
        "category": category,
        "memo": memo,
        "row_fill": "#f1f3f5" if weekend else "#fff",
    }


data: Data = {
    "period": {"month": "2026年9月", "department": "総務課", "author": "山田 太郎"},
    "days": [
        _day(1, "火", week="第1週", am="始業MTG", pm="資料作成", category="会議", memo="A社：14時～"),
        _day(2, "水", week="第1週", am="庁内連絡調整", pm="企画書作成", category="作業"),
        _day(3, "木", week="第1週", am="来客対応", category="来客", memo="会議室予約済"),
        _day(4, "金", week="第1週"),
        _day(5, "土", week="第1週", category="休日", weekend=True),
        _day(6, "日", week="第1週", category="休日", weekend=True),
        _day(7, "月", week="第2週", am="定例会議", pm="議事録作成", category="会議", memo="10時～ 会議室B"),
        _day(8, "火", week="第2週", am="予算資料確認", category="作業"),
        _day(9, "水", week="第2週"),
        _day(10, "木", week="第2週"),
        _day(11, "金", week="第2週"),
        _day(12, "土", week="第2週", category="休日", weekend=True),
        _day(13, "日", week="第2週", category="休日", weekend=True),
        _day(14, "月", week="第3週", am="資料作成", pm="打合せ（B社）", category="来客", memo="B社 来庁"),
        _day(15, "火", week="第3週"),
        _day(16, "水", week="第3週"),
        _day(17, "木", week="第3週"),
        _day(18, "金", week="第3週", am="月次報告まとめ", category="作業", memo="17時まで提出"),
        _day(19, "土", week="第3週", category="休日", weekend=True),
        _day(20, "日", week="第3週", category="休日", weekend=True),
        _day(21, "月", week="第4週", am="会議資料作成", pm="定例会議", category="会議"),
        _day(22, "火", week="第4週"),
        _day(23, "水", week="第4週", am="来客対応（C社）", category="来客", memo="13:30～"),
        _day(24, "木", week="第4週"),
        _day(25, "金", week="第4週"),
        _day(26, "土", week="第4週", category="休日", weekend=True),
        _day(27, "日", week="第4週", category="休日", weekend=True),
        _day(28, "月", week="第5週", am="次月計画作成", category="作業"),
        _day(29, "火", week="第5週"),
        _day(30, "水", week="第5週", am="庁内清掃", category="他", memo="全員参加"),
        _day(31, "木", week="第5週"),
    ],
    "notes": "月末までに次月予定を確定。休日直前の案件は前日までに引継ぎ確認。",
    "approval": {"created_by": "山田", "checked_by": "佐藤", "created_date": "9/1"},
}


if __name__ == "__main__":
    output_path = Path(__file__).with_name("output.svg")
    output_path.write_text(svg_report_template.render(data), encoding="utf-8")
    print(output_path)
