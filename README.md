# historic-withdrawals-key-finder

An endpoint to query historic-withdrawals json data

## Run

Requirements
- python3
- python3-venv

```
python3 -m venv venv
source ./venv/bin/activate
python -m pip install -r pip.requirements
DATA_FILE=./ovm1_withdrawals_111521-mainnet.json flask run
```