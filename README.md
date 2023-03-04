# efficom-car-dealer

A back-end app serving resources representing a car-dealer

# Documentation
documentation is automatically available at [FQDN](https://fr.wikipedia.org/wiki/Fully_qualified_domain_name):port/docs/ or /redoc
The default FQDN is `localhost` and default port is 80.

# Run the application
Two possible modes to launch the application, the recommended one is Docker mode.  
Once launched, the app will be accessible at http://localhost except if you've changed port 80 to something else.
## Docker mode
**requirements:** docker and docker-compose installed  
To launch, you terminal must be in the root folder of this repository. Then issue :  
`docker-compose up --build`

## Uvicorn mode
**requirements:** python3.10 or greater installed  
First, install dependencies
`pip install -r requirements.txt`

Then, run the app:  
`uvicorn app.main:app --host 0.0.0.0 --port 80`
