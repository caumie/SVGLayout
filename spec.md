# SVGReportBuilder 仕様

本書は、公開 API とその動作を定める。旧 API との互換層は設けない。

## 1. 責務

固定レイアウトの SVG とデータの対応を `SvgReportTemplate` にまとめ、`render(data)` で1つの SVG 文字列を生成する。

```text
SvgReportTemplate(svg=SVG文字列, fields=フィールド定義) -> 帳票テンプレート
帳票テンプレート.render(data) -> SVG文字列
```

SVG に用意された ID 付き `rect` を描画先とし、その領域へテキストや画像を差し込む。ファイルの読込・保存、行の生成、改ページ、複数ページの結合は呼び出し側が担当する。

### 1.1. 描画機能の継続

帳票とフィールドの定義方式を新しくし、今回の定義方式・固定枠・検証時点の規則と矛盾しない既存の描画仕様は維持する。データによる背景色・枠線の変更も、通常のフィールド、固定枠内のフィールド、関数が返すフィールドで共通して使用できる。

| 機能 | 新しい定義での指定・動作 |
| --- | --- |
| データによる背景色の変更 | `TextField`／`ImageField` の `target_fill_path` から、描画時に対象 `rect` の `fill` を取得する |
| データによる枠線の変更 | `target_stroke_path` から、描画時に対象 `rect` の `stroke` を取得する |
| 塗りなし・枠線なしの表示 | データの文字列 `"none"`、および定義の `remove_stroke=True` を使用する |
| 対象枠全体の非表示 | `hide_target=True` を使用する |
| 文字組み・余白・画像の配置 | `container_style`、`foreign_object_style`、`image_style` を使用する |
| 既定値と空の表示 | `default`、`UNSET`、`None` を第4・7節の規則で扱う。固定枠の空きは第5節で扱う |
| 画像の埋め込み | `ImageSource` のバイト列と MIME から Data URI を生成する |
| 元の SVG と繰り返し描画 | 元の SVG を保存し、毎回そこから描画する。指定のない塗り・枠線・style・内部参照を保持する |
| 生成結果の検査 | `svgrb-*` クラスと `data-svgrb-*` 属性を付ける |

## 2. 定義の基本形

```python
from pathlib import Path

from svgreportbuilder import FixedSlots, SvgReportTemplate, TextField

svg_report_template = SvgReportTemplate(
    svg=Path("report.svg").read_text(encoding="utf-8"),
    fields=[
        TextField(
            value_path="page.title",
            target_id="header_title_box",
            target_fill_path="appearance.title_fill",
        ),
        TextField(
            value_path="page.title",
            target_id="footer_title_box",
        ),
        FixedSlots(
            value_path="items",
            capacity=3,
            min_items=1,
            index="row",
            fields=[
                lambda row: TextField(
                    value_path="name",
                    target_id="item_{row}_name_box",
                    target_fill_path="appearance.fill",
                    target_stroke_path="appearance.stroke",
                    foreign_object_style=(
                        {"overflow": "visible"} if row == 0 else {}
                    ),
                ),
                TextField(
                    value_path="quantity",
                    target_id="item_{row}_quantity_box",
                    container_style={"text-align": "right"},
                ),
            ],
        ),
    ],
)

output_svg = svg_report_template.render({
    "page": {"title": "納品書"},
    "appearance": {"title_fill": "#fff3cd"},
    "items": [{
        "name": "ノートPC",
        "quantity": 2,
        "appearance": {"fill": "#e8f4ff", "stroke": "#2874a6"},
    }],
})
```

この例の `report.svg` には、タイトル用の2つの `rect` と、添字が `0`、`1`、`2` の品名・数量用 `rect` を用意する。タイトルは2箇所に表示し、明細は1件目へ割り当て、残り2件分は空欄にする。

ヘッダーの背景色はルートの `appearance.title_fill`、品名欄の背景色と枠線は各明細の `appearance.fill` と `appearance.stroke` から取得する。関数はデータパスを持つフィールドを構築し、色の取得は `render(data)` のたびに行う。

