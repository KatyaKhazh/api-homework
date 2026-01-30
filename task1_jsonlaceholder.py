import requests

def main():

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    posts = response.json()
    print("Первые 5 постов:\n")
    for post in posts[:5]:
        title = post.get("title", "")
        body = post.get("body", "")
        print("=" * 40)
        print(f"ID: {post.get('id')}")
        print(f"Title: {title}")
        print("Body:")
        print(body)
        print()
main()