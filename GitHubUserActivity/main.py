import requests
import typer
import json
from typing_extensions import Annotated


messages = {
    "PushEvent": "Pushed to",
    "IssueCommentEvent": "Issue Commented in",
    "IssuesEvent": "Opened a new issue in",
    "PullRequestEvent": "New pull request",
    "WatchEvent": "A new user is watching",
    "ForkEvent": "A new fork was created to"
}


def github_activity(
        username: Annotated[str, typer.Argument(help="Github username")]
):
    response = requests.get(f"https://api.github.com/users/{username}/events")

    content = json.loads(response.content)

    for row in content:
        print(f"{messages[row['type']] if row['type'] in messages.keys() else row['type']} {row['repo']['name']}")


app = typer.Typer()
app.command()(github_activity)

if __name__ == "__main__":
    app()
