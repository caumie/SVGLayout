# 実務帳票サンプル

このディレクトリには、SVGReportBuilderの機能を実務帳票の形で確認する12の事例があります。

| フォルダ | 帳票 | 主な機能 |
| --- | --- | --- |
| `invoice` | 12行の請求明細一覧 | 大量行、ゼブラ行、記号を含む長文、空行へのdefault、list添字、右寄せ金額、SVG画像、QRコード、データ指定の塗り、固定の枠なし表示 |
| `quotation` | 左右非対称の見積提案シート | 色付きセクション、記号凡例、tuple添字、数値の文字列化、任意値引き、データ指定の枠色・塗り、固定の枠なし印影 |
| `delivery_note` | 3ページの納品書セット | 同一テンプレートのページ分割、ページごとのタイトル差し込み、Renderer再利用、バーコード、任意の受領印、`foreign_object_style` |
| `purchase_order` | 縦レール付き変則発注書 | 非対称配置、社内回覧・承認欄、欠損値default、整数・真偽値、複数画像、記号凡例 |
| `receipt` | 小型領収書 | mm単位、整数・小数・`None`、PNG/SVG画像、チェック記号、データ指定の透明塗り、固定の枠なしロゴ、欠損した任意印影、QRコード |
| `delivery_slip` | A4納品書 | 8行固定明細、空き行、バーコード、受領印、長文の切り詰め |
| `vehicle_inspection` | 車両点検表 | 18行固定点検、判定ごとの色、空き行、注意事項 |
| `monthly_schedule` | A4横の月間予定表 | 31日固定枠、空欄予定、休日色、横長レイアウト |
| `shipping_packing` | 出荷指示兼梱包明細書 | 9行商品明細、資材・注意事項の固定枠、チェック記号、A4内への整形 |
| `daily_report` | 作業日報 | 作業・材料・設備の複数固定枠、空き行、時刻と数量の文字列化 |
| `small_ticket` | 変形小型伝票 | 210×100mmの変形用紙、切り取り控え、サービス・支払チェック |
| `print_process` | 印刷工程進行票 | 7工程固定枠、進捗色、資材・数量確認、未入力欄 |

## 実行

```bash
uv run pytest
uv run mypy
```

個別の帳票は、例えば次のように生成できます。

```bash
python -m examples.invoice.render
python -m examples.delivery_note.render
python -m examples.delivery_slip.render
python -m examples.monthly_schedule.render
```

各フォルダの`render.py`を実行すると、同じフォルダの`template_spec.py`で定義したテンプレートへサンプルデータを差し込み、`template.svg`を元に結果SVGだけを生成します。単一ページは`output.svg`、複数ページは`output-1.svg`、`output-2.svg`のように分割します。比較用HTMLが必要な場合は、各フォルダの静的なHTMLからこれらのSVGを`img`タグで参照します。納品書は`render.py`内のページデータを順に処理して、1つのテンプレートから3ページの結果SVGを生成します。ライブラリの`render()`は1回につき1つのSVG文字列を返します。

各帳票の明細行は固定レイアウトのため、テンプレートへあらかじめ配置しています。最大行数を超えるデータの自動改ページや、行の自動生成はこのライブラリの責務ではありません。

枠なし表示の事例では、`remove_stroke=True`で枠を表示しないことを帳票定義に固定し、`target_fill_path`でデータ投入時の塗りつぶしを指定しています。比較HTMLのテンプレート側には元の枠が見え、結果側にはデータ反映後の塗り・枠が表示されます。
