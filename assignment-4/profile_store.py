import json

PROFILE_FILE = "profiles/user.json"


def get_profile():
    with open(PROFILE_FILE, "r") as f:
        return json.load(f)


def get_name():
    return get_profile()["name"]


def get_email():
    return get_profile()["email"]


def get_resume():
    return get_profile()["resume_path"]