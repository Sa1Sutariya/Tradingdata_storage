# Trading Data Storage and Stock Market Web Scraping

This project provides a solution for storing and retrieving historical stock market data, as well as a web scraping tool for gathering the data in the first place.

Getting Started

Prerequisites

Python 3.x

pip

MongoDB (for storing the data)

Installation

Clone the repository

Copy code

git clone https://github.com/[username]/tradingdata-storage-stockmarket-webscraping.git 

Install the requirements

Copy code

pip install -r requirements.txt 

Start MongoDB

Copy code

mongod 

Run the script to gather and store data

Copy code

python gather_data.py 

Usage

The script gather_data.py can be used to gather data for specific stock symbols and store it in the MongoDB database. The script takes the following arguments:

-s or --symbols: a comma-separated list of stock symbols to gather data for

-d or --days: the number of days of historical data to gather (default is 30)

Example:

Copy code

python gather_data.py -s "AAPL,GOOG,MSFT" -d 90 

The data can then be retrieved and used for further analysis or visualization.

