#!/usr/bin/env python3
"""
Печатает сводку по задачам из результатов pytest (test_results.json).

Запуск: python utils/summarize_results.py

Группирует тесты по файлу задания (test_taskN_*.py) и показывает,
какая задача решена верно, а какая нет:
    ✅ 04_paradigms/task1_analyze_grades.py — 4/4
    ❌ 04_paradigms/task3_park_analysis.py — 2/5
"""

import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RESULTS_FILE = "test_results.json"


def load_results(path=RESULTS_FILE):
    if not os.path.exists(path):
        print(f"❌ Файл {path} не найден. Тесты не запускались?")
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def task_key(nodeid):
    """Из nodeid (tests/test_04_paradigms/test_task1_x.py::Class::test) -> (модуль, задача)."""
    test_path = nodeid.split("::")[0]
    parts = test_path.replace("\\", "/").split("/")
    test_suite = parts[-2] if len(parts) >= 2 else ""
    test_file = parts[-1]
    if not test_file.startswith("test_"):
        return None
    module_dir = test_suite[len("test_"):] if test_suite.startswith("test_") else test_suite
    task_file = test_file[len("test_"):]
    return module_dir, task_file


def summarize(results):
    groups = {}
    for test in results.get("tests", []):
        key = task_key(test.get("nodeid", ""))
        if key is None:
            continue
        outcome = test.get("outcome", "unknown")
        group = groups.setdefault(key, {"total": 0, "passed": 0, "failed": 0, "skipped": 0})
        group["total"] += 1
        group[outcome if outcome in ("passed", "failed", "skipped") else "failed"] += 1

    if not groups:
        print("ℹ️ Нет результатов по задачам.")
        return

    print("=" * 60)
    print("📋 Сводка по задачам")
    print("=" * 60)

    solved = 0
    for (module_dir, task_file), stats in sorted(groups.items()):
        ok = stats["failed"] == 0
        if ok:
            solved += 1
        mark = "✅" if ok else "❌"
        print(
            f"{mark} {module_dir}/{task_file} — "
            f"{stats['passed']}/{stats['total']}"
        )

    print("-" * 60)
    print(f"Решено задач: {solved} из {len(groups)}")

    fail_cases = [
        test["nodeid"] for test in results.get("tests", [])
        if test.get("outcome") in ("failed", "error")
    ]
    if fail_cases:
        print("\nУпавшие тесты:")
        for nodeid in fail_cases:
            print(f"  - {nodeid}")


def main():
    results = load_results()
    if results is None:
        return 0
    summarize(results)
    return 0


if __name__ == "__main__":
    sys.exit(main())