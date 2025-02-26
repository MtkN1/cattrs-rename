import pytest
from attrs import define, field
from cattrs import ClassValidationError, Converter

import cattrs_rename


@define
class User:
    name: str = field(metadata=cattrs_rename.rename("userName"))


def test_configure_converter() -> None:
    """Test configured converter."""
    # Arrange
    converter = Converter()

    # Act
    cattrs_rename.configure_converter(converter)
    instance = converter.structure({"userName": "Alice"}, User)
    obj = converter.unstructure(instance)

    # Assert
    assert instance == User(name="Alice")
    assert obj == {"userName": "Alice"}


def test_invalid_usage() -> None:
    """Test invalid usage."""
    # Arrange
    converter = Converter()

    # Act
    # Assert
    cattrs_rename.configure_converter(converter)

    with pytest.raises(ClassValidationError):
        converter.structure({"name": "Alice"}, User)

    with pytest.raises(TypeError):
        User(userName="Alice")  # pyright: ignore[reportCallIssue]
