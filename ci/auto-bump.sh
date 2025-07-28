#!/bin/bash

set -o errexit

git config --global user.name "$GIT_USER"
git config --global user.email "$GIT_EMAIL"
git config http.https://gitlab.mitre.org.sslcainfo /etc/ssl/certs/ca-certificates.crt
git remote set-url origin \
    "https://gitlab-ci-token:${GITLAB_CI_TOKEN}@${CI_SERVER_HOST}/${CI_PROJECT_PATH}.git"

echo $(git remote get-url origin)

exists=`git show-ref refs/heads/main` && if [ -n "$exists" ]; then git branch -D main; fi
git checkout -b main

git status

echo "Auto Bumping Repo"
cz bump --changelog --check-consistency --yes --no-verify --prerelease alpha

git status
git push origin main:$CI_COMMIT_REF_SLUG --tag -f
