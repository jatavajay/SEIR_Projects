# Description: This program extracts title, body text and all links from a given URL in command line argument.

import sys  # load system module to read command line argument
import urllib.request  # urllib is main module while request is submodule used to fetch webpage
from bs4 import BeautifulSoup  # used to parse HTML page and extract data

# checking command line arguments entered by user which get stored in sys.argv list by python
if len(sys.argv) != 2:  # program should accept only one URL 
    print("Please enter exactly one URL")
    sys.exit()

# print("Programme name is:", sys.argv[0])  #sys.argv always contains program name as its first element
url = sys.argv[1] 
# print("URL entered is:", url)

# checking if URL does not start with https:// then add https:// as its prefix
if not url.startswith("https://"):
    url = "https://" + url

# checking whether URL is valid and webpage can be fetched/scrap or not
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)  # server sends HTML content in binary format(bytes) which get stored in response
except Exception:
    print("You have entered Invalid URL") # will through exception if any error occur in try block
    sys.exit() # close and exit program in case of exception

# read webpage content and convert/decode binary data into normal readable text
pageContent = response.read().decode() 

# parse deocded HTML content using BeautifulSoup
soup = BeautifulSoup(pageContent, "html.parser")

# extracting and printing page title (without HTML tags)
print("Title:", soup.title.text)

# Now extracting body text of webpage (only text, no HTML tags)
bodyText=soup.body.text
print("Body:-")
print(bodyText)

# extracting all links present on the webpage
print("Outlinks:-")
allLinks=soup.find_all("a")
for link in allLinks:
    href=link.get("href")
    if href is not None: #checking if link present if yes then print and not if it contains None
        print(href)

print("Thank You! for using my program..")