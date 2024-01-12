from ultra_simple_config import load_config
from omegaconf import DictConf

@load_config(location="tests/example_config/config.yaml")
def test_loading(cfg: DictConf):

    assert cfg.db.url == "localhost"
    assert cfg.db.port == 5432
    assert cfg.db.format == "utf8"

    assert cfg.user.name == "blubby"

    