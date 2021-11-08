

import sys
from PyQt5.QtWidgets import QApplication

from widgetgallery import WidgetGallery
import qtmodern.styles
import qtmodern.windows


def main():
    app = QApplication(sys.argv)
    qtmodern.styles.dark(app)
    
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()