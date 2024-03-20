from django.core.exceptions import ValidationError
import re

def validate_name_format(name):
    pattern = r'^[A-Z][a-z]+\s[A-Z]\.\s[A-Z][a-z]+$'
    
    if not re.match(pattern, name):
        raise ValidationError('Name must be in the format "First Middle Initial. Last"', code='invalid_name_format')
    
def validate_school_email(value):
    pattern = r'^.+@school\.com$'
    
    if not re.match(pattern, value):
        raise ValidationError('Invalid school email format. Please use an email ending with "@school.com".', code='invalid_email_format')

def validate_combination_format(value):
    pattern = r'^\d{2}-\d{2}-\d{2}$'
    
    if not re.match(pattern, value):
        raise ValidationError('Combination must be in the format "12-12-12"', code='invalid_combination_format')