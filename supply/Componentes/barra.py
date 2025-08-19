import reflex as rx
#import Web.Styles.styles as styles
import supply.Styles.styles as styles
import supply.Styles.colors as colors
from supply.routes import Route


def barra() -> rx.Component:
    return rx.hstack(
        rx.link(
        rx.box(
                rx.text("Siempre", as_="span", color=colors.Color.PRIMARY.value),
                rx.text(" más", as_="span", color=colors.Color.SECONDARY.value),
                style=styles.barra_title_style
        ),
        href=Route.INDEX.value
        ),
        position='sticky',
        bg=colors.Color.CONTENT.value,
        padding_x=styles.Size.DEFAULT.value,
        padding_y=styles.Size.SMALL.value,
        z_index='999',
        top='0'
    )