フィールドは表示箇所ごとに列挙する。同じ `value_path` を複数のフィールドで使用でき、それぞれ別のスタイルや既定値を持てる。展開後の `target_id` は帳票全体で重複できない。

## 3. `SvgReportTemplate`

```python
SvgReportTemplate(svg=template_svg, fields=[...])
```

| 引数 | 型・内容 |
| --- | --- |
| `svg` | SVG 本体の `str`。パスや URL としては解釈しない |
| `fields` | `TextField`、`ImageField`、`FixedSlots` の順序付き列 |

本書の定義用コンストラクターの引数はキーワード専用とする。

構築時に SVG、固定枠の展開結果、全フィールドを検証する。入力の `fields` やスタイル辞書、および入れ子の定義はスナップショットとして保持し、構築後の外部からの変更で帳票の動作を変えない。関数から返された定義も同じ扱いとする。

`render(data)` はデータを検証して SVG 文字列を返す。毎回、保存した元の SVG 文字列から XML を再構築するため、同じ帳票テンプレートを複数回使える。前回の出力や呼び出し側のデータを変更しない。生成済み SVG をテンプレートとして再入力することは対応範囲外とする。

## 4. フィールド

### 4.1. 共通の引数

| 引数 | 既定値 | 意味 |
| --- | --- | --- |
| `value_path` | 必須 | 表示する値のデータパス |
| `target_id` | 必須 | 描画先 `rect` の ID。固定枠内では添字の置換を利用できる |
| `default` | `UNSET` | 値が見つからない場合に使用する値 |
| `container_style` | `{}` | 内部の XHTML `div` に適用するスタイル |
| `foreign_object_style` | `{}` | SVG `foreignObject` に適用するスタイル |
| `hide_target` | `False` | 対象 `rect` に `visibility="hidden"` を設定する |
| `remove_stroke` | `False` | 対象 `rect` の枠線を非表示にする |
| `target_fill_path` | `None` | 対象 `rect` の塗りの値を取得するデータパス |
| `target_stroke_path` | `None` | 対象 `rect` の枠線の値を取得するデータパス |

`hide_target` は対象の `rect` だけに作用し、差し込む文字や画像を非表示にはしない。`remove_stroke=True` はデータから取得した `stroke` より優先する。

`target_fill_path`／`target_stroke_path` は元の SVG の枠を変更する。`container_style` はその上に差し込む XHTML `div` の文字組み・余白・背景などに作用し、元の `rect` の `fill`／`stroke` は変更しない。

### 4.2. `TextField`

```python
TextField(
    value_path="customer.name",
    target_id="customer_name_box",
    default="",
    container_style={"font-size": "12px"},
    remove_stroke=True,
    target_fill_path="$.appearance.customer_fill",
)
```

対象 `rect` の直後に、同じ `x`、`y`、`width`、`height` を持つ SVG `foreignObject` を追加する。その中の XHTML `div` へプレーンテキストを設定する。

値と `default` は `str`、`int`、`float`、`bool`、`None` を受け付ける。`None` は空文字列、それ以外は Python の `str()` により文字列化する。HTML として解釈しない。文字列化したテキストに XML 1.0 禁止文字が含まれる場合は `SvgDataError` とする。

### 4.3. `ImageField`

```python
ImageField(
    value_path="issuer.logo",
    target_id="issuer_logo_box",
    default=None,
    container_style={"padding": "1px"},
    image_style={"object-fit": "contain"},
)
```

`TextField` と同じ領域に `foreignObject` と XHTML `div` を追加し、その中へ XHTML `img` を生成する。追加の引数 `image_style` は既定値 `{}` で、`img` に適用する。

値と `default` は `ImageSource` または `None` を受け付ける。`None` なら `img` を生成しない。`UNSET` は既定値が未指定であることを示す。

## 5. `FixedSlots`

配列の各要素に1件分のフィールド定義を適用し、SVG に用意された固定枠へ割り当てる。

