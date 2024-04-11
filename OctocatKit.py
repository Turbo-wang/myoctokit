# -*- coding:utf8 -*-

import requests

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
        resp = requests.get(url, headers=self._headers)
        return resp.json().get("stargazers_count", -1)

        
    def get_stars_user_list(self):
        url = f"https://api.github.com/repos/{self.own}/{self.repo}/stargazers"
        page_size = 100
        stars_num = self.get_stars_number()
        page_max = stars_num // page_size + 1
        user_list = list()
        for page_index in range(0, page_max):
            parameters = {
                "per_page": 100,
                "page": page_index 
            }
            resp = requests.get(url=url, headers=self._headers, params=parameters)
            for user in resp.json():
                user_list.append(user)
        print(f"stared user amount is {stars_num}; We crawled {len(user_list)} users")
        return user_list



def main():
    get_starts_user_list()


if __name__ == "__main__":
    main()