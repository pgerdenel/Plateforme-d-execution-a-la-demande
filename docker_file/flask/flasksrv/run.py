#!/usr/bin/env python3
from zmapp import app

if __name__ == "__main__":
    app.run(host="172.17.0.3", port=8081, debug=True)