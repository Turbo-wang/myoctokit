# -*- coding:utf8 -*-

import requests
from collections import OrderedDict

class OctocatKit:

    def __init__(self, access_token):
        self.access_token = access_token
        self._headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.access_token}",
            "X-GitHub-Api-Version": "2022-11-28"
        }


    def set_repo(self, repo, own):
        self.repo = repo
        self.own = own


    def get_stars_number(self):
        url = f"https://api.github.com/repos/{self.own}/{self.repo}"
        try:
            resp = requests.get(url, headers=self._headers)
            return resp.json().get("stargazers_count", -1)
        except Exception as e:
            print(e)
            return None

        
    def get_stars_user_list(self):
        url = f"https://api.github.com/repos/{self.own}/{self.repo}/stargazers"
        page_size = 100
        stars_num = self.get_stars_number()
        page_max = stars_num // page_size + 1
        users = OrderedDict()
        for page_index in range(0, page_max):
            parameters = {
                "per_page": 100,
                "page": page_index 
            }
            try:
                resp = requests.get(url=url, headers=self._headers, params=parameters)
                for user in resp.json():
                    user_name = user.get("login")
                    if user_name not in users:
                        users[user_name] = user
            except Exception as e:
                print(f"fetch page {page_index} error: ", e)
        print(f"stared user amount is {stars_num}; We crawled {len(users)} users")
        return users


    def get_user_info(self, user_login_id):
        url = f"https://api.github.com/users/{user_login_id}"
        try:
            resp = requests.get(url=url, headers=self._headers)
            return resp.json()
        except Exception as e:
            print(e)
            return None





def main():
    get_starts_user_list()


if __name__ == "__main__":
    main()