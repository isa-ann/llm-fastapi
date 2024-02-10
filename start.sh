cd $GITPOD_REPO_ROOT
 chmod +x update_url.sh
  ./update_url.sh
docker compose build
docker compose up  