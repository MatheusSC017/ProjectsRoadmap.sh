# Caching Proxy

This project involves building a simple command-line interface (CLI) tool that starts a caching proxy server. The server forwards requests to an origin server and caches the responses. If the same request is made again, the proxy returns the cached response instead of forwarding the request.

## Installing CLI

> pipx ensurepath

restart the terminal

> pipx install .

## Commands

Use the command below to initialize the proxy, informing the target site and the port that will be used.

> caching-proxy --port 3000 --origin http://dummyjson.com

The command below is used to clear the cache

> caching-proxy --clear
