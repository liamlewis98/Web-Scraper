from bs4 import BeautifulSoup
import re

with open("test_HTML2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# tag will return everything associated to 'option'
# tag ['value'] is us attempting to change the result that we get.
# We get 'Course type*' as the initial response, but we change this value to 'new value'.
tag = doc.find("option")
tag['value'] = 'new value'
# Adding attributes
tag['added'] = 'true'

#print(tag.attrs) # returns all of the attributes of the tag.
#print(tag)

# You can combine searches by doing: ...find_all(["TAG NAME"], text="text_here", value="value_here")
# E.g. tag = doc.find_all([p], text="test")

# Using RE package.
tags = doc.find_all(text = re.compile("\$.*"))
print(tags)