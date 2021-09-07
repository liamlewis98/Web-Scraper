# Reminder, don't use the filename 'requests' when trying to import a module named 'requests'...

from bs4 import BeautifulSoup
import requests
# This site lets you access everything needed to webscrape.
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

result = requests.get(url)

# Using BS4

doc = BeautifulSoup(result.text, "html.parser")

#print(doc.prettify)

# Finding the price by searching the entire result for a '$'.
# Printing individually you get - everything that includes a '$', but returns a list of 2 items like so: ['$', '$']
# the parent is the parental tag which wraps the first '$' location. Isolating the tag surrounding the text (this case it's strong) we can print it out. 
# Alternatively, once we have the parent, we can just print the parent result.text.
gpu_price = doc.find_all(text="$")
gpu_price_parent = gpu_price[0].parent
strong = gpu_price_parent.find("strong")
print(strong.string)