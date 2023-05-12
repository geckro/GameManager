import os
import git
import configparser


class UpdateDatabase:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('conf/settings.ini')

    def check(self):
        db_path = "data/db.csv"

        # Check to see if the database file exists already
        if os.path.exists(db_path):

            # Get the repo origin and fetch updates
            db_repo = git.Repo("data/")
            origin = db_repo.remote(name="origin")
            origin.fetch()

            # Check if local repository in data/ has changes made. If so, block changes
            if db_repo.is_dirty():
                # while loop to prompt user for confirmation
                while True:
                    print("Local repository has been changed, are you sure you want to update?")
                    dirty_input = input("y/n: ")
                    if dirty_input.lower() == "y":
                        break
                    elif dirty_input.lower() == "n":
                        return
                    print("Enter a valid input.")

            # List commits that the local repo is behind on
            commits_behind = list(db_repo.iter_commits('main..origin/main'))
            if len(commits_behind) > 0:
                print(f"Local repository is {len(commits_behind)} commits behind. Updating...")
                db_repo.git.merge()
                return "Database updated."

            # If there are no new changes
            else:
                return "Local repository is up-to-date"

        # If data/db.csv does not exist locally
        else:
            print("Downloading database...")
            git_repo_link = "https://github.com/geckro/GameDatabase.git"
            git_path_link = "data"
            try:
                git.Repo.clone_from(git_repo_link, git_path_link)
            except git.GitCommandError as error:
                print(f"Failed to clone repository: {error}")

    def update_check(self):
        try:
            config_update_check = int(self.config['updatecheck']['check'])
        except (KeyError, ValueError):
            print("Error: config file is missing 'updatecheck' section or 'check' key.")
            return

        if config_update_check == 0:
            return
        elif config_update_check == 1:
            while True:
                update = input("Do you want to update? y/n: ")
                if update.lower() == "y":
                    break
                elif update.lower() == "n":
                    return
            self.check()
        elif config_update_check == 2:
            self.check()
