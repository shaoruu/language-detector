import os
import csv
import sys
import uuid
import shutil
import atexit
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QFileDialog, QListWidgetItem
from PyQt5.QtGui import QPixmap

from .ui import Ui_MainWindow


class LanguageDetector(QWidget):
    def __init__(self):
        self.language_dict = dict()

        self.init_ui()
        self.init_listeners()
        self.init_frequencies()

    def init_ui(self):
        self.app = QApplication(sys.argv)
        self.main_window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.ui.graph.setScaledContents(True)

    def init_listeners(self):
        self.ui.importButton.clicked.connect(lambda: self.import_file())
        self.ui.runButton.clicked.connect(lambda: self.predict())
        atexit.register(self.on_terminate)

    def init_frequencies(self):
        with open(Path('assets/letter-frequency.txt'), encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')

            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    for language in row:
                        self.language_dict[language] = dict()

                for language in row:
                    self.language_dict[language][row['Letter']] = row[language]

                line_count += 1

    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec_())

    def import_file(self):
        filename = self.ask_for_file()

        if filename == '':
            return

        with open(filename) as text:
            whole_text = text.read()
            self.ui.inputBox.setText(whole_text)

    def predict(self):
        text = self.ui.inputBox.toPlainText().lower().replace(' ', '')

        if not text:
            self.ui.graph.setText("Empty Input\n Detected.")
            return

        text_letter_lookup = dict()

        for letter in text:
            if letter in self.language_dict['Letter']:
                if letter in text_letter_lookup:
                    text_letter_lookup[letter] += 1
                else:
                    text_letter_lookup[letter] = 1

        # normalize data
        sum = 0
        for count in text_letter_lookup.values():
            sum += count

        text_letter_freq = dict()
        for letter, count in text_letter_lookup.items():
            text_letter_freq[letter] = count / sum

        # calculate difference
        text_scores = dict()
        for language in self.language_dict:
            if language != 'Letter':
                score = 0

                for letter in text_letter_freq:
                    expected = float(
                        self.language_dict[language][letter]) / 100.0
                    if letter in text_letter_freq:
                        score += abs(expected - text_letter_freq[letter]) ** 2
                    else:
                        score += expected ** 2

                text_scores[language] = score

        # print(text_scores)
        prediction_results = sorted(
            text_scores.items(), key=lambda item: item[1])

        self.list(prediction_results)
        self.graph(prediction_results)

    def list(self, prediction_results):
        index = 1
        self.ui.languagesList.clear()
        for language in prediction_results:
            self.ui.languagesList.addItem(
                f"{index}.  {language[0]} - {round(language[1] * 100, 2)}")
            index += 1

    def graph(self, prediction_results):
        ypos = np.arange(len(prediction_results))

        languages = [l[0][0:2] for l in prediction_results]
        values = [v[1] for v in prediction_results]

        plt.xticks(ypos, languages)
        plt.ylabel('score')
        plt.bar(ypos, values)

        file_loc = str(Path(f"saves/{str(uuid.uuid1())}.png"))
        plt.savefig(file_loc)

        self.ui.graph.setPixmap(QPixmap(file_loc))
        plt.clf()

    def on_terminate(self):
        # removed saved images
        folder = Path('saves')
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    def ask_for_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(QWidget(),
                                                  "Choose a Text File",
                                                  "",
                                                  "All Files (*);;Python Files (*.py)",
                                                  options=options)
        if filename:
            return filename
        return ''
