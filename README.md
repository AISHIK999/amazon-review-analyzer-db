# Sentimental review database for Amazon Products  
  
 - **Authors:** Aishik Mukherjee, Subhrajyoti Chakraborty
 -   **Language and tools:** Python, Bash, SQL, Docker, MariaDB
- **Date:** 18/11/23
- **Credits: [officialpm](https://github.com/officialpm/scrape-amazon)** for the scrape-amazon library
## Description
"Sentimental review database for Amazon Products" is an attempt to create a database to scrape and store reviews from Amazon after performing a sentimental analysis on them and appending a score for each of the reviews, based on it's negativity or positivity. The functioning of each of the scripts have been explained below as per their usage:
```.env```
This file contains all the necessary environment variables to be used in our code. They contain the product identification number and the country specific domain for each product.

```docker-compose.yml```
The docker-compose file to fetch docker images of mariadb - our database management system and adminer - out frontend GUI to manage the database graphically.

```fetch_reviews.py```
This file contains the code to scrape the reviews from the Amazon product page. The reviews are then stored in a temporary directory in the reviews.csv file.

```clean_reviews.py```
This file contains the code to cleanup the csv file to remove all unnecessary or redundant information like the rating in description column, review url etc.
The csv file gets overwritten after this operation.

```sentiment_analyzer.py```
This file contains the code to perform sentiment analysis upon the review description using nltk library. The description are broken down into tokens and analysis is done based on those tokens. A score is generated for each review. More closer to 1, the score indicates a positive review, more towards -1, the score indicates an overall negative review.

```append_to_database.py```
This file contains the code to append the csv file to our database. The database hosted through the docker container appends the contents from the csv file onto itself. This can be checked through the docker shell itself or, through the adminer interface at [localhost](http://localhost:8080/).

## Execution:
* Clone the repository
```bash
git clone https://github.com/AISHIK999/amazon-review-analyzer-db.git
```
* Change directory to the repository
```bash
cd amazon-review-analyzer-db
```
* Run the docker-compose file to fetch the docker images
```bash
docker-compose up -d --build
```
* Run the bash script to execute the python scripts
```bash
bash app.sh
```

## TODO:
* The scraping library is capable of fetching data only from the first review page. Need to configure it to be able to scrape reviews across multiple pages.
* The database seems to append only the first entry of the csv file instead of all of them. Find a way to fix this issue. Most probably generated due to some misconfiguration or some erroneous SQL query. 

## UML Diagram:
```mermaid
graph LR
A[Amazon webpage] --reviews--> B(reviews.csv)
B --cleanup--> C(cleaned reviews)
C --sentiment analysis--> D(scored reviews)
D --> E[Database]
```