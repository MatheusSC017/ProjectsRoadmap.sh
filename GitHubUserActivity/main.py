import requests
import typer
import json
from typing_extensions import Annotated


def github_activity(
        username: Annotated[str, typer.Argument(help="Github username")]
):
    response = requests.get(f"https://api.github.com/users/{username}/events")

    content = json.loads(response.content)

    for row in content:
        print(row.keys())
        print(row["type"])


app = typer.Typer()
app.command()(github_activity)

if __name__ == "__main__":
    app()
