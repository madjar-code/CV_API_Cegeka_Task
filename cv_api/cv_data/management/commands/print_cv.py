from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from cv_data.data import CV_DATA


class Command(BaseCommand):
    help = 'Displays CV data'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            'section',
            type=str,
            help='Section of the CV to display'
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        section = options['section']

        if section in CV_DATA:
            self.stdout.write(str(CV_DATA[section]))
        else:
            self.stdout.write(
                self.style.ERROR(
                    f"Section '{section}' not found in CV data"
                )
            )
