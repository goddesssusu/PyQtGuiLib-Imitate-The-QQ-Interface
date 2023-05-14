# -*- coding: utf-8 -*-
# @Time    : 2023/5/14 13:45
# @Author  : 讨厌自己
# @Email   : 507194368@qq.com
# @File    : pushButton.py
# @Software: PyCharm
from PyQtGuiLib.header import (
    QPushButton,
    QObject,
    QEvent,
    Qt,
    QLabel,
    QPainter,
    QFontMetrics,
    QPainterPath,
    QColor,
    QPen,
    QBrush,
    QPaintEvent,
    QEnterEvent
)


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


class StrokeFontButton(QPushButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hovered = False

    def enterEvent(self, event: QEnterEvent) -> None:
        self._hovered = True
        self.update()

    def leaveEvent(self, event: QEvent) -> None:
        self._hovered = False
        self.update()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setFont(self.font())

        pen = QPen(Qt.GlobalColor.red)
        pen.setStyle(Qt.PenStyle.SolidLine)
        pen.setWidth(1)

        metrics = QFontMetrics(self.font())
        w = metrics.width(self.text(), Qt.TextFlag.TextSingleLine)
        h = metrics.height()
        x = (self.width() - w) / 2
        y = (self.height() - h) / 2 + h - 3

        path = QPainterPath()
        path.addText(x, y, self.font(), self.text())
        painter.strokePath(path, pen)
        painter.fillPath(path, QBrush(Qt.GlobalColor.yellow))

        if self._hovered:
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRoundedRect(self.rect(), 2, 2)
