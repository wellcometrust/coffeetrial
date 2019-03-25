.DEFAULT_GOAL := all

VIRTUALENV := build/virtualenv

IMAGE := rct
VERSION := 2019.3.1
LATEST_TAG := latest


.PHONY: docker-build
docker-build: \
	api


$(VIRTUALENV)/.installed: requirements.txt
	@if [ -d $(VIRTUALENV) ]; then rm -rf $(VIRTUALENV); fi
	@mkdir -p $(VIRTUALENV)
	virtualenv --python python3.6 $(VIRTUALENV)
	$(VIRTUALENV)/bin/pip3 install -r requirements.txt
	touch $@

.PHONY: virtualenv
virtualenv: $(VIRTUALENV)/.installed

.PHONY: all
all: virtualenv docker-build
