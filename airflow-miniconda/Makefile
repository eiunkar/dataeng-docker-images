SHELL := /usr/bin/env bash

#######
# Help
#######

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sorted(sys.stdin):
	match = re.match(r'^([$()a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))

endef
export PRINT_HELP_PYSCRIPT

help:
	@ python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

###################
# Conda Enviroment
###################

IMAGE_NAME := nyer-airflow-miniconda
IMAGE_TAG := 1.10.2

.PHONY: build
build: ## build docker image
	cp ../LICENSE .
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

.PHONY: push
push: ## push docker image
	docker push $(IMAGE_NAME):$(IMAGE_TAG)
