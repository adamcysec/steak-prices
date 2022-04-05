# steak-prices

## Synopsis
track steak prices from kroger for ribeye, sirlon, t-bone, and top loin.

## Description
I wanted to track steak prices over time to determine when steak prices are at a low. I want to buy steak at the lowest price possible.

I was able to create a developer account with [Kroger](https://developer.kroger.com/) and access their api.

## Setup: Kroger api
replace the contents of file kroger_api_key.txt with your base64 encoded kroger secret

kroger secret = base64(client_id:client_secret)

### krogerlib.py
This python script handles the kroger api code required for reading the local api key file, api authentication, and product search.

### get-steakprices.py
This python script handles the code for searching the 4 different kinds of steak and outputing the data into CSV files (one file for each steak type).

## Future plans
I plan to extend the steak tracking to other stores such as, HEB.

I will also be hosting the steak data in this repository and plan on making a report tool for alerting me to when i should buy steak. 

**update**
HEB does not have a publicly documented api and does not offer public api access. This is the same case with Sam's club. 

This project will be strictly limited to Kroger.
