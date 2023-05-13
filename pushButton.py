# -*- coding: utf-8 -*-
# @Time    : 2023/5/14 3:45
# @Author  : 讨厌自己
# @Email   : 507194368@qq.com
# @File    : pushButton.py
# @Software: PyCharm
from PyQtGuiLib.header import QPushButton, QObject, QEvent, Qt, QLabel


class PushButton(QPushButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setVisible(False)
        self.parent().installEventFilter(self)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.HoverEnter:
            self.show()
        elif event.type() == QEvent.Type.HoverLeave:
            self.hide()

        return super().eventFilter(watched, event)


class CPushButton(QPushButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCheckable(True)
        self.setAutoExclusive(True)


class MPushButton(QPushButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)


class Label(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
