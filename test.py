import re

pattern = r"!T!\s*((.*?)\n(.*?)(?=!T!))"
flags = re.MULTILINE | re.DOTALL

with open("roads.txt", "r") as f:
    text = f.read()

matches = re.findall(pattern, text, flags)
results = {}

for match in matches:
    key = match[1]
    value = match[2].strip()
    results[key] = value

print(results)