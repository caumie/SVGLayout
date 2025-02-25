from dataclasses import dataclass
from dataclasses import field as dc_field
from typing import Any, Callable, List, Optional, TypeVar

# フィールドの型を汎用化
T = TypeVar("T")


def field(
    *,
    default: Optional[T] = None,
    style: Optional[str] = None,
    formatter: Optional[Callable[[T], str]] = None,
    **kwargs: Any
) -> T:
    """
    拡張されたdataclassのfield関数。
    defaultやstyle、formatterをサポート。

    :param default: フィールドのデフォルト値
    :param style: CSSスタイル情報
    :param formatter: 値を整形するための関数
    :return: 型注釈付きのField
    """
    metadata = kwargs.pop("metadata", {})
    metadata.update(
        {
            "default": default,
            "style": style,
            "formatter": formatter,
        }
    )
    result = dc_field(default=default, metadata=metadata, **kwargs)
    if result is None:
        raise Exception()
    return result


@dataclass
class _Header:
    company_name: str = field(
        default="A Corp.", style="font-size:24px; font-weight:bold;"
    )
    company_address: str = field(
        default="New York.", style="font-size:12px; font-weight:bold;"
    )


@dataclass
class _Item:
    name: str = field(default="Item A")
    count: int = field()
    price: float = field(digit=2)
    total: float = field(digit=2)


@dataclass
class _Footer:
    my_company_name: str = field(
        default="XXXX Corp.", style="font-size:24px; font-weight:bold;"
    )
    my_company_address: str = field(
        default="Amazon.", style="font-size:12px; font-weight:bold;"
    )


@dataclass
class InvoiceModel:
    header: _Header
    line_items: List[_Item]
    footer: _Footer
    # template_file: str = "invoice_template.svg"
