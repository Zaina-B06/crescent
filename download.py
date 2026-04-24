import urllib.request

url = "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzQ5NGIzMzU3NjJmNjRkMjc4ODhlODZkMzYyMDkzZTczEgsSBxDjgKGr8xQYAZIBIwoKcHJvamVjdF9pZBIVQhM3MzQxNDQ0MzkxNDgwMjU2MDI4&filename=&opi=89354086"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        with open('c:/Users/zaina/OneDrive/Desktop/dental/crescent-dental/stitch_raw.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Success")
except Exception as e:
    print(f"Error: {e}")
