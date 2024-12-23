:description: Common issues and solutions that you may encounter with a project generated with falco.

Known issues
============

Permission denied on Tailwind CLI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you encounter an error similar to the one below when trying to run the server:

.. code-block:: bash

    08:12:38 tailwind | PermissionError: [Errno 13] Permission denied:
    08:12:38 tailwind | '/home/tobi/.local/bin/tailwindcss-linux-x64-3.4.10'

The simplest solution is to delete the file and re-run the server. The file will be re-downloaded, and the error should be resolved.

pre-commit python version
^^^^^^^^^^^^^^^^^^^^^^^^^

If you encounter the following error:

.. code-block:: shell

   RuntimeError: failed to find interpreter for Builtin discover of python_spec='python3.11'

You need to update the section below (located at the beginning of the ``.pre-commit-config.yaml`` file) to match the Python version in your virtual environment:

.. code-block:: yaml

   default_language_version:
      python: python3.11 # TODO: Change this to match your virtual environment's Python version
