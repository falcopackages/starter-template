import multiprocessing
import platform

__version__ = "0.1.0"

if platform.system() == "Darwin":
    multiprocessing.set_start_method("fork", force=True)
