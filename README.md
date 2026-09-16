# SVGReportBuilder

固定レイアウトの SVG テンプレートへ、テキスト・画像・データ由来の背景色や枠線を差し込みます。帳票の SVG と表示定義は `SvgReportTemplate` にまとめ、`render(data)` で出力 SVG 文字列を取得します。

```python
from pathlib import Path

from svgreportbuilder import FixedSlots, SvgReportTemplate, TextField

report = SvgReportTemplate(
    svg=Path("invoice.svg").read_text(encoding="utf-8"),
    fields=[
        TextField(
            value_path="customer.name",
            target_id="customer_name_box",
        ),
        FixedSlots(
            value_path="items",
            capacity=12,
            index="row",
            fields=[
                TextField(
                    value_path="name",
                    target_id="item_{row}_name_box",
                ),
                TextField(
                    value_path="quantity",
                    target_id="item_{row}_quantity_box",
                ),
            ],
        ),
    ],
)

output_svg = report.render({
    "customer": {"name": "株式会社サンプル"},
    "items": [
        {"name": "ノートPC", "quantity": 2},
    ],
})
```

`FixedSlots` は SVG にあらかじめ用意した枠へ配列を割り当てます。`capacity=12` なら、データが2件のとき残り10枠は空欄になります。データが枠数を超える場合は `SvgDataError` です。

枠ごとに条件を入れたいときは、`fields` にフィールドを返す関数を置けます。

```python
FixedSlots(
    value_path="items",
    capacity=3,
    index="row",
    fields=[
        lambda row: TextField(
            value_path="name",
            target_id="item_{row}_name_box",
            foreign_object_style={
                "overflow": "visible" if row == 0 else "hidden",
            },
        ),
    ],
)
```

背景色と枠線は、データパスをフィールドへ指定します。`None` は SVG テンプレートの色を維持し、文字列の `"none"` は塗りや枠線をなくします。

```python
TextField(
    value_path="buyer.name",
    target_id="buyer_name_box",
    target_fill_path="appearance.buyer_fill",
    target_stroke_path="appearance.buyer_stroke",
)

data = {
    "buyer": {"name": "株式会社サンプル 御中"},
    "appearance": {
        "buyer_fill": "#fff3cd",
        "buyer_stroke": "#b7791f",
    },
}
output_svg = report.render(data)
```

画像は `ImageSource` で渡します。`ImageField` の `image_style` は生成する XHTML `img`、`container_style` はその親 `div`、`foreign_object_style` は SVG `foreignObject` に適用されます。`remove_stroke=True` は対象 `rect` の枠線を常に非表示にし、`hide_target=True` は対象 `rect` だけを非表示にします。

パスはドット区切りで、固定枠内では現在の配列要素を起点にします。`$.appearance.fill` のように `$` を付けると、常に `render(data)` のルートを起点にできます。

ライブラリは SVG ファイルの読込・保存、行の自動生成、改ページ、複数ページの結合を行いません。必要なら呼び出し側でファイルを読み、返却された文字列を保存してください。

## 開発

```bash
uv sync
uv run pytest
uv run mypy
```

詳細な動作規則は [spec.md](spec.md) にあります。
