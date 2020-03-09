#!/usr/bin/env python3
#
# Sets up helm repos
#
# Usage:
#
# Create environment variables like so
#   HELM_REPO_<repo_name>=<repo_url>
#
import os
import re
import subprocess

def get_repos_from_env():
  repos = {}
  repo_pattern = re.compile('^HELM_REPO_(.+)')
  for k, v in os.environ.items():
    repo_name = repo_pattern.match(k)
    if repo_name == None:
      continue
    repo_name = repo_name.group(1)
    repo_url = v
    print(f"Got repo '{repo_name}' ({repo_url})")
    repos[repo_name] = repo_url
  return repos

def add_repos(repos):
  def add_repo(repo_name, repo_url):
    subprocess.run(['helm','repo','add',repo_name,repo_url])
  for repo_name, repo_url in repos.items():
    add_repo(repo_name, repo_url)


repos = get_repos_from_env()
if len(repos) > 0:
  add_repos(repos)
  subprocess.run(['helm','repo','update'])
