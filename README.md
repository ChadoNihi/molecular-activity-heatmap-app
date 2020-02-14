# WIP molecular activity visualization web app

A task for one job interview.

Build w/ [FastAPI](https://fastapi.tiangolo.com/) & [Svelte](https://svelte.dev/).

## Build and run the app
0. (Have Python 3.6+ and Node.js 10+ installed.)
1. Build FE:
`(cd frontend; npm i; npm run build)`
2. Run the web app:
`(cd backend; uvicorn main:app --reload)`
3. Follow the output from the command line on errors (like absent dependencies).
4. FE app is served on [127.0.0.1:8000](http://127.0.0.1:8000), while the activity data is on [127.0.0.1:8000/api/activity](http://127.0.0.1:8000/api/activity) (and auto-generated API docs are on [127.0.0.1:8000/docs](http://127.0.0.1:8000/docs))

## Fetch the newest [ChEMBL](https://chembl.gitbook.io/chembl-interface-documentation/web-services/chembl-data-web-services) data
`(cd backend; python3 fetch_pchembl_values.py)`

Then find the data in _backend/data/pchembl_values.json_. (The JSON is also served at _/api/activity_.)

## Running tests
### FE
`(cd frontend; npm run test)`

To run the FE tests automatically on each file change:
`(cd frontend; npm run test:watch)`

### BE
`(cd backend; pytest)`

### FE + BE
`./run-all-tests.sh`

## Next steps

- use feature branches
- finish the app
- fix FIXMEs and TODOs from the code
- generate requirements.txt
- Dockerize the app
- lock FE dependencies
