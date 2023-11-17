import requests
import yaml

# Read API and Steam keys from config.yaml
def read_keys_from_yaml(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
        game_count = config.get('game_count', 10) # Default to 10 games
    return config.get('api_key'), config.get('steam_id'), game_count

# Get the list of games and playtime for the specified user
def get_top_games(api_key, steam_id, game_count):
    url = f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={api_key}&steamid={steam_id}&format=json'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        games = data['response']['games']
        # Sort the games by playtime in descending order
        sorted_games = sorted(games, key=lambda x: x['playtime_forever'], reverse=True)[:game_count]
        return sorted_games
    else:
        print("Failed to retrieve data")
        return None

# Get game name by appid
def get_game_name(app_id):
    url = f'https://store.steampowered.com/api/appdetails?appids={app_id}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data[str(app_id)]['success']:
            game_name = data[str(app_id)]['data']['name']
            return game_name
    return 'Unknown Game'

# Convert minutes to hours
def convert_to_hours(minutes):
    return minutes / 60

# Display top ten games based on playtime
def display_top_games(top_games, game_count):
    if top_games:
        print(f"Top {game_count} Games Based on Hours Played:")
        for idx, game in enumerate(top_games, start=1):
            app_id = game['appid']
            game_name = get_game_name(app_id)
            playtime_hours = convert_to_hours(game['playtime_forever'])
            print(f"{idx}. {game_name} - {playtime_hours:.2f} hours")
    else:
        print("No data available")

if __name__ == "__main__":
    api_key, steam_id, game_count = read_keys_from_yaml('config.yaml')
    top_games = get_top_games(api_key, steam_id, game_count)
    display_top_games(top_games, game_count)