```python
FixedSlots(
    value_path="items",
    capacity=12,
    index="row",
    min_items=0,
    fields=[
        TextField(value_path="name", target_id="item_{row}_name_box"),
        TextField(value_path="quantity", target_id="item_{row}_quantity_box"),
    ],
)
```

| 引数 | 既定値 | 意味 |
| --- | --- | --- |
| `value_path` | 必須 | 割り当てる配列のデータパス |
| `capacity` | 必須 | テンプレートに用意された枠数。正の整数 |
| `index` | 必須 | 描画先 ID の置換に使用する添字名 |
| `fields` | 必須 | 1件分のフィールド定義の順序付き列 |
| `min_items` | `0` | 必要な最小件数。`0 <= min_items <= capacity` の整数 |

`capacity` と `min_items` には真偽値を受け付けない。`fields` の各要素には `TextField`、`ImageField`、入れ子の `FixedSlots`、または第6節の関数を指定できる。

### 5.1. 割り当てと空き枠

配列は `list` または `tuple`、各要素は文字列キーの `Mapping` とする。並べ替えや要素の除外は行わず、配列の添字と枠の添字を一致させる。

| データの状態 | 動作 |
| --- | --- |
| `min_items` 以上、`capacity` 以下 | 配列順に割り当てる |
| 件数が `min_items` 以上、`capacity` 未満 | 余った枠を空欄にする |
| 空配列で `min_items=0` | 全枠を空欄にする |
| 件数が `min_items` 未満、または `capacity` 超過 | `SvgDataError` |
| 配列のパスが見つからない、`None`、配列以外 | `SvgDataError` |
| 配列の要素が `Mapping` 以外 | `SvgDataError` |

空き枠では、テキストは空文字列、画像は `img` なしとして描画する。各フィールドの `default` は適用せず、`value_path`、`target_fill_path`、`target_stroke_path` のデータ参照も行わない。固定のスタイル、`hide_target`、`remove_stroke` は適用する。データ由来の塗り・枠線を適用しない部分では、元の SVG の指定を維持する。

存在する要素で項目が欠落した場合は、そのフィールドの `default` を使う。`default` が未指定なら `SvgDataError` とする。空き枠と項目欠落は別の状態として扱う。

### 5.2. 添字と描画先 ID

添字は `0` から `capacity - 1` までとする。`index="row"` なら、`target_id="item_{row}_name_box"` を `item_0_name_box`、`item_1_name_box` のように展開する。

`index` は `[A-Za-z_][A-Za-z0-9_]*` に一致する名前とする。置換は `target_id` にだけ適用し、データパスやスタイル文字列には適用しない。未知の添字名や不正な波括弧は `SvgSpecError` とする。置換は `{名前}` のみを受け付け、式・属性アクセス・書式指定は解釈しない。文字としての波括弧は `{{`、`}}` で表す。

通常の文字列として渡した置換指定も、関数が返した `target_id` の置換指定も同じ規則で処理する。関数内で f-string などにより ID を組み立て、確定した ID を返すこともできる。

ID の単数形・複数形変換や、SVG からの枠数の推測は行わない。全枠について展開し、実際のデータ件数にかかわらず描画先の存在と重複を構築時に検証する。

### 5.3. 入れ子

`FixedSlots` の中に `FixedSlots` を置ける。内側の `value_path` は外側の現在要素から配列を参照する。内側のフィールドの `target_id` では、外側と内側の添字名を使用できる。

例えば外側を `index="group"`、内側を `index="row"` とすれば、`group_{group}_item_{row}_name_box` と記述できる。祖先と同じ添字名の再定義は `SvgSpecError` とする。独立した兄弟の `FixedSlots` では同じ添字名を使用できる。

外側が空き枠なら、その配下もすべて空き枠とし、内側のデータ参照と `min_items` の検証は行わない。外側の要素が存在する場合は、内側の配列も通常どおり検証する。

## 6. フィールド単位の関数

`FixedSlots.fields` の要素として、次の型の関数を直接置ける。

```text
Callable[[int], TextField | ImageField]
```

通常のフィールドは各枠に同じ定義を適用する。関数は、枠の添字を受け取り、その枠用のフィールドを1つ返す。

