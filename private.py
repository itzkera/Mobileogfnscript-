from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if ".ol.epicgames.com" in flow.request.pretty_host:
        flow.request.scheme = "http"
        flow.request.host = ""
        flow.request.port = 3551
