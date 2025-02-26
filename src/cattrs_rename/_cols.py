from __future__ import annotations

from cattrs_rename._gen import MetadataKey


def rename(name: str, /) -> dict[MetadataKey, str]:
    """Create a rename dictionary for metadata."""
    return {MetadataKey.RENAME: name}
