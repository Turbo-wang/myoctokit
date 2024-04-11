# -*- coding:utf8 -*-

import os
import argparse
from OctocatKit import OctocatKit

access_token = os.getenv["GITHUB_ACCESS_TOKEN"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=str, required=True, help="name of Github Repo")
    parser.add_argument("--own", type=str, required=True, help="name of Github Repo's owner")
    args = parser.parse_args()
    repo = args.repo
    own = args.own
    octocat_kit = OctocatKit(access_token)
    octocat_kit.set_repo(repo=repo, own=own)
    user_list = octocat_kit.get_stars_user_list()
    with open("loki_starred_user_list.txt", 'w') as fw:
        for user in user_list:
            user_name = user.get("login")
            user_email = user.get("email")
            if user_email:
                fw.write(user_name + "\t" + user_email)
                fw.write("\n")


if __name__ == "__main__":
    main()