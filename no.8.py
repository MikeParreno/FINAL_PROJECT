import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_punctuation=False):
  """Generates a random password based on specified criteria.

  Args:
      length (int): Desired length of the password.
      include_uppercase (bool, optional): Include uppercase letters (default: True).
      include_lowercase (bool, optional): Include lowercase letters (default: True).
      include_digits (bool, optional): Include digits (default: True).
      include_punctuation (bool, optional): Include punctuation characters (default: False).

  Returns:
      str: The generated random password.
  """

  all_chars = ''
  if include_uppercase:
    all_chars += string.ascii_uppercase
  if include_lowercase:
    all_chars += string.ascii_lowercase
  if include_digits:
    all_chars += string.digits
  if include_punctuation:
    all_chars += string.punctuation

  if not all_chars:
    raise ValueError("At least one character set must be included.")

  password = ''.join(random.sample(all_chars, length))
  return password

# Example usage with different configurations
password1 = generate_password(12)  # 12 characters, alphanumeric
password2 = generate_password(16, include_punctuation=True)  # 16 characters, alphanumeric + punctuation
password3 = generate_password(10, include_uppercase=False)  # 10 characters, lowercase + digits

print(f"Password 1: {password1}")
print(f"Password 2: {password2}")
print(f"Password 3: {password3}")
