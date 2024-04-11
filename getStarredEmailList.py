# -*- coding:utf8 -*-

import os
from tqdm import tqdm
import argparse
from OctocatKit import OctocatKit

access_token = os.getenv("GITHUB_ACCESS_TOKEN")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=str, required=True, help="name of Github Repo")
    parser.add_argument("--own", type=str, required=True, help="name of Github Repo's owner")
    args = parser.parse_args()
    repo = args.repo
    own = args.own
    octocat_kit = OctocatKit(access_token)
    octocat_kit.set_repo(repo=repo, own=own)
    users = octocat_kit.get_stars_user_list()
    error_fw = open("get_failed_user.txt", 'w')
    with open("loki_starred_user_list.txt", 'w') as fw:
        for user_name, user in tqdm(users.items()):
            user_name = user.get("login")
            user_info = octocat_kit.get_user_info(user_name)
            if user_info:
                user_email = user_info.get("email")
                if user_email:
                    fw.write(user_name + "\t" + user_email)
                    fw.write("\n")
            else:
                error_fw.write(user_name)
                error_fw.write("\n")
    error_fw.close()
            


if __name__ == "__main__":
    main()
