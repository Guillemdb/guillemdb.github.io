current_dir = $(shell pwd)

PROJECT = retrospective
DOCKER_ORG = guillemdb
DOCKER_TAG ?= ${PROJECT}
VERSION ?= latest
n ?= auto

.PHONY: install
install:
	pip3 install -r sphinx/requirements-docs.txt
	cd sphinx && make html && cd ..

.PHONY: run
run:
	cd sphinx && make server
