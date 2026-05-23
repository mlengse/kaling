import os
import re

base_dir = r"c:\Users\anjan\dev\kaling\docs"
tdd_file = os.path.join(base_dir, "pendahuluan", "tdd.md")

print("Fixing TDD anchors formatting by placing them inline inside list items...")
print("-" * 75)

with open(tdd_file, "r", encoding="utf-8") as f:
    content = f.read()

# Let's use regex to find all instances where an anchor tag is on the line before a list item
# Pattern: <a id="anchor-id"></a>\n(\d+)\.\s+(.*)
# We want to replace it with: \1. <a id="anchor-id"></a> \2

pattern = r'<a id="([^"]+)"></a>\n\s*(\d+)\.\s+'
# Let's do it carefully line-by-line or by finding matches.
# Wait! Let's do a re.sub with a custom replacer or a robust regex.

# We need to handle windows newlines \r\n as well as standard newlines \n
# So let's normalize newlines first, then do the substitution, then write it back.
normalized_content = content.replace("\r\n", "\n")

# Let's define the replacement regex
# The regex matches:
# <a id="anchor-id"></a>
# 1. Title
def replacer(match):
    anchor_id = match.group(1)
    num = match.group(2)
    return f'{num}. <a id="{anchor_id}"></a> '

new_content = re.sub(r'<a id="([^"]+)"></a>\n\s*(\d+)\.\s+', replacer, normalized_content)

if new_content != normalized_content:
    with open(tdd_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully moved all TDD anchors inline!")
else:
    print("Warning: No matches found for separate line anchors.")

print("-" * 75)
