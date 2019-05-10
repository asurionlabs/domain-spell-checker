###
# Domain Spell Checker is an AWS Lambda interface to perform spell checks using a domain 
# specific dictionary.
# 
# Copyright (C) 2018-2019  Asurion, LLC
#
# Domain Spell Checker is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Domain Spell Checker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Domain Spell Checker.  If not, see <https://www.gnu.org/licenses/>.
###
PYVERSION ?= 3.6
APP_NAME = domain-spell-checker

.PHONY: build
build:
	@python3 --version 2>&1 | grep $(PYVERSION)
	@if [ -d "dist" ]; then rm -rf dist/; fi
	@if [ -d "target" ]; then rm -rf target/; fi
	@mkdir dist target
	@cp -r *.py requirements.txt dictionary.txt dist/
	@pip3 install -r requirements.txt -t dist
	@find dist/ -type f -name "*.py[co]" -exec rm {} +
	@cd dist && zip -r $(APP_NAME).zip *
	@cd ..
	@mv dist/$(APP_NAME).zip target/$(APP_NAME).zip
	@rm -rf dist/
	@echo "Deployment package is ready at target/$(APP_NAME).zip"