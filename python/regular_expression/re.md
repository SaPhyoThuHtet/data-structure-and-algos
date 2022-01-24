Re Practice from Hacker Rank
# Note ရေးဖို့ မပျင်းပါနဲ့


1. re.search()
The re.search() expression scans through a string looking for the first location where the regex pattern produces a match.
Regex pattern နဲ့ တူတဲ့ ပထမဆုံး Location ကိုရှာ။
It either returns a MatchObject instance or returns None if no position in the string matches the pattern.
တွေ့ရင် MatchObject ကို ပြန်ပေးပြီး မတွေ့ရင်တော့ None ကို ပြန်ပေးပါတယ်။

import re
print bool(re.search(r"ly","similarly"))
>>True
