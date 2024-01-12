# Ultra Simple Config for Python


## Installation

```bash
pip install ultra-simple-config
```

## Usage

Create a yml file with your configuration, for example:

```yaml
db:
  url: localhost
  port: 5432
  format: utf8


user:
  name: blubby
```

Then load it in your python code:

```python
from ultra_simple_config import load_config
```

Then use it on your method like that:

```python
@load_config(location="tests/example_config/db.yaml")
def test_loading(cfg: DictConfig):

    # then you can use it like this:
    print(cfg.db.url)
```