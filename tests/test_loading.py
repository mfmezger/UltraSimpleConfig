"""Simple Test."""
from omegaconf import DictConfig

from ultra_simple_config import load_config


def test_decorator():
    """Testing the decorator."""

    @load_config(location="tests/example_config/db.yaml")
    def test_loading(cfg: DictConfig):
        """Test the loading of the configuration file.

        Args:
            cfg (DictConf): The configuration object.
        """
        return cfg

    cfg = test_loading()
    assert cfg.db.url == "localhost"
    assert cfg.db.port == 5432
    assert cfg.db.format == "utf8"

    assert cfg.user.name == "blubby"
