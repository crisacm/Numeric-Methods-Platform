from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *

# from platform.methods.biseccion import Biseccion
# from platform.methods.regla_falsa import ReglaFalsa
# from platform.methods.newton_rapshon import NewtonRapshon


class Methods:
    @staticmethod
    def menu():
        menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_BORDER)\
            .set_title_align('center').set_subtitle_align('center')\
            .set_left_margin(2)\
            .set_right_margin(2)\
            .set_top_margin(0)\
            .show_prologue_top_border(True)\
            .show_prologue_bottom_border(True)
        menu = ConsoleMenu("Solución de Métodos Numéricos", prologue_text='Prologue text', formatter=menu_format)
        menu.formatter.set_top_margin(0)
        menu.formatter.set_left_margin(2)
        item_biseccion = MenuItem("Bisección")
        item_regla_falsa = MenuItem("Regla Falsa")
        item_newton_rapshon = MenuItem("Newton Rapshon")
        menu.append_item(item_biseccion)
        menu.append_item(item_regla_falsa)
        menu.append_item(item_newton_rapshon)
        menu.show()


if __name__ == "__main__":
    methods = Methods()
    methods.menu()