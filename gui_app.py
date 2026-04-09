#!/usr/bin/env python3
"""
Vocabulary IPA - Language Pronunciation Retriever
Main GUI application using modular UI components.
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.loader = QUiLoader()

        # Load the main window UI without a parent to avoid conflicts
        main_ui_file = QFile("ui/main_window.ui")
        main_ui_file.open(QIODevice.ReadOnly)
        main_window_widget = self.loader.load(main_ui_file)
        main_ui_file.close()

        # Extract properties from the loaded UI
        self.setWindowTitle(main_window_widget.windowTitle())
        self.setGeometry(main_window_widget.geometry())
        self.setStyleSheet(main_window_widget.styleSheet())

        # Set up the central widget and tab widget
        central_widget = main_window_widget.centralwidget
        self.setCentralWidget(central_widget)
        self.tab_widget = central_widget.findChild(QTabWidget, "tabWidget")
        self.setStatusBar(main_window_widget.statusbar)

        # Load individual tab widgets
        self.load_tab_widgets()

    def load_tab_widgets(self):
        """Load individual tab UI files into the main tab widget."""
        # Languages tab
        languages_ui = QFile("ui/languages_tab.ui")
        languages_ui.open(QIODevice.ReadOnly)
        languages_widget = self.loader.load(languages_ui, self.tab_widget)
        languages_ui.close()
        # Replace the tab content
        old_widget = self.tab_widget.widget(0)
        self.tab_widget.removeTab(0)
        self.tab_widget.insertTab(0, languages_widget, "Languages")

        # Random words tab
        random_ui = QFile("ui/random_words_tab.ui")
        random_ui.open(QIODevice.ReadOnly)
        random_widget = self.loader.load(random_ui, self.tab_widget)
        random_ui.close()
        old_widget = self.tab_widget.widget(1)
        self.tab_widget.removeTab(1)
        self.tab_widget.insertTab(1, random_widget, "Random Words")

        # Retrieve tab
        retrieve_ui = QFile("ui/retrieve_tab.ui")
        retrieve_ui.open(QIODevice.ReadOnly)
        retrieve_widget = self.loader.load(retrieve_ui, self.tab_widget)
        retrieve_ui.close()
        old_widget = self.tab_widget.widget(2)
        self.tab_widget.removeTab(2)
        self.tab_widget.insertTab(2, retrieve_widget, "Retrieve Pronunciation")

        # Analyze tab
        analyze_ui = QFile("ui/analyze_tab.ui")
        analyze_ui.open(QIODevice.ReadOnly)
        analyze_widget = self.loader.load(analyze_ui, self.tab_widget)
        analyze_ui.close()
        old_widget = self.tab_widget.widget(3)
        self.tab_widget.removeTab(3)
        self.tab_widget.insertTab(3, analyze_widget, "Analyze")

        # About tab
        about_ui = QFile("ui/about_tab.ui")
        about_ui.open(QIODevice.ReadOnly)
        about_widget = self.loader.load(about_ui, self.tab_widget)
        about_ui.close()
        old_widget = self.tab_widget.widget(4)
        self.tab_widget.removeTab(4)
        self.tab_widget.insertTab(4, about_widget, "About")


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Vocabulary IPA")
    app.setApplicationVersion("1.0.0")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
