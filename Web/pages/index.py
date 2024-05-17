import reflex as rx
import Web.utils as utils
from Web.Componentes.barra import barra
from Web.Vistas.Encabezado.header import header
from Web.Views.enlaces import enlaces
from Web.Pie.footer import footer
#from Web.Styles.styles import Size as Size
import Web.Styles.styles as styles

@rx.page(
        title=utils.index_title,
        description=utils.index_description
)

def index() -> rx.Component:
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