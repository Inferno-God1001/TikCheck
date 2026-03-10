import requests
import re


# exemple: t = tiktok.function.search("username")
# print(t)
# 
# terminal result: found
# ===============================================
#
# exemple: t = tiktok.function.followers("username")
# print(t)
# 
# terminal result: 1000
# ===============================================
#
# exemple: t = tiktok.function.status("username")
#
# terminal result: id: 18273 Username: username DisplayName: username123 Stats: found Followers: 1000 Following: 326 Likes: 50000 Videos: 53  Bio: hiiii! i love u!
#
# or
#
# exemple: t = tiktok.function.status("username", organized=True)
#
# terminal result: id: 18273
#                  Username: username 
#                  DisplayName: username123 
#                  Stats: found 
#                  Followers: 1000 
#                  Following: 326 
#                  Likes: 50000 
#                  Videos: 53  
#                  Bio: hiiii! i love u!
#
#






empty_username = '<error>: The field cannot be left empty. Solution: site.function("JohnDoe")'
dev_error = "<dev>: Dev error."


def check_by_html(url=None, keyword=None):

    data_variables = [url, keyword]
    keyword = keyword.lower()

    if data_variables != None:
        try:
            process = requests.get(url)
            html = process.text.lower()

            if process.status_code == 200:
                try:
                    final = "not found"
                    
                    if keyword in html:
                        final = "found"
                    else:
                        final = final
                    return f"{final}"       
                     
                except Exception as exc:
                    return exc
                
        except Exception as exc:
            return exc        
            
    else:
        return dev_error


class function():
    def search(username):
        if username != "":
            order = check_by_html(url=f"https://tiktok.com/@{username}", keyword='"statusCode":0')
            return order
        else:
            return empty_username

    def followers(username):        
        if username != "":
            order = check_by_html(url=f"https://tiktok.com/@{username}", keyword='"statusCode":0')
            if order == "found":
                process = requests.get(f"https://tiktok.com/@{username}")
                html = process.text.lower()
                
                followers = re.search(r'"followercount":(\d+)', html)
                if followers:
                    followers = followers.group(1)
                else:
                    followers = None    
                return followers


                
    def following(username):
        if username != "":
            order = check_by_html(url=f"https://tiktok.com/@{username}", keyword='"statusCode":0')
            if order == "found":
                process = requests.get(f"https://tiktok.com/@{username}")
                html = process.text.lower()
                
                followers = re.search(r'"followingcount":(\d+)', html)
                if followers:
                    followers = followers.group(1)
                else:
                    followers = None    
                return followers


                
    def likes(username):
        if username != "":
            order = check_by_html(url=f"https://tiktok.com/@{username}", keyword='"statusCode":0')
            if order == "found":
                process = requests.get(f"https://tiktok.com/@{username}")
                html = process.text.lower()
                
                followers = re.search(r'"heartcount":(\d+)', html)
                if followers:
                    followers = followers.group(1)
                else:
                    followers = None    
                return followers


                
    def videos(username):
        if username != "":
            order = check_by_html(url=f"https://tiktok.com/@{username}", keyword='"statusCode":0')
            if order == "found":
                process = requests.get(f"https://tiktok.com/@{username}")
                html = process.text.lower()
                
                followers = re.search(r'"videocount":(\d+)', html)
                if followers:
                    followers = followers.group(1)
                else:
                    followers = None    
                return followers


    def id(username):
        if username != "":
            order = check_by_html(url=f"https://tiktok.com/@{username}", keyword='"statusCode":0')
            if order == "found":
                process = requests.get(f"https://tiktok.com/@{username}")
                html = process.text.lower()
                
                followers = re.search(r'"id":"(.*?)"', html)
                if followers:
                    followers = followers.group(1)
                else:
                    followers = None    
                return followers


                
    def user_name(username):
        if username != "":
            order = check_by_html(url=f"https://tiktok.com/@{username}", keyword='"statusCode":0')
            if order == "found":
                process = requests.get(f"https://tiktok.com/@{username}")
                html = process.text.lower()
                
                followers = re.search(r'"uniqueid":"(.*?)"', html)
                if followers:
                    followers = followers.group(1)
                else:
                    followers = None    
                return followers


                
    def display_name(username):
        if username != "":
            order = check_by_html(url=f"https://tiktok.com/@{username}", keyword='"statusCode":0')
            if order == "found":
                process = requests.get(f"https://tiktok.com/@{username}")
                html = process.text.lower()
                
                followers = re.search(r'"nickname":"(.*?)"', html)
                if followers:
                    followers = followers.group(1)
                else:
                    followers = None    
                return followers


                
    def bio(username):
        if username != "":
            order = check_by_html(url=f"https://tiktok.com/@{username}", keyword='"statusCode":0')
            if order == "found":
                process = requests.get(f"https://tiktok.com/@{username}")
                html = process.text.lower()
                
                followers = re.search(r'"signature":"([^"]*)"])"', html)
                if followers:
                    followers = followers.group(1)
                else:
                    followers = None    
                return followers


                
    def status(username, organized=False):
        videos_r = function.videos(username)
        heart_r = function.likes(username)
        following_r = function.following(username)
        followers_r = function.followers(username)
        search_r = function.search(username)
        
        bio_r = function.bio(username)
        display_r = function.display_name(username)
        username_r = function.user_name(username)
        id_r = function.id(username)

        qu = " "
        
        if organized == True:
            qu = "\n"
        else:
            qu = qu    
        return f"id: {id_r}{qu}Username: {username_r}{qu}DisplayName: {display_r}{qu}Stats: {search_r}{qu}Followers: {followers_r}{qu}Following: {following_r}{qu}Likes: {heart_r}{qu}Videos: {videos_r}{qu}Bio: {bio_r}"
