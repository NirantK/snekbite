import os
import sys

import pytest
import catalogue

def test_entry_points():
    ep_string = """[snek_types]
     cute = cute_snek:cute_snek"""
    ep = catalogue.importlib_metadata.EntryPoint._from_text(ep_string)
    catalogue.AVAILABLE_ENTRY_POINTS["snek_types"] = ep
    # test empty registry
    assert catalogue.REGISTRY == {}
    # test registry with entry point
    test_registry = catalogue.create("snek", "types", entry_points=True)
    entry_points = test_registry.get_entry_points()
    assert "cute" in entry_points
    assert type(entry_points) == type({})


# def test_cute_entry_point():
#     eps = metadata.entry_points()
#     snek_types = list(eps["snek_types"])
#     fresh_ep: metadata.EntryPoint = metadata.EntryPoint._from_text(
#         """
#     """
#     )
#     snek_types.extend(fresh_ep)
#     # snek_types.append(EntryPoint(name="cute", value="cute_snek", group="snek_types"))
#     snek_type_names = [ep.name for ep in snek_types]
#     assert "cute" in snek_type_names

#     # Relative Path to the cute_snek directory
#     cwd = os.getcwd()
#     egg_pth = os.path.join(cwd, "cute_snek")
#     sys.path.append(egg_pth)
#     # The load will fail if the package is not found
#     for ep in snek_types:
#         ep.load()


# def test_load():
#     eps = metadata.entry_points()
#     snek_types = list(eps["snek_types"])

#     fresh_ep: metadata.EntryPoint = metadata.EntryPoint._from_text(
#         """[snek_types]
#     cute = cute_snek:cute_snek
#     """
#     )
#     snek_types.extend(fresh_ep)
