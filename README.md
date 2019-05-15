# Shiptrader

A platform on which users can buy and sell Starships.
Technical information about the Starships on sale from the [Starship
API](https://swapi.co/documentation#starships).

## Getting started

* Install [Docker](https://docs.docker.com/compose/install/#install-compose)
* Run the following shell commands:

```
> docker-compose up

# You can run `manage.py` commands using the `./manapy` wrapper.
# To load data into DB from external SWAPI resource:
> ./manapy load_ships
# Running tests:
> pytest
```

## Endpoints

* `/swagger-docs` to browse with Swagger-UI.
* `/api/v1/starship` to browse Starships (GET).
* `/api/v1/listing` to browse, create and edit Listings for Starship sales (GET, POST, PATCH).

## Functionality

* A potential buyer can browse all Starships
* A potential buyer can browse all the listings for a given `starship_class` (provided `is_active is True`).
* A potential buyer can sort listings by price or time of listing
* To list a Starship as for sale, the user should supply the listing name, Starship name and list price.
* A seller can deactivate and reactivate their listing (PATCH request with listing ID and a value for `is_active` field).
