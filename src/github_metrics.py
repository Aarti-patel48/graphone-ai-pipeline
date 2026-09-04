
import requests

def get_repo_info(repo_url):

    if not repo_url or "github.com" not in repo_url:
        return None

    parts = repo_url.rstrip("/").split("/")
    owner = parts[-2]
    repo = parts[-1]

    api_url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        return {
            "stars": data["stargazers_count"],
            "forks": data["forks_count"],
            "language": data["language"]
        }

    return None


# Test
if __name__ == "__main__":

    repo = "https://github.com/huggingface/transformers"

    info = get_repo_info(repo)

    print(info)