from dataclasses import fields, is_dataclass
from typing import Any, Type

from .util import InvoiceModel


def dict_to_dataclass(cls: Type[Any], data: dict[str, Any]) -> Any:
    """
    辞書データをdataclassに再帰的に変換する。
    """
    if not is_dataclass(cls):
        raise ValueError(f"{cls} is not a dataclass")

    field_map = {field.name: field.type for field in fields(cls)}
    init_kwargs = {}

    for key, value in data.items():
        if key not in field_map:
            continue

        field_type = field_map[key]
        if is_dataclass(field_type):
            # ネストされたdataclassの処理
            init_kwargs[key] = dict_to_dataclass(field_type, value)
        elif isinstance(value, list) and get_origin(field_type) == list:
            # リスト型の処理
            item_type = get_args(field_type)[0]
            init_kwargs[key] = [
                dict_to_dataclass(item_type, item) if is_dataclass(item_type) else item
                for item in value
            ]
        else:
            # 単純型の処理
            init_kwargs[key] = value

    return cls(**init_kwargs)


data = {
    "header": {"company_name": "B Corp.", "company_address": "San Francisco."},
    "line_items": [
        {"name": "Product A", "count": 2, "price": 10.0, "total": 20.0},
        {"name": "Product B", "count": 1, "price": 15.5, "total": 15.5},
    ],
    "footer": {"my_company_name": "YYYY Corp.", "my_company_address": "Seattle."},
}

# 使用例
model = dict_to_dataclass(InvoiceModel, data)
print(model)


# h: _Header = dict(company_address="243234", company_name=21313)


# inv: InvoiceModel = dict(header=dict(company_name="adfa"))

# inv.footer.my_company_address
