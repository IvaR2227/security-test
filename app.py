import os

# 1. LEAKED SECRET: Fake AWS Access Key
AWS_ACCESS_KEY = "AKIA1234567890ABCDEF"

# 2. LEAKED SECRET: Fake Gemini / High-Entropy Token (Random string >= 20 chars)
GEMINI_KEY = "AIzaSyD-7x8Kp9demoRandomSecretToken99120"

# 3. AST OWASP VULNERABILITY: Dynamic SQL Injection
def get_user_data(cursor, user_id):
    # DANGEROUS: f-string inside database query
    cursor.execute(f"SELECT * FROM users WHERE id = '{user_id}'")

# 4. AST OWASP VULNERABILITY: Arbitrary Command Execution
def download_file(url):
    # DANGEROUS: os.system with raw concatenation
    os.system("curl -O " + url)
