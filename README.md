# Blanche is tiny CDN

## Serving

    ./console.py serve --server cherrypy --host 0.0.0.0 --port 80 --hostname cdn.example.com --root /data/cdn

## Usage

    >>> import blanche
    >>> blanche.upload(open("/etc/hosts", "rb").read())
    '//cdn.rithis.com/files/a97/ac8065934d0bd7c39e999167302c6f43515d5f372ce0932e4f5a1d3f2e0a6e9e3e5111b14195ff45809f8ce7d8a665d1a9eed34ae2fdd5b2be091c878aa5e'
    >>> blanche.download("http://cdn.rithis.com/files/a97/ac8065934d0bd7c39e999167302c6f43515d5f372ce0932e4f5a1d3f2e0a6e9e3e5111b14195ff45809f8ce7d8a665d1a9eed34ae2fdd5b2be091c878aa5e")
    '//cdn.rithis.com/files/a97/ac8065934d0bd7c39e999167302c6f43515d5f372ce0932e4f5a1d3f2e0a6e9e3e5111b14195ff45809f8ce7d8a665d1a9eed34ae2fdd5b2be091c878aa5e'
