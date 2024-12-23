:description: Virtualenv and dependencies management with a project generated with falco.

Python Environment
==================

This is mainly handled using `uv <https://docs.astral.sh/uv/>`_ and the ``pyproject.toml`` file.

The pyproject.toml File
-----------------------

The ``pyproject.toml`` file is a Python standard introduced to unify and simplify Python project packaging and configurations. It was introduced by `PEP 518 <https://www.python.org/dev/peps/pep-0518/>`_ and `PEP 621 <https://www.python.org/dev/peps/pep-0621/>`_.
For more details, check out the `complete specifications <https://packaging.python.org/en/latest/specifications/pyproject-toml/#pyproject-toml-spec>`_.
Many tools in the Python ecosystem, including hatch, support it, and it seems that this is what the Python ecosystem has settled on for the future.

uv
--
