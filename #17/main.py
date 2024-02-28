import re

# +7xxxxxxxxxx
# 7xxxxxxxxxx

numbers = '+7 499 456-45-78 +74994564578 7 (499) 456 45 78 74994564578'
template = r"[+]\d{11}|\d{11}"
correct = (re.findall(template, numbers))
print(correct)