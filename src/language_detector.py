import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from PIL.ImageQt import ImageQt
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

    def init_listeners(self):
        self.ui.importButton.clicked.connect(lambda: self.import_file())
        self.ui.runButton.clicked.connect(lambda: self.predict())

    def init_frequencies(self):
        with open('assets/letter-frequency.txt', encoding='utf-8') as csv_file:
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
        # plt.show()

        plt_img = self.fig2img(plt.gcf())
        self.ui.graph.setScaledContents(True)
        self.ui.graph.setPixmap(QPixmap.fromImage(ImageQt(plt_img)))
        plt.clf()

    def fig2data(self, fig):
        # draw the renderer
        fig.canvas.draw()

        # Get the RGBA buffer from the figure
        w, h = fig.canvas.get_width_height()
        buf = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint8)
        buf.shape = (w, h, 4)

        # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
        buf = np.roll(buf, 3, axis=2)
        return buf

    def fig2img(self, fig):
        """
        @brief Convert a Matplotlib figure to a PIL Image in RGBA format and return it
        @param fig a matplotlib figure
        @return a Python Imaging Library ( PIL ) image
        """
        # put the figure pixmap into a numpy array
        buf = self.fig2data(fig)
        w, h, d = buf.shape
        return Image.frombytes("RGBA", (w, h), buf.tostring())

    def ask_for_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(QWidget(
        ), "Choose a Text File", "", "All Files (*);;Python Files (*.py)", options=options)
        if filename:
            return filename
        return ''
