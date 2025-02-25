import xml.etree.ElementTree as ET


class SVGElement:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        fill_color="#FFFFFF",
        stroke_color="#000000",
        stroke_width=1,
        data_name=None,
        data_for=None,
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill_color = fill_color
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.data_name = data_name
        self.data_for = data_for

    def to_svg(self):
        raise NotImplementedError("Subclasses should implement this method.")


class Rectangle(SVGElement):
    def to_svg(self):
        return (
            f'<rect x="{self.x}" y="{self.y}" fill="{self.fill_color}" '
            f'stroke="{self.stroke_color}" stroke-width="{self.stroke_width}" '
            f'width="{self.width}" height="{self.height}"/>'
        )


class TextField(SVGElement):
    def __init__(self, x, y, text, font_family="MS-Gothic", font_size=24):
        super().__init__(x, y, 0, 0)  # Width and height are not used for text fields
        self.text = text
        self.font_family = font_family
        self.font_size = font_size

    def to_svg(self):
        return (
            f'<text x="{self.x}" y="{self.y}" font-family="{self.font_family}" '
            f'font-size="{self.font_size}">{self.text}</text>'
        )


class ForeignObject(SVGElement):
    def __init__(self, x, y, width, height, content):
        super().__init__(x, y, width, height)
        self.content = content

    def to_svg(self):
        return (
            f'<foreignObject x="{self.x}" y="{self.y}" width="{self.width}" '
            f'height="{self.height}">{self.content}</foreignObject>'
        )


class SVGManipulator:
    def __init__(self, svg_content: str):
        if svg_content:
            self.svg_content = ET.fromstring(svg_content)
        else:
            self.svg_content = None

    def load_svg(self, svg_file: str):
        tree = ET.parse(svg_file)
        self.svg_content = tree.getroot()

    def replace_elements(self, replacements: dict):
        if self.svg_content is None:
            raise ValueError("SVG content is not loaded.")
        for name, new_content in replacements.items():
            element = self.svg_content.find(f".//*[@data-name='{name}']")
            if element is None:
                raise ValueError(f"Element with data-name '{name}' does not exist.")
            if isinstance(new_content, str):
                new_element = ET.fromstring(new_content)
                parent = self.svg_content.find(f".//*[@data-name='{name}']/..")
                if parent is not None:
                    parent.remove(element)
                    parent.append(new_element)
            elif isinstance(new_content, dict):
                for key, value in new_content.items():
                    if key in element.attrib:
                        element.set(key, value)
        return ET.tostring(self.svg_content, encoding="unicode")

    def replace_group_elements(self, group_replacements: dict):
        if self.svg_content is None:
            raise ValueError("SVG content is not loaded.")
        for group_name, elements in group_replacements.items():
            groups = self.svg_content.findall(f".//*[@data-name='{group_name}']")
            if not groups:
                continue  # グループが存在しない場合はスキップ
            for group in groups:
                for element_str in elements:
                    new_element = ET.fromstring(element_str)
                    group.append(new_element)
        return ET.tostring(self.svg_content, encoding="unicode")

    def overlay_element(self, name: str, new_element_str: str):
        if self.svg_content is None:
            raise ValueError("SVG content is not loaded.")
        element = self.svg_content.find(f".//*[@data-name='{name}']")
        if element is None:
            raise ValueError(f"Element with data-name '{name}' does not exist.")
        new_element = ET.fromstring(new_element_str)
        parent = self.svg_content.find(f".//*[@data-name='{name}']/..")
        if parent is None:
            raise ValueError(f"Parent of element '{name}' not found.")
        index = list(parent).index(element)
        parent.insert(index + 1, new_element)
        return ET.tostring(self.svg_content, encoding="unicode")
