#!/usr/bin/env python
import os
import sys


def main():
    """Run administrative tasks."""

    # 1️⃣ Tell Django which settings file to use
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    try:
        # 2️⃣ Import Django command executor
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Is it installed?"
        ) from exc

    # 3️⃣ Execute command passed in terminal
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()