```python
FixedSlots(
    value_path="items",
    capacity=3,
    index="row",
    fields=[
        lambda row: TextField(
            value_path="name",
            target_id="item_{row}_name_box",
            foreign_object_style=(
                {"overflow": "visible"} if row == 0 else {}
            ),
        ),
        TextField(value_path="quantity", target_id="item_{row}_quantity_box"),
    ],
)
```

- 関数は `SvgReportTemplate` の構築時に各枠について1回ずつ呼び出す。`FixedSlots` を作るだけでは呼び出さない。
- 展開順は各枠の添字順、その枠内では `fields` の記述順とする。入れ子はその位置で展開する。
- 入れ子の関数へ渡すのは、直接所属する `FixedSlots` の添字だけとする。外側の添字は `target_id` の置換で利用できる。
- 表示データは渡さない。`render(data)` では関数を再実行しない。
- 関数名や仮引数名は自由とし、引数は位置引数で渡す。ラムダと名前付き関数を同じように扱う。
- 返り値は `TextField` または `ImageField` の1つとする。`None`、列、`FixedSlots`、別の関数は受け付けない。
- 関数から返されたフィールドも、通常のフィールドと同じ置換・スナップショット化・検証を行う。
- 関数の実行失敗や不正な返り値は、所属する `FixedSlots`、枠の添字、フィールドの位置を示す `SvgSpecError` とする。実行失敗では元の例外を原因として保持する。

関数には渡された添字から定義を返す処理を書く。非同期関数は受け付けない。帳票直下の `fields` には枠の添字がないため、この関数形式は使用できない。

## 7. データ参照

### 7.1. データとパス

`render(data)` の `data` は文字列キーの `Mapping` とする。データは `str`、`int`、`float`、`bool`、`None`、`ImageSource`、文字列キーの `Mapping`、`list`、`tuple` で構成する。任意のオブジェクト属性は参照しない。

公開の型 `TextValue`、`DataValue`、`Data` と、欠落を表す `UnsetType`／`UNSET` を継続して使用する。表示値と `appearance` などの装飾値を同じ入力データに持てる。帳票定義で参照先を指定するため、新しい定義方式に合わせて入力データのキーを変更する必要はない。

パスはドット区切りで、次の順に各要素を参照する。

1. 現在の値が `Mapping` なら、文字列キーとして参照する。
2. `list` または `tuple` なら、非負の10進整数の添字として参照する。

空のパス、空のパス要素、XML 1.0 禁止文字を含むパスは `SvgSpecError` とする。キーのドットをエスケープする構文、ワイルドカード、属性アクセス、式の評価は提供しない。

### 7.2. 参照の起点

接頭辞のないパスは現在のデータを基準にする。帳票直下ではルート、`FixedSlots` 内ではその枠に割り当てられた要素が起点となる。

`$.` で始まるパスは、常に `render(data)` に渡したルートを起点とする。この接頭辞は `value_path`、`FixedSlots.value_path`、`target_fill_path`、`target_stroke_path` に共通で使用できる。

例えば明細内の `value_path="name"` は現在の明細の品名、`target_fill_path="$.appearance.item_fill"` はルートの共通色を参照する。相対パスが見つからなくても、ルートへ参照し直す処理は行わない。

### 7.3. 欠落と `None`

パスの途中でキーや添字が見つからない、または値をそれ以上たどれない場合は欠落として扱う。フィールドの `default` が `UNSET` 以外ならその値を使い、そうでなければ `SvgDataError` とする。取得できた値の型がフィールドに適さない場合は、`default` で補わず `SvgDataError` とする。

最終的に取得した値が `None` の場合は欠落ではない。テキストは空文字列、画像は `img` なしとし、`default` は適用しない。配列自体と配列要素の検証は第5節の規則による。

### 7.4. データによる背景色・枠線の変更

`TextField` と `ImageField` のどちらでも、`target_fill_path` と `target_stroke_path` を指定した場合、参照先の文字列を対象 `rect` の `fill` と `stroke` へ適用する。色は `render(data)` のたびに取得し、同じ帳票テンプレートへ異なるデータを渡して変更できる。

