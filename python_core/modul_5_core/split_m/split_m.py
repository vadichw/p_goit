#text = "First sentence. Second sentence. Third sentence."
#sentences = text.split(".")
#print(sentences)

import re

#text = "First sentence. Second sentence! Third sentence?"
#sentences = re.split("[\.\!\?]", text)
#print(sentences)

text = "First sentence. \nSecond sentence! \nThird sentence?"
sentences = text.split('\n')
new_text = " ".join(sentences)
print(sentences)
print(new_text)

