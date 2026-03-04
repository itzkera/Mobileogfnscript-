from mitmproxy import http

EPIC_GAMES = (
    "game-social.epicgames.com",
    "ol.epicgames.com",
    "ol.epicgames.net",
    "on.epicgames.com",
    "ak.epicgames.com",
    "epicgames.dev",
)

def request(flow: http.HTTPFlow) -> None:
    host = flow.request.pretty_host

    if host and host.endswith(EPIC_GAMES):
        print(f"Redirecting {host} to localhost lol")

        # send it to my backend instead
        flow.request.scheme = "http"
        flow.request.host = "127.0.0.1"
        flow.request.port = 3551
        flow.request.headers["Host"] = host
