#!/bin/bash

# Set the new workspace URL
NEW_WORKSPACE_URL=$GITPOD_WORKSPACE_URL

# Add 'https://8000-' at the beginning
NEW_WORKSPACE_URL_WITH_PORT="https://8000-${NEW_WORKSPACE_URL#https://}"

# Set the path to your environment.js file
ENV_FILE_PATH="$PWD/frontend/src/environment.js"

# Replace the value of fastAPIUrl in the environment.js file
sed -i "s|fastAPIUrl: 'https://[^']*'|fastAPIUrl: '$NEW_WORKSPACE_URL_WITH_PORT/get_gemini_completion'|g" "$ENV_FILE_PATH"

echo "Updated fastAPIUrl in $ENV_FILE_PATH to $NEW_WORKSPACE_URL_WITH_PORT/get_gemini_completion"
