from PyQt6.QtWidgets import QMessageBox
from update_database import UpdateDatabase

class Help:
    def MenuAbout(self, parent):
        about_message = """
        GameManager
        Version 0.1
        (c) 2023 geckro
        
        https://github.com/geckro/GameManager
        License: MIT License
        """
        QMessageBox.about(parent, "About GameManager", about_message)
    def MenuUpdate(self, parent):
        updater = UpdateDatabase()
        status = updater.check()
        if status:
            QMessageBox.information(parent, "Update", status)
        else:
            QMessageBox.information(parent, "Update", "Database is up-to-date.")

