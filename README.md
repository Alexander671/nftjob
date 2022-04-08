
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

## .env file

For correct work you need to create .env file in ~/PROJECT_DIR/nftjob/.env
with the following content:

```
WEB3_INFURA_PROJECT_ID=<endoint infura>
ADDRESS_CONTRACT=<address contract>
ME=<your address>
ABI=<ABI of contract>
PRIVATE_KEY=<private key your address>
```

## Build Without Docker

### Git

Clone the repository
```
git clone https:github.com/Alexander671/nftjob
```

Navigate into the `nftjob` directory
```
cd nftjob
```

### Dependencies

Install, using `pip`:

```
pip install -r requirements.txt
```


### Usage
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## Build Using Docker

### Git

Clone the repository
```
git clone https:github.com/Alexander671/nftjob
```

Navigate into the `nftjob` directory
```
cd nftjob
```

### Usage

1. Build the image

`docker build .`

2. Сompiling the image with the team

`docker-compose build`

3. Run container:

`docker-compose up -d`

## Some examples

Some edge-cases examples are available on the `examples` folder. 

## Authors

* **Alexander Matveev** - *Initial work* - [Alexander671](https://github.com/Alexander671)

