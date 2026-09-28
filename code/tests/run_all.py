"""Uruchamia wszystkie testy bez pytest:  python -m tests.run_all  (z katalogu code/)."""
import importlib
import sys
import traceback

MODULES = ["tests.test_env", "tests.test_parse", "tests.test_psychometric", "tests.test_pipeline"]

failed = total = 0
for mod_name in MODULES:
    mod = importlib.import_module(mod_name)
    for name in sorted(n for n in dir(mod) if n.startswith("test_")):
        total += 1
        try:
            getattr(mod, name)()
            print(f"OK    {mod_name}.{name}")
        except Exception:  # noqa: BLE001
            failed += 1
            print(f"BŁĄD  {mod_name}.{name}")
            traceback.print_exc()
print(f"\n{total - failed}/{total} testów zaliczonych")
sys.exit(1 if failed else 0)
