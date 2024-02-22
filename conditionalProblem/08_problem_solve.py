# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
password = '123456'

if len(password) < 6:
    Strength = "weak"
elif len(password) < 10:
    Strength = "medium"
elif len(password) >=10:
    Strength = "strong"
print("your password strength is:",Strength)