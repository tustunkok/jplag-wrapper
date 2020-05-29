from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QHBoxLayout, QGroupBox, QVBoxLayout, QFileDialog, QComboBox
from PyQt5.QtCore import QRect

import sys
import os
import subprocess
import logging

logging.basicConfig(
    filename="output.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 150
        self.lang = "java19"

        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)

        self.create_layout()

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(self.group_box)
        self.setLayout(vbox_layout)

        self.show()
    
    def create_layout(self):
        vbox_layout = QVBoxLayout()

        hbox_layout = QHBoxLayout()

        btn_source = QPushButton("Choose Source", self)
        btn_source.setMinimumHeight(28)
        btn_source.clicked.connect(self.click_source_btn)
        hbox_layout.addWidget(btn_source)

        btn_destination = QPushButton("Choose Destination", self)
        btn_destination.setMinimumHeight(28)
        btn_destination.clicked.connect(self.click_destination_btn)
        hbox_layout.addWidget(btn_destination)

        btn_start = QPushButton("Start", self)
        btn_start.setMinimumHeight(28)
        btn_start.clicked.connect(self.click_start_btn)
        hbox_layout.addWidget(btn_start)

        vbox_layout.addLayout(hbox_layout)

        self.lang_cb = QComboBox()
        self.lang_cb.addItems("java19,java17,java15,java15dm,java12,java11,python3,c/c++,c#-1.2,char,text,scheme".split(","))
        self.lang_cb.currentIndexChanged.connect(self.selection_changed_lang_gb)
        vbox_layout.addWidget(self.lang_cb)


        self.group_box = QGroupBox("JPlag Wrapper")
        self.group_box.setLayout(vbox_layout)
    
    def click_source_btn(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.DirectoryOnly)

        if dlg.exec_() == QFileDialog.Accepted:
            self.source_dir = dlg.selectedFiles()[0]
            logging.info("Source dir: '%s'", dlg.selectedFiles())
            print(dlg.selectedFiles())
    
    def click_destination_btn(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.DirectoryOnly)

        if dlg.exec_() == QFileDialog.Accepted:
            self.destination_dir = dlg.selectedFiles()[0]
            logging.info("Destination dir: '%s'", dlg.selectedFiles())
            print(dlg.selectedFiles())
    
    def click_start_btn(self):
        logging.info("JPlag started with source: '%s' and destination: '%s'", self.source_dir, self.destination_dir)
        print("Started with source: {} and destination: {}".format(self.source_dir, self.destination_dir))
        jplag_process = subprocess.run(f"java -jar ./jplag.jar -l {self.lang} -s '{self.source_dir}' -r '{self.destination_dir}'", shell=True, stdout=subprocess.PIPE)
        
        with open("jplag_output.txt", "w") as jplag_output_fd:
            jplag_output_fd.write(jplag_process.stdout.decode())
        
        logging.info("JPlag completed.")
        print("JPlag completed.")
    
    def selection_changed_lang_gb(self, i):
        logging.info("Selection changed to %s", self.lang_cb.currentText())
        print("Selection changed to", self.lang_cb.currentText())
        self.lang = self.lang_cb.currentText()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())