# import unittest

# from src.svg_layout import SVGManipulator


# class TestSVGManipulator(unittest.TestCase):
#     def setUp(self):
#         self.svg_content = """
#         <svg>
#             <g data-name="group1">
#                 <rect data-name="rect1" width="100" height="100"/>
#                 <text data-name="text1">Old Text</text>
#             </g>
#             <g data-name="group1">
#                 <rect data-name="rect1" width="100" height="100" fill="blue"/>
#             </g>
#             <g data-name="group2">
#                 <rect data-name="rect2" width="200" height="200"/>
#             </g>
#         </svg>
#         """
#         self.manipulator = SVGManipulator(self.svg_content)

#     def test_load_svg(self):
#         manipulator = SVGManipulator("")
#         manipulator.load_svg("tests/usage/example1.svg")  # 例としてファイルを指定
#         self.assertIsNotNone(manipulator.svg_content)

#     def test_overlay_element(self):
#         manipulator = SVGManipulator(self.svg_content)
#         new_element = (
#             '<circle data-name="circle1" cx="50" cy="50" r="40" fill="green"/>'
#         )
#         updated_svg = manipulator.overlay_element("rect1", new_element)
#         self.assertIn("circle1", updated_svg)  # 新しい要素が追加されているか確認

#     def test_replace_elements(self):
#         replacements = {
#             "rect1": '<rect data-name="rect1" width="100" height="100" fill="red"/>',
#             "text1": '<text data-name="text1">New Text</text>',
#         }
#         updated_svg = self.manipulator.replace_elements(replacements)
#         self.assertIn('fill="red"', updated_svg)
#         self.assertIn("New Text", updated_svg)

#     def test_replace_group_elements(self):
#         group_replacements = {
#             "group1": [
#                 '<rect data-name="rect1" width="100" height="100" fill="blue"/>',
#                 '<text data-name="text1">Updated Text</text>',
#             ]
#         }
#         updated_svg = self.manipulator.replace_group_elements(group_replacements)
#         self.assertIn('fill="blue"', updated_svg)
#         self.assertIn("Updated Text", updated_svg)

#     def test_no_replacement(self):
#         group_replacements = {
#             "nonexistent": [
#                 '<rect data-name="rect3" width="100" height="100" fill="green"/>',
#             ]
#         }
#         updated_svg = self.manipulator.replace_group_elements(group_replacements)
#         self.assertEqual(updated_svg, self.svg_content)  # No changes should be made

#     def test_group_with_same_name(self):
#         group_replacements = {
#             "group1": [
#                 '<rect data-name="rect1" width="100" height="100" fill="yellow"/>',
#                 '<text data-name="text1">Another Text</text>',
#             ]
#         }
#         updated_svg = self.manipulator.replace_group_elements(group_replacements)
#         self.assertIn('fill="yellow"', updated_svg)
#         self.assertIn("Another Text", updated_svg)


# if __name__ == "__main__":
#     unittest.main()
