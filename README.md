###Install dependency
##### pre-requisite: install pipenv
    brew install pipenv
#### dependency
	sh setEnv.sh
	pipenv install
#### activate
    pipenv shell
	
### Local Dev Environment
#### spin up database from docker
	docker pull postgres

	docker run --name dealerDB -e POSTGRES_DB=dealer -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres

##### copy to generate local database property and fill in the information
	cp car_dealer/settings/local-template.py car_dealer/settings/local.py

##### apply migration
	python manage.py makemigration

###Run Application
    python manage.py runserver --settings=car_dealer.settings.{env}