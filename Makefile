.DEFAULT_GOAL := all

VIRTUALENV := build/virtualenv

IMAGE := coffeetrial
ECR_IMAGE := 160358319781.dkr.ecr.eu-west-1.amazonaws.com/uk.ac.wellcome/coffeetrial
VERSION := 2019.6.9
LATEST_TAG := latest


.PHONY: docker-build
docker-build: \
	base-image \
	api-image

.PHONY: api-image
api-image:
	docker build \
		-t $(IMAGE):$(VERSION) \
		-t $(IMAGE):$(LATEST_TAG) \
		-t $(ECR_IMAGE):$(VERSION) \
		-t $(ECR_IMAGE):$(LATEST_TAG) \
		-f Dockerfile \
		.

.PHONY: base-image
base-image:
	docker build \
	    -t $(IMAGE).base:$(VERSION) \
	    -t $(IMAGE).base:$(LATEST_TAG) \
		-f Dockerfile.base \
		.

.PHONY: docker-push
docker-push: docker-build
	@echo "Running 'aws ecr get-login' && docker push ..."
	@LOGIN=$$(aws ecr get-login --no-include-email --region eu-west-1) && \
	$$LOGIN && \
	docker push $(ECR_IMAGE):$(VERSION) && \
	docker push $(ECR_IMAGE):$(LATEST_TAG)


$(VIRTUALENV)/.installed: requirements.txt
	@if [ -d $(VIRTUALENV) ]; then rm -rf $(VIRTUALENV); fi
	@mkdir -p $(VIRTUALENV)
	virtualenv --python python3.6 $(VIRTUALENV)
	$(VIRTUALENV)/bin/pip3 install -r requirements.txt
	touch $@

.PHONY: virtualenv
virtualenv: $(VIRTUALENV)/.installed

.PHONY: run
run:
	docker-compose up -d && \
	./docker_exec.sh python3 manage.py recreate-db && \
	./docker_exec.sh python3 manage.py new-round

.PHONY: all
all: virtualenv docker-build
