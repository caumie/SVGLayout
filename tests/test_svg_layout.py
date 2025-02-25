from src.svg_layout import Rectangle


def svg_template():
    # テスト用のSVGテンプレート文字列
    return """
    <svg xmlns="http://www.w3.org/2000/svg" width="500" height="700">
        <foreignObject x="10" y="10" width="480" height="50" data-id="company_name">
            <div xmlns="http://www.w3.org/1999/xhtml">Placeholder Company</div>
        </foreignObject>
        <g data-id="line_items">
            <foreignObject x="10" y="100" width="300" height="30" data-id="item_name">
                <div xmlns="http://www.w3.org/1999/xhtml">Placeholder Item</div>
            </foreignObject>
            <foreignObject x="350" y="100" width="100" height="30" data-id="item_price">
                <div xmlns="http://www.w3.org/1999/xhtml">0.00</div>
            </foreignObject>
        </g>
    </svg>
    """


def test_rectangle():
    rect = Rectangle(10, 10, 100, 50)
    expected_svg = '<rect x="10" y="10" fill="#FFFFFF" stroke="#000000" stroke-width="1" width="100" height="50"/>'
    assert rect.to_svg() == expected_svg


# def test_text_field(self):
#     text_field = TextField(20, 30, "Sample Text")
#     expected_svg = '<text transform="matrix(1 0 0 1 20 30)" font-family="MS-Gothic" font-size="24">Sample Text</text>'
#     self.assertEqual(text_field.to_svg(), expected_svg)


# def test_svg_document(self):
#     svg_doc = SVGDocument(200, 100)
#     svg_doc.add_element(Rectangle(10, 10, 100, 50))
#     svg_doc.add_element(TextField(20, 30, "Sample Text"))
#     expected_svg_start = '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="200" height="100" viewBox="0 0 200 100">'
#     self.assertTrue(svg_doc.to_svg().startswith(expected_svg_start))
#     self.assertIn("</svg>", svg_doc.to_svg())


# def test_svg_manipulator_replace_elements(self):
#     manipulator = SVGManipulator(self.template_svg)
#     replacements = {
#         "company_name": '<foreignObject x="10" y="10" width="480" height="50" data-id="company_name"><div xmlns="http://www.w3.org/1999/xhtml">Test Company</div></foreignObject>'
#     }
#     result = manipulator.replace_elements(replacements)
#     self.assertIn("Test Company", result)


# def test_svg_manipulator_replace_group_elements(self):
#     manipulator = SVGManipulator(self.template_svg)
#     group_replacements = {
#         "line_items": [
#             '<foreignObject x="10" y="100" width="300" height="30" data-id="item_name"><div xmlns="http://www.w3.org/1999/xhtml">Product A</div></foreignObject>',
#             '<foreignObject x="350" y="100" width="100" height="30" data-id="item_price"><div xmlns="http://www.w3.org/1999/xhtml">10.00</div></foreignObject>',
#         ]
#     }
#     result = manipulator.replace_group_elements(group_replacements)
#     self.assertIn("Product A", result)
#     self.assertIn("10.00", result)


# def test_svg_document_with_data_attributes(self):
#     doc = SVGDocument(500, 700)
#     text_field = TextField(20, 30, "Test Text", data_name="company_name")
#     doc.add_element(text_field)
#     svg_output = doc.to_svg()
#     self.assertIn('data-name="company_name"', svg_output)


# def test_overlay_element(self):
#     manipulator = SVGManipulator(self.template_svg)
#     new_element = (
#         '<circle data-name="price_circle" cx="50" cy="50" r="40" fill="green"/>'
#     )
#     result = manipulator.overlay_element("company_name", new_element)
#     self.assertIn("price_circle", result)
#     self.assertIn("company_name", result)


# def test_invalid_data_id(self):
#     manipulator = SVGManipulator(self.template_svg)
#     replacements = {"nonexistent_id": "<text>Test</text>"}
#     with self.assertRaises(ValueError):
#         manipulator.replace_elements(replacements)
