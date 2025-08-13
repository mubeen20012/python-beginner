"""import re
def is_valid(ip):
    if not re.fullmatch(r'\d+\.\d+\.\d+\.\d+',ip):
        return False
    parts=ip.split('.')
    if len(parts) !=4:
        return False
    for p in parts:
        if len(p) >1 and p[0]=='0':
            return False
        num=int(p)
        if num <0 or num >255:
            return False
    return True
test_cases = ["192.168.0.1", "300.10.10.10", "192.168.1", "abc.def.ghi.jkl", "01.2.3.4"]
for t in test_cases:
    print(t,is_valid(t))"""
"""import re
url="https://youtu.be/xvFZjo5PgG0"
pattern=r'youtu\.be/([\w-]{11}'
match=re.search(pattern,url)
if match:
    print("Video ID:",match.group(1))"""
import re

url = "https://youtu.be/xvFZjo5PgG0"

# pattern: youtu.be/ then 11 characters
pattern = r'youtu\.be/([\w-]{11})'

match = re.search(pattern, url)
if match:
    print("Video ID:", match.group(1))
