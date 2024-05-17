"""Welcome to Reflex! This file outlines the steps to create a basic app."""

#from rxconfig import config

import reflex as rx
from Web.pages.index import index
from Web.pages.Modulo1 import Modulo1
import Web.Styles.styles as styles




app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLES
)

#app.add_page(index)
#app.add_page(Modulo1)
