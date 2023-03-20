import os

def create_package_dir():
    dir_path = os.getcwd() + "/biblioglot_package"
    os.mkdir(dir_path)

def create_json_dir():
    dir_path = os.getcwd() + "/biblioglot_package"
    json_path = f"{dir_path}/json"
    os.mkdir(json_path)

def create_audio_dir():
    dir_path = os.getcwd() + "/biblioglot_package"
    audio_path = f"{dir_path}/audio"
    os.mkdir(audio_path)

def package_dir_exists():
    dir_path = os.getcwd() + "/biblioglot_package"
    return os.path.exists(dir_path)

def json_dir_exists():
    dir_path = os.getcwd() + "/biblioglot_package"
    json_path = f"{dir_path}/json"
    return os.path.exists(json_path)

def audio_dir_exists():
    dir_path = os.getcwd() + "/biblioglot_package"
    audio_path = f"{dir_path}/audio"
    return os.path.exists(audio_path)



