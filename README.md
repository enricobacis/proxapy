# Proxapy

Simple API proxy that uses Flask/requests/gunicorn.

## Use cases

 * **Centralize API requests** - Sometimes only a specific IP can access APIs. Run Proxapy on that machine in order to gain access to the API from everywhere.
 * **Implement custom pre/post operation on API request/response** - Fork the project, add routes and implement your changes. Common changes include content filtering, add of authentication key header not known by the end user.

## Usage

 1. Make sure you have [virtualenv][1]
 2. `make run`
 3. Use `http://localhost:5000/<apihost>:<apiport>` to access the API at `http://<apihost>:<apiport>`
 
[1]: https://virtualenv.pypa.io
