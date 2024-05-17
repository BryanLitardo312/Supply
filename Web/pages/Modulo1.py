import reflex as rx
import Web.utils as utils
from Web.routes import Route
from Web.Componentes.barra import barra
from Web.Vistas.Encabezado.header import header
from Web.Views.enlaces import enlaces
from Web.Pie.footer import footer
import Web.Styles.styles as styles

@rx.page(
        route=Route.MODULO1.value,
        title=utils.modulo1_title,
        description=utils.modulo1_description
)

def Modulo1() -> rx.Component:
    return rx.box(
        utils.lang(),
        barra(),
        rx.center(
            rx.vstack(
                header(),
                enlaces(),
                max_width=styles.MAX_WIDTH,
                width="60%",
                margin_y=styles.Size.BIG.value,
                padding=styles.Size.BIG.value
            )
        ),
        footer()
    )