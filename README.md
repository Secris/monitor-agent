# monitor-agent
Agent for monitoring some basic items on a system.

## Usage
The process for using this as follows
1. Install python3 and pip
2. pip install psutils uptime
3. Run python3 agent.py

## Dev configuration
1. Install python3
2. Install pipenv
3. Run `pipenv install`
4. Run `pipenv shell` 
5. While in the pipenv run `python agent.py`

## Notes
If you are running in WSL2 on Windows it will report the usage for the WSL container instead of the total system usage.