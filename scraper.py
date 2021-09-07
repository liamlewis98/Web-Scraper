# installed BeautifulSoup4 and requests via PIP.
from bs4 import BeautifulSoup

# Opening up my HTML file under 'f'
with open("test_HTML.html", "r",) as f:
    doc = BeautifulSoup(f, "html.parser")

# Returns the raw HTML. (Prettify just includes the indentation of the code.)
#print(doc.prettify())

# To retrieve a specific tag you add the tag after the . e.g...
tag = doc.h1

#print(tag) # Result = <h1 style="align-content: center;padding-left: 20%;padding-right: 20%;size: 100%;"> Hello World! </h1>
#print(tag.string) # Returns =  Hello World! 

# Having multiple types of the same 'a', 'p', 'h1' tags... you can use:
# all_tags = doc.find_all("a") # This will return all the instances of the <a> tag. If you include a [0] you will find the first instance of this tag. and so on...