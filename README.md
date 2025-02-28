# cattrs-rename

A shorthand syntax for [*cattrs rename overrides*](https://catt.rs/en/stable/customizing.html#rename).

It is important to...
1. `cattrs_rename.rename` generates metadata for `attrs.field`.
2. `cattrs_rename.configure_converter` configures `cattrs.Converter`.

```python
from attrs import define, field
from cattrs import Converter

import cattrs_rename


@define
class User:
    name: str = field(metadata=cattrs_rename.rename("userName"))


converter = Converter()
cattrs_rename.configure_converter(converter)
```

Things just got easier 🪄

It is brought to you by *cattrs rename overrides* ...

```python
>>> instance = converter.structure({"userName": "Alice"}, User)
>>> instance
User(name='Alice')

>>> converter.unstructure(instance)
{'userName': 'Alice'}

>>> User(name="Alice")
User(name='Alice')
```

Ambiguity is not allowed ...

```python
>>> User(userName="Alice")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    User(userName="Alice")
    ~~~~^^^^^^^^^^^^^^^^^^
TypeError: User.__init__() got an unexpected keyword argument 'userName'

>>> converter.structure({"name": "Alice"}, User)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    res['name'] = __c_structure_name(o['userName'])
                                     ~^^^^^^^^^^^^
KeyError: 'userName'
```
