from __future__ import annotations

from enum import Enum, auto
from typing import TYPE_CHECKING

from attrs import fields_dict, has
from cattrs.gen import make_dict_structure_fn, make_dict_unstructure_fn, override

if TYPE_CHECKING:
    from collections.abc import Callable

    from attrs import AttrsInstance
    from cattrs import BaseConverter
    from cattrs.gen._consts import AttributeOverride


class MetadataKey(Enum):
    """Metadata key definitions for attrs fields."""

    RENAME = auto()


def make_dict_renames(cl: type[AttrsInstance], /) -> dict[str, AttributeOverride]:
    """Create a dictionary of renames for a given class."""
    return {
        x.name: override(rename=r)
        for x in fields_dict(cl).values()
        if (r := x.metadata.get(MetadataKey.RENAME))
    }


def make_structure_hook_factory(
    converter: BaseConverter, /
) -> Callable[[type[AttrsInstance]], Callable[..., object]]:
    """Create a structure hook factory that uses renames."""

    def hook(cl: type[AttrsInstance], /) -> Callable[..., object]:
        return make_dict_structure_fn(
            cl,
            converter,
            **make_dict_renames(cl),  # pyright: ignore[reportArgumentType]
        )

    return hook


def make_unstructure_hook_factory(
    converter: BaseConverter,
    /,
) -> Callable[[type[AttrsInstance]], Callable[..., object]]:
    """Create an unstructure hook factory that uses renames."""

    def hook(cl: type[AttrsInstance], /) -> Callable[..., object]:
        return make_dict_unstructure_fn(
            cl,
            converter,
            **make_dict_renames(cl),  # pyright: ignore[reportArgumentType]
        )

    return hook


def configure_converter(converter: BaseConverter) -> None:
    """Configure the converter to override renames."""
    converter.register_structure_hook_factory(
        has,
        make_structure_hook_factory(converter),
    )
    converter.register_unstructure_hook_factory(
        has,
        make_unstructure_hook_factory(converter),
    )
