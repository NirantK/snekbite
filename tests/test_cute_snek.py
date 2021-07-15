import pytest
from importlib import metadata

def test_entry_point_grp_exists():
    eps = metadata.entry_points()
    assert 'snek_types' in list(eps)

def test_cute_entry_exists():
    eps = metadata.entry_points()
    snek_types = eps["snek_types"]
    snek_type_names = [ep.name for ep in snek_types]
    assert "cute" in snek_type_names
