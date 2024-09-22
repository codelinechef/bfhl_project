# bfhl_app/serializers.py
import base64
import string
from rest_framework import serializers

class BFHLSerializer(serializers.Serializer):
    data = serializers.ListField()
    file_b64 = serializers.CharField(required=False, allow_blank=True)

    def validate(self, data):
        numbers = []
        alphabets = []
        lowercase_alphabets = []

        # Separate numbers and alphabets
        for item in data['data']:
            if item.isdigit():
                numbers.append(item)
            elif item.isalpha():
                alphabets.append(item)
                if item.islower():
                    lowercase_alphabets.append(item)

        # Find the highest lowercase alphabet
        highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None

        # Handle the file (Base64 decoding)
        file_b64 = data.get('file_b64', None)
        file_valid = False
        mime_type = None
        file_size_kb = 0

        if file_b64:
            try:
                decoded_file = base64.b64decode(file_b64)
                file_size_kb = len(decoded_file) / 1024  # Get size in KB
                # Assume MIME type based on file content (this could be improved)
                mime_type = "application/octet-stream"  # Default if unknown
                file_valid = True
            except Exception:
                file_valid = False

        return {
            'is_success': True,
            'user_id': 'john_doe_17091999',
            'email': 'john@xyz.com',
            'roll_number': 'ABCD123',
            'numbers': numbers,
            'alphabets': alphabets,
            'highest_lowercase_alphabet': highest_lowercase,
            'file_valid': file_valid,
            'file_mime_type': mime_type,
            'file_size_kb': file_size_kb,
        }
