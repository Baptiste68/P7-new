#! /usr/bin/env python
from gbapp import app

if __name__ == "__main__":
    app.config['TESTING']=True
    app.run(debug=True)