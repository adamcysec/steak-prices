# steak-prices

## Synopsis
track steak prices from kroger for ribeye, sirlon, t-bone, and top loin.

## Description
I wanted to track steak prices over time to determine when steak prices are at a low. I want to buy steak at the lowest price possible.

I was able to create a developer account with [Kroger](https://developer.kroger.com/) and access their api.

## krogerlib.py
This python script handles the kroger api code required for reading the local api key file, api authentication, and product search.

## get-steakprices.py
This python script handles the code for search the 4 different kinds of steak and outputing the data into CSV files (one file for each steak type).
