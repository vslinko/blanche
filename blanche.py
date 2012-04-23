import os
import hashlib
import urllib.request
from bottle import get, post, static_file, request, run


__all__ = ["make_hash", "upload", "download"]


CONFIG={"hostname": None, "root": None}


def make_hash(arg):
    hash = hashlib.sha512(arg).hexdigest()
    return (hash[:3], hash[3:])


def upload(file, host="cdn.rithis.com"):
    return str(urllib.request.urlopen("http://{0}/files/".format(host), file).read(), encoding="ascii")


def download(url, host="cdn.rithis.com"):
    return str(urllib.request.urlopen("http://{0}/files/download".format(host), url.encode("ascii")).read(), encoding="ascii")


def controller(file_content):
    file_hash = make_hash(file_content)

    directory_path = os.path.join(CONFIG["root"], file_hash[0])

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    file_path = os.path.join(directory_path, file_hash[1])

    if not os.path.exists(file_path):
        with open(file_path, "wb") as f:
            f.write(file_content)

    return "//{0}/files/{1}/{2}".format(CONFIG["hostname"], file_hash[0], file_hash[1])


@post("/files/")
def post_file():
    return controller(request.body.read())


@post("/files/download")
def post_download_file():
    url = str(request.body.read(), encoding="ascii")
    return controller(urllib.request.urlopen(url).read())


@get("/files/<directory>/<file>")
def get_file(directory, file):
    return static_file(filename=file, root=os.path.join(CONFIG["root"], directory))


def main(hostname, root, **kwargs):
    CONFIG["hostname"] = hostname
    CONFIG["root"] = root
    run(**kwargs)