| 指定・値 | 動作 |
| --- | --- |
| パス引数が `None`、または未指定 | 対応する塗り・枠線のデータ参照を行わない |
| 参照先の値が `"#fff3cd"` などの文字列 | 対応する `fill`／`stroke` の値として適用する |
| 参照先の値が文字列 `"none"` | `fill:none`／`stroke:none` により塗り・枠線をなくす |
| 参照先の値が Python の `None` | 対応する塗り・枠線を元の SVG の指定から変更しない |
| 指定したパスが見つからない、または値が文字列と `None` 以外 | `SvgDataError` |
| セミコロンや XML 1.0 禁止文字など、第9節に反する CSS 文字列 | `SvgDataError` |

文字列 `"none"` と Python の `None` は区別する。色の文字列は第9節の限定的な CSS 検証を行い、色表現全体を解析する処理は設けない。

例えば、宛先の背景色・枠線と印影領域の塗りなし表示を、次のように指定できる。

```python
svg_report_template = SvgReportTemplate(
    svg=template_svg,
    fields=[
        TextField(
            value_path="buyer.name",
            target_id="buyer_name_box",
            target_fill_path="appearance.buyer_fill",
            target_stroke_path="appearance.buyer_stroke",
        ),
        ImageField(
            value_path="seller.seal",
            target_id="seller_seal_box",
            target_fill_path="appearance.seller_seal_fill",
            remove_stroke=True,
        ),
    ],
)

data = {
    "buyer": {"name": "株式会社サンプル 御中"},
    "seller": {"seal": seal_image},  # seal_image は ImageSource
    "appearance": {
        "buyer_fill": "#fff3cd",
        "buyer_stroke": "#b7791f",
        "seller_seal_fill": "none",
    },
}
highlighted_svg = svg_report_template.render(data)

original_colors_svg = svg_report_template.render({
    **data,
    "appearance": {
        "buyer_fill": None,
        "buyer_stroke": None,
        "seller_seal_fill": "none",
    },
})
```

`template_svg` には `buyer_name_box` と `seller_seal_box` の `rect` を用意する。1回目は宛先の背景色と枠線を変更し、2回目は宛先を元の SVG の色で描画する。前回描画した色を引き継がない。印影領域はどちらも塗りなし・枠線なしとし、画像そのものの色は変更しない。

塗り・枠線へのデータ適用は次の順序とする。

1. 指定されたパスから値を取得して検証する。
2. 文字列の値を対象 `rect` の `fill`／`stroke` に適用する。
3. `remove_stroke=True` なら `stroke:none` を優先して適用する。

`remove_stroke=True` でも、`target_stroke_path` が指定されていれば参照と検証は行う。枠線を常に非表示にするだけなら `target_stroke_path` は指定しなくてよい。

フィールドの `default` は塗り・枠線の参照には適用しない。表示値が `None` や既定値でも、存在するデータ要素の塗り・枠線は参照する。固定枠の空きでは第5節に従ってデータ参照を行わず、固定の設定だけを適用する。

## 8. SVG の要件と生成結果

### 8.1. テンプレート

- ルートは SVG 名前空間の `svg` とする。
- SVG 内の ID は重複できない。
- フィールドの描画先は SVG 名前空間の `rect` とする。
- 描画先には `x`、`y`、`width`、`height` が必要。数値または `mm`、`cm`、`in`、`pt`、`pc`、`px` 付きの数値を受け付け、`width` と `height` は正数とする。
- 対象 `rect` 自身の `transform` は受け付けない。祖先の変換は保持する。
- `defs`、`symbol`、`clipPath`、`mask`、`pattern`、`marker` 内の対象は受け付けない。

対象の親、クラス、SVG 内部参照は書き換えない。`hide_target=True` の場合は対象 `rect` へ `visibility="hidden"` を設定する。塗り・枠線を指定する場合は、対象 `rect` の既存 style 末尾へ宣言を追加する。`remove_stroke=True` では `stroke:none` を適用する。

