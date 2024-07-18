from io import StringIO
from django.test import TestCase
from django.core.management import call_command


class PrintCVCommandTest(TestCase):
    def test_print_personal_section(self):
        out = StringIO()
        call_command('print_cv', 'personal', stdout=out)
        self.assertIn('name', out.getvalue())
        self.assertIn('email', out.getvalue())
        self.assertIn('phone', out.getvalue())

    def test_print_experience_section(self):
        out = StringIO()
        call_command('print_cv', 'experience', stdout=out)
        self.assertIn('position', out.getvalue())
        self.assertIn('company', out.getvalue())
        self.assertIn('start_date', out.getvalue())
        self.assertIn('end_date', out.getvalue())

    def test_print_education_section(self):
        out = StringIO()
        call_command('print_cv', 'education', stdout=out)
        self.assertIn('degree', out.getvalue())
        self.assertIn('institution', out.getvalue())
        self.assertIn('start_date', out.getvalue())
        self.assertIn('end_date', out.getvalue())

    def test_print_nonexistent_section(self):
        out = StringIO()
        call_command('print_cv', 'hobbies', stdout=out)
        self.assertIn("Section 'hobbies' not found in CV data", out.getvalue())
