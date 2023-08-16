# User Authentication Service

This project is aimed at creating a user authentication service using Flask, where users can register, log in, and log out. It will demonstrate the usage of API routes, cookie handling, form data retrieval, and returning different HTTP status codes.

## Learning Objectives

By completing this project, you will gain the following skills:

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should follow the `pycodestyle` style (version 2.5)
- Use SQLAlchemy 1.3.x
- All files must be executable
- Code length will be tested using `wc`
- All modules, classes, and functions should be documented
- Functions should be type annotated
- The Flask app should only interact with `Auth` and never with `DB` directly
- Only public methods of `Auth` and `DB` should be used outside these classes

## Setup

To install the required `bcrypt` package, run the following command:

```bash
pip3 install bcrypt
