import json
import os


def get_user_rosters(user_id): 
    rosters = []
    roster_dir = f"data/users/{user_id}/rosters"
    # for root, dirs, files in os.walk(roster_dir):
    #     for dir in dirs:
    #         dir_path = os.path.join(root, dir)
    for file in os.listdir(roster_dir):
        if file.endswith(".json"):
            file_path = os.path.join(roster_dir, file)
            try:
                with open(file_path, 'r') as json_file:
                    # Read and append the content of the JSON file to the result list
                    content = json.load(json_file)
                    rosters.append(content)
            except (json.JSONDecodeError, FileNotFoundError) as e:
                print(f"Error reading file {file_path}: {e}")
    return rosters