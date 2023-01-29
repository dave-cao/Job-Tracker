# Will change to notes.md later on

## Brainstorming ideas for a webscraper project


1. Scraping novels from websites
2. Job listings across different websites


*To see if a website allows webscraping, append `/robots.txt` to end of url*


### Web scraping technology
- Beautiful Soup


Some Useful BS4 commands:

1. Get all the links in of a document
```python
links = soup.find_all("a") # gets all the a tags
for link in links:
    print(link.get("href"))
```
2. Grabbing text from a page
```python
soup.get_text()
```

Different parsers:
- Beautiful soup contains multiple different parsers

1. HTML Parser: `BeautifulSoup(markup, "html.parser")`
2. XML Parser: `BeautifulSoup(markup, "lxml-xml")`
    - Must `pip install lxml` for XML parser

    
### Basic Usage / Plan

1. Grab a website / websites with requests
2. Convert requests into text and parse with Beautiful Soup



### Ideas
1. Scraping job postings based on a search query
 - Place the job postings in an easy to read format or db, then have the ability to 
    "X" / complete these job postings like the todo list

2. Consolidate all books and audiobooks based on a search term
 - Web scrape torrent hrefs / display it on website
 
### Start

Decided to do a web scraping project on audiobook (for now)

- First I have to get the proper search term for the search string
    - I'm using .format for this
    
- I want to now get all the links and have the ones that say "percy jackson" at the top
    - getting links: soup.find_all("a")


