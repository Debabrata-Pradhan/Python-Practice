#program for using special function in python
#map()
emails = ["  Alice@Gmail.com ", "bob@yahoo.com", "  CHARLIE@OUTLOOK.COM   "]

cleaned_emails = list(map(lambda email: email.strip().lower(), emails))

print(cleaned_emails)

#filter()
users = [
    {"name": "Alice", "type": "Free"},
    {"name": "Bob", "type": "Premium"},
    {"name": "Charlie", "type": "Premium"},
    {"name": "David", "type": "Free"}
]

premium_users = list(filter(lambda user: user["type"] == "Premium", users))

print(premium_users)

#reduce()
from functools import reduce

scores = [45, 82, 99, 64, 91]

highest_score = reduce(lambda x, y: x if x > y else y, scores)

print(highest_score)

