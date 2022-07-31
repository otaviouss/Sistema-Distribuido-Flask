init: requirements.txt
	pip install -r requirements.txt
	prisma generate --schema=./servidor/bd/schema.prisma

client: interface/main.py
	python3 interface/main.py

server: run.py
	cd servidor/bd && prisma py fetch
	python3 run.py