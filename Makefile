# Define the token file
TOKEN_FILE := token.txt

# Define the distribution directory
DIST_DIR := dist

# Define the setup script
SETUP_SCRIPT := setup.py

# Define the twine command with token
TWINE_UPLOAD := twine upload

.PHONY: all clean build upload

all: clean build upload

clean:
	@echo "Removing previous build artifacts..."
	@rm -rf $(DIST_DIR)
	@find . -name '*.egg-info' -exec rm -rf {} +

build:
	@echo "Building the distribution..."
	python $(SETUP_SCRIPT) sdist bdist_wheel

upload:
	@echo "Uploading the distribution..."
	@$(TWINE_UPLOAD) -u __token__ -p `cat $(TOKEN_FILE)` $(DIST_DIR)/*