
# NFTJOB

A simple python backend service that interacts with the contract of the ERC-721 standard in the Ethereum blockchain.

Tested on Ubuntu 20.04 and is compatable with
Python==3.8.10
Django==2.2.12
web3==5.28.0


## Getting Started

These instructions will get you a copy of the project up and running on your local machine. There are **two** ways to run a project.

1. run without Docker
2. run with Docker 


### Dependencies

Install  if you do not have it already installed, using `pip`:

```
pip install requests
```


### Usage

Clone the repository
```
git clone https:github.com/Alexander671/nftjob
```

Navigate into the `nftjob` directory
```
cd nftjob
```

Run the script

```
python3 manage.py runserver
```

## Build Using Docker

1. Build the image

`docker build -t noisy .`


2. Create the container and run:

`docker run -it noisy --config config.json`

## Some examples

Some edge-cases examples are available on the `examples` folder. 

## Authors

* **Alexander Matveev** - *Initial work* - [1tayH](https://github.com/Alexander671)