文字列の空白、属性順、名前空間の接頭辞などの字句的な一致は保証しない。

### 8.2. 生成要素の属性

生成する `foreignObject` と内部要素には、検査や CSS・DOM での選択用の属性を付ける。

| 要素 | 属性 |
| --- | --- |
| `foreignObject` | `class="svgrb-field"`、`data-svgrb-target`、`data-svgrb-kind`、`data-svgrb-role="field"`、`data-svgrb-value-path` |
| XHTML `div` | `class="svgrb-container"`、`data-svgrb-role="container"` |
| XHTML `img` | `class="svgrb-image"`、`data-svgrb-role="image"` |

`data-svgrb-target` は展開後の対象 ID、`data-svgrb-kind` は `text` または `image` とする。`data-svgrb-value-path` はルートからの具体的なデータパスとする。相対参照は固定枠の添字を含めて `items.0.name` のように解決する。`$.` によるルート参照は接頭辞を取り除き、例えば `$.page.title` なら `page.title` と記録する。空き枠でも、データを読み取らずに同じ規則でパスを記録する。

生成要素へ新しい ID は付けない。対応する `rect` は `data-svgrb-target` から参照する。表示位置を固定するため、対象 `rect` 自身の座標を CSS で変更する運用は対応範囲外とする。

## 9. CSS

スタイルは文字列キー・文字列値の `Mapping` で指定する。入力の辞書を保持する際にコピーし、ライブラリが生成する style は辞書の順序で直列化する。

- プロパティ名は ASCII の CSS 識別子、または `--` で始まるカスタムプロパティとする。
- プロパティ名と値に XML 1.0 禁止文字を含められない。
- 値にセミコロンを含められない。
- 生成要素では、既定スタイルへ指定スタイルをプロパティ単位で重ねる。
- CSS 全体の構文解析や優先順位計算、既存テンプレートの style の解析は行わない。

`div` の既定スタイルは `width:100%`、`height:100%`、`box-sizing:border-box` とする。`img` は `display:block`、`width:100%`、`height:100%`、`object-fit:contain` を既定とする。

値の中でセミコロンを使う引用符や複数宣言などは受け付けない。複雑な CSS はテンプレート側へ記述する。対象 `rect` の style への追記は、既存 CSS の優先順位に対する上書きを保証するものではない。

## 10. 画像

```python
ImageSource(data=image_bytes, mime_type="image/png")
```

`data` は埋め込む `bytes`、`mime_type` は画像の MIME 文字列とする。出力時に `data:<mime>;base64,...` へ変換する。MIME 文字列の形式を検証するが、画像の内容、MIME との一致、サイズ、バーコードや QR コードの読取可否は検査しない。

画像ファイルの読込や、SVG 画像文字列の UTF-8 化は呼び出し側で行う。

## 11. 検証と例外

`SvgRenderError` を基底例外とし、次の3種類で失敗を分類する。

| 例外 | 主な原因 | 検証時点 |
| --- | --- | --- |
| `SvgSpecError` | 定義の型・引数・パス・生成 CSS の不正、添字置換の不正、描画先の二重指定、フィールド関数の失敗や不正な返り値 | 定義オブジェクトまたは `SvgReportTemplate` の構築時。データから取得する CSS 文字列は `render(data)` 時 |
| `SvgTemplateError` | SVG の構文・名前空間・ID・対象要素・座標の不正、必要な描画先の欠落 | `SvgReportTemplate` の構築時 |
| `SvgDataError` | 必須データの欠落、表示値の型や文字列・画像の不正、塗り・枠線のパスの欠落や値の型の不正、配列の型や件数の不正 | `render(data)` 時 |

構築に成功した帳票は、全枠のフィールド展開とテンプレートの検証が完了している。描画時に空き枠となる可能性があるフィールドも、構築時の検証から除外しない。

エラーメッセージには、特定できる範囲で描画先 ID、ルートからのデータパス、所属する固定枠と添字を含める。ファイル入出力をライブラリで行わないため、ファイル出力専用の API や例外は設けない。
