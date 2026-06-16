import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

try:
    import lib.generate_log as _generate_log
except ImportError:
    _generate_log = None

if _generate_log is not None:
    sys.modules.setdefault("generate_log", _generate_log)
