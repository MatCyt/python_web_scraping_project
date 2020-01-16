from requests import get
url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)


from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))

movie_containers

first_movie = movie_containers[0]

# one by one
first_namefirst_movie.h3.a.text

first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
first_year = first_year.text

first_imdb = float(first_movie.strong.text)
first_imdb

first_mscore = first_movie.find('span', class_ = 'metascore favorable')
first_mscore = int(first_mscore.text)
print(first_mscore)

first_votes = first_movie.find('span', attrs = {'name':'nv'}) # searching through attributes
first_votes = int(first_votes['data-value']) # attributes as dictionary

# SOLUTION FOR ALL FILMS AT THE WEB PAGE
# Lists to store the scraped data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []
# Extract data from individual movie container
for container in movie_containers:
# If the movie has Metascore, then extract:
    if container.find('div', class_ = 'ratings-metascore') is not None:
# The name
    name = container.h3.a.text
    names.append(name)
# The year
    year = container.h3.find('span', class_ = 'lister-item-year').text
    years.append(year)
# The IMDB rating
    imdb = float(container.strong.text)
    imdb_ratings.append(imdb)
# The Metascore
    m_score = container.find('span', class_ = 'metascore').text
    metascores.append(int(m_score))
# The number of votes
    vote = container.find('span', attrs = {'name':'nv'})['data-value']
    votes.append(int(vote))