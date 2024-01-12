"""Simple Test."""
from omegaconf import DictConf

from ultra_simple_config import load_config


@load_config(location="tests/example_config/config.yaml")
def test_loading(cfg: DictConf):
    """Test the loading of the configuration file.

    Args:
        cfg (DictConf): The configuration object.
    """
    assert cfg.db.url == "localhost"
    assert cfg.db.port == 5432
    assert cfg.db.format == "utf8"

    assert cfg.user.name == "blubby"
