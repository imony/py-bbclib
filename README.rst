py-bbclib
====

The library that defines BBc-1 transaction data structure is decoupled from [the bbc1 repository](https://github.com/beyond-blockchain/bbc1).

BBc-1 is a Python-based reference implementation of BBc-1, a trustable system of record keeping beyond blockchains. The transaction data structure definition is the most important part of BBc-1.
      
The design paper (white paper) and the analysis paper are available [here](https://beyond-blockchain.org/public/bbc1-design-paper.pdf) and [here](https://beyond-blockchain.org/public/bbc1-analysis.pdf). BBc-1 is inspired from blockchain technologies like Bitcoin, Ethereum, Hyperledger projects, and so on.
BBc-1 is a simple but reliable distributed ledger system in contrast with huge and complicated existing blockchain platforms.
The heart of BBc-1 is the transaction data structure and the relationship among transactions, which forms a graph topology.
A transaction should be signed by the players who are the stake holders of the deal. BBc-1 achieves data integrity and data transparency by the topology of transaction relationship and signatures on transactions. Simply put, BBc-1 does not have *blocks*, and therefore, requires neither mining nor native cryptocurrency.
BBc-1 can be applied to both private/enterprise use and public use. BBc-1 has a concept of *domain* for determining a region of data management. Any networking implementation (like Kademlia for P2P topology management) can be applied for each domain.
Although there are many TODOs in BBc-1, this reference implementation includes most of the concept of BBc-1 and would work in private/enterprise systems. When sophisticated P2P algorithms are ready, BBc-1 will be able to support public use cases.

For the details, please read documents in docs/ directory in [the bbc1 repository](https://github.com/beyond-blockchain/bbc1). Not only documents but slide decks (PDF) explain the design of the BBc-1 and its implementation.

API doc is ready at [readthedocs.org](https://py-bbclib.readthedocs.io/en/latest/index.html).


# Environment

* Python
    - Python 3.5.0 or later
    - virtualenv is recommended
        - ```python -mvenv venv```

* tools for macOS by Homebrew
    ```
    brew install libtool automake python3
    pip3 install virtualenv
    ```

* tools for Linux (Ubuntu 16.04 LTS)
    ```
    sudo apt-get update
    sudo apt-get install -y git tzdata openssh-server python3 python3-dev python3-pip python3-venv libffi-dev net-tools autoconf automake libtool libssl-dev make
    ```

# Install

### install module using pip

    python -mvenv venv
    source venv/bin/activate
    pip install -r py-bbclib


### build from github repository (this repository)
This project needs an external library, [libbbcsig](https://github.com/beyond-blockchain/libbbcsig), for sign/verify of transaction data. This repository includes setup script to build the external library.

    git clone https://github.com/beyond-blockchain/py-bbclib
    cd py-bbclib
    bash prepare.sh

You fill find a dynamic link library (libbbcsig.so or libbbcsig.dylib) in bbc1/libs/ directory.

 
