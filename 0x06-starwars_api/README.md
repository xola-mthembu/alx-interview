# 0x06. Star Wars API

This project involves interacting with the Star Wars API to fetch and display 
information about characters in a specified Star Wars movie.

## Project Requirements

- All code should be semistandard compliant.
- The script should fetch data from the Star Wars API using HTTP requests.
- Asynchronous operations should be managed using callbacks or promises.
- Command line arguments should be used to specify the Movie ID.

## Files

- `0-starwars_characters.js`: A script to fetch and print all character names 
  from a given Star Wars movie.

## Installation

To run the scripts in this project, you will need to have Node.js installed. 
Follow these instructions to install the required packages:

```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm install semistandard --global
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
