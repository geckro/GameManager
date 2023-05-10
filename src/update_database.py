import os
import git

class UpdateDatabase:
  
  def check(self):
    db_path = "data/db.csv"
    if os.path.exists(db_path):
        db_repo = git.Repo("data/")
        origin = db_repo.remote(name="origin")
        origin.fetch()
        if db_repo.is_dirty():
            print("Local repository is dirty, please commit any changes")
            return
        commits_behind = list(db_repo.iter_commits('main..origin/main'))
        if len(commits_behind) > 0:
            print(f"Local repository is {len(commits_behind)} commits behind origin/master")
            print("Pulling changes from remote repository...")
            db_repo.git.merge()
            print("Changes merged. Database updated.")
        else:
            print("Local repository is up-to-date")
    else:
        print("Downloading database...")
        git_repo_link = "https://github.com/geckro/GameDatabase.git"
        git_path_link = "data"
        git.Repo.clone_from(git_repo_link, git_path_link)

