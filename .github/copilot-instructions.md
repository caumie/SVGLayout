# あなたの成長のために必要で行うこと
./.github/copilot-instructions_YYYYMMDD.md、へ学んだことや指摘されたことをMarkdown形式で追記してください。内容としては「ユーザーはどのようなことを関心事としているか」「AIの返答として何を改善すると良いか」「コードと指摘からわかるプロジェクトの内容」です。


# SVGを先に定義してデータ構造を生成するレポート生成ライブラリ

## 概要
本ライブラリは、最初にSVGテンプレートを作り、そのテンプレート内のプレースホルダーや繰り返し要素などを解析して、対応するPythonのデータ構造（dataclassやTypedDictなど）を自動生成または補完します。これにより、テンプレートとデータモデル間の不整合を防ぎ、帳票やレポートの作成をスムーズに行えます。

## 特徴
- **SVG優先のワークフロー**: はじめにSVGを準備し、テンプレートの構造に沿ってデータモデルを生成・カスタマイズ。
- **自動解析**: SVG内の`data-id`や`<foreignObject>`, `<g>`タグを自動的に解析し、対応するフィールド定義を出力。
- **柔軟なデータ定義**: 自動生成されたデータ構造をベースに、dataclassやTypedDict形式で拡張可能。
- **型安全性**: 生成されたデータ定義を用いて、MyPyなどの型チェックが可能。
- **ネスト・繰り返し対応**: 繰り返し要素（テーブル行など）やネストされた構造にも対応。

## インストール
```bash
pip install svgreportbuilder
```

## 使い方の流れ

1. **SVGテンプレートの作成**
   - `<foreignObject>`や`<g>`に`data-id`属性を付与し、テキストや画像を差し込みたい箇所をマークします。
   - 繰り返し要素（テーブル行など）の場合、同じ`data-id`を持つ要素をひとまとまりに定義します。

   ```xml
   <svg xmlns="http://www.w3.org/2000/svg" width="500" height="700">
     <foreignObject x="10" y="10" width="480" height="50" data-id="company_name">
       <div xmlns="http://www.w3.org/1999/xhtml" style="font-size:24px; font-weight:bold;">Placeholder Company</div>
     </foreignObject>
     <g data-id="line_items">
       <!-- 繰り返し要素の例 -->
       <foreignObject x="10" y="100" width="300" height="30" data-id="item_name">
         <div xmlns="http://www.w3.org/1999/xhtml" style="font-size:14px;">Placeholder Item Name</div>
       </foreignObject>
       <foreignObject x="350" y="100" width="100" height="30" data-id="item_price">
         <div xmlns="http://www.w3.org/1999/xhtml" style="font-size:14px; text-align:right;">Placeholder Price</div>
       </foreignObject>
     </g>
   </svg>
   ```

2. **SVGテンプレートからデータ構造を生成**
   - 付属のコマンドやスクリプト（例: `svg2model.py`）を使用して、テンプレートを解析します。
   - テンプレート内の`data-id`に対応するフィールドが自動抽出され、PythonのdataclassやTypedDictの定義が生成されます。

   ```bash
   # 例: svg2model.pyを使ってモデルファイルを生成
   python svg2model.py invoice_template.svg --output invoice_model.py
   ```

   - 出力例（dataclassの場合）:
     ```python
     from dataclasses import dataclass, field
     from typing import List

     @dataclass
     class LineItem:
         item_name: str
         item_price: float

     @dataclass
     class InvoiceModel:
         company_name: str
         line_items: List[LineItem] = field(default_factory=list)
     ```

3. **データを作成し、マッピングを実行**
   - 生成されたデータモデルを読み込み、値を設定した辞書やdataclassインスタンスを用意します。
   - `SVGReportBuilder`(仮)にテンプレートとデータを渡してマッピングを実行します。

   ```python
   from invoice_model import InvoiceModel, LineItem
   from svgreportbuilder import SVGReportBuilder

   # データを用意
   invoice_data = InvoiceModel(
       company_name="B Corp.",
       line_items=[
           LineItem(item_name="Product A", item_price=10.0),
           LineItem(item_name="Product B", item_price=15.5)
       ]
   )

   # ビルダーでマッピング
   builder = SVGReportBuilder(template_file="invoice_template.svg", data=invoice_data)
   builder.map_data()
   builder.save("output_invoice.svg")
   ```

4. **SVGの出力**
   - マッピング後、指定された`data-id`の場所にテキストや画像が挿入されたSVGファイルが生成されます。
   - 必要に応じてCairoSVGなどを使用してPDF変換も可能です。

## 高度な機能
- **条件付き表示**: データ値に応じて特定要素を表示・非表示にしたり、スタイルを切り替えるロジックを設定可能。
- **フォーマッタ**: 数値や日付などの表示形式を切り替えるためのフォーマッタ関数を導入。
- **レイアウト調整**: 長い文字列を折り返す、文字サイズを自動調整する、繰り返し要素の高さを可変にするなどの機能も拡張可能。
- **型チェック**: MyPyやPyrightなどを活用し、生成されたモデルと実際のデータの整合性を担保。

## よくある質問
1. **PDF変換はできますか？**
   - 生成後のSVGをCairoSVGなどでPDFに変換できます。
2. **画像を挿入したい場合は？**
   - `<foreignObject>`内に`<img>`タグを仕込むか、`<image>`タグを使って`data-id`を設定し、画像パスを動的に埋め込むことが可能です。
3. **テンプレートの一括生成・更新は？**
   - 複数のSVGテンプレートを同時に解析し、モデルを一括生成する機能も拡張が可能です。

## ライセンス
MIT License (MIT)。自由に利用・改変・再配布していただけます。

## コントリビューション
バグ報告、機能追加のリクエスト、プルリクエストは大歓迎です。GitHubのリポジトリでお待ちしています。

