#!/usr/bin/env python3
"""
Парсит результаты pytest (test_results.json) и отправляет сводку в webhook.

Запуск: python utils/parse_and_send_results.py

Переменные окружения:
    WEBHOOK_URL        URL для отправки отчёта (например, Telegram-бот)
    GITHUB_USERNAME    Имя пользователя, запустившего CI
    GITHUB_REPO        Репозиторий (owner/repo)
"""

import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

try:
    import requests
except ImportError:
    requests = None

RESULTS_FILE = "test_results.json"


def load_results(path=RESULTS_FILE):
    if not os.path.exists(path):
        print(f"❌ Файл {path} не найден. Тесты не запускались?")
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def format_message(results):
    summary = results.get("summary", {})
    total = summary.get("total", 0)
    passed = summary.get("passed", 0)
    failed = summary.get("failed", 0)
    errors = summary.get("errors", 0)
    skipped = summary.get("skipped", 0)

    repo = os.environ.get("GITHUB_REPO", "python_basic_course")
    username = os.environ.get("GITHUB_USERNAME", "student")

    status = (
        "✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ"
        if failed == 0 and errors == 0
        else "❌ ЕСТЬ ПРОВАЛЫ"
    )

    lines = [
        f"{status}",
        f"Репозиторий: {repo}",
        f"Студент: {username}",
        f"Всего: {total} | Прошло: {passed} | Упало: {failed}"
        f" | Ошибок: {errors} | Пропущено: {skipped}",
    ]

    failed_tests = [
        test.get("nodeid", "?")
        for test in results.get("tests", [])
        if test.get("outcome") in ("failed", "error")
    ]
    if failed_tests:
        lines.append("Упавшие тесты:")
        lines.extend(f"- {nodeid}" for nodeid in failed_tests[:10])

    return "\n".join(lines)


def send_message(url, message):
    if requests is None:
        print(
            "❌ Библиотека requests не установлена. Установите: pip install requests"
        )
        return False
    try:
        response = requests.post(url, json={"text": message}, timeout=15)
        response.raise_for_status()
        print("✅ Отчёт отправлен в webhook")
        return True
    except Exception as e:
        print(f"❌ Не удалось отправить отчёт: {e}")
        return False


def main():
    results = load_results()
    if results is None:
        return 1

    message = format_message(results)
    print(message)
    print("-" * 40)

    webhook_url = os.environ.get("WEBHOOK_URL", "").strip()
    if not webhook_url:
        print("ℹ️ WEBHOOK_URL не задан — отчёт не отправлен (это не ошибка).")
        return 0

    return 0 if send_message(webhook_url, message) else 1


if __name__ == "__main__":
    sys.exit(main())
