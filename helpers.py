import secrets
import string


from flask import render_template

def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_symbols=True, include_numbers=True):
    alphabet = ''
    if include_uppercase:
        alphabet += string.ascii_uppercase
    if include_lowercase:
        alphabet += string.ascii_lowercase
    if include_symbols:
        alphabet += string.punctuation
    if include_numbers:
        alphabet += string.digits 
    
    if not alphabet:
        raise ValueError("At least one character set must be included.")
    
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

