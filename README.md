# WIP molecular activity visualization web app

A task for one job interview.

Build w/ [FastAPI](https://fastapi.tiangolo.com/) & [Svelte](https://svelte.dev/).

## Build and run the app
0. (Have Python 3.6+ and Node.js 10+ installed.)
1. Build FE:
`(cd frontend; npm i; npm run build)`
2. Run the web app:
`(cd backend; uvicorn main:app --reload`)
3. Follow the output from the command line.

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
- generate requirements.txt
- Dockerize the app
- lock FE dependencies
