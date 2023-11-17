# Top 10 Steam Games by Hours Played

It started as a conversation around the threshhold to purchasing a game. Where a successful purchase was suggested as $1 per hour of fun. The next metric was $1 per 10 hours of play time. A strong implication can be inferred that a $60 AAA title would have to produce 600 hours of play! 😲

## Getting Started

Setup a virtual environment.

```console
python -m venv .venv
```

Install required Python modules.

```console
pip install -r requirements.txt
```

Create a file named `config.yaml`. Then add your Steam API key and Steam ID to the `config.yaml` file. E.g.

```yaml
api_key: YOUR_API_KEY
steam_id: YOUR_STEAM_ID
```

Run the script.

```console
python top_games.py
```
