from flask import Flask, request, Response
from typing_extensions import Annotated
import requests
import typer

cache = {}


def caching_proxy(
    port: Annotated[int, typer.Option(help="Port used to run the proxy")] = 3000,
    origin: Annotated[str, typer.Option(help="link to the website that will be targeted by the proxy")] = "http://dummyjson.com"
):
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
    @app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def proxy(path=''):
        method = request.method
        data = request.get_data()
        headers = {key: value for key, value in request.headers if key != 'Host'}

        dest_url = f"{origin}/{path}"

        if dest_url not in cache.keys():
            response = requests.request(method, dest_url, headers=headers, data=data)
            headers = [(k, v) for k, v in response.headers.items()
                       if k not in ('Content-Length', 'Content-Encoding', 'Transfer-Encoding', 'Connection', 'X-Cache')]
            content, status_code = response.content, response.status_code

            cache[dest_url] = (content, status_code, headers)
            headers.append(('X-Cache', 'MISS'))

        else:
            content, status_code, headers = cache[dest_url]
            headers.append(('X-Cache', 'HIT'))

        return Response(content, status_code, headers=headers)

    app.run(debug=True, port=port)


app = typer.Typer()
app.command()(caching_proxy)

if __name__ == "__main__":
    app()
