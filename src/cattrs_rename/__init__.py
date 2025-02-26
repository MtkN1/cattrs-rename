"""A shorthand syntax for cattrs rename overrides."""

__all__ = [
    "MetadataKey",
    "configure_converter",
    "make_dict_renames",
    "make_structure_hook_factory",
    "make_unstructure_hook_factory",
    "rename",
]

from cattrs_rename._cols import rename
from cattrs_rename._gen import (
    MetadataKey,
    configure_converter,
    make_dict_renames,
    make_structure_hook_factory,
    make_unstructure_hook_factory,
)
