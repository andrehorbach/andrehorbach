import random
import json
import requests
import os

# Category List for Quotes
api_url = 'https://api.api-ninjas.com/v1/facts?limit=1'
# Enter your API Key Here
response = requests.get(api_url, headers=
						{'X-Api-Key': 'XXXXXXXXXXXXXXXXXX'})

if response.status_code == requests.codes.ok:
	quote = response.text
	mainQuote = quote
else:
	print("Error:", response.status_code, response.text)


# Reading the readme file
with open("README.md", mode="r", encoding="utf8") as f:
	readmeText = f.read()

# Finding the tag where the quote is to be replaced
openingTag = "<h4 quote"
closingTag = "</h4 quote"

startIndex = readmeText.index(openingTag)
endIndex = readmeText.index(closingTag)

quoteMarkdown = "<h4 quote align='center'>" + mainQuote + "." + "</h4 quote>"

content = readmeText[startIndex +
					len(openingTag): endIndex]
newContent = (
	readmeText[:startIndex]
	+ quoteMarkdown
	+ readmeText[endIndex + len(closingTag) + 1:]
)

# Writing new Quote into readme file
readme_file = open("README.md",
				mode="w", encoding="utf8")
readme_file.write(newContent)
