import reflex as rx
import Web.Styles.styles as styles
import Web.Styles.colors as colors
from Web.Componentes.iconos import icono


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(src='icon-primax.png',size='8'),
            rx.vstack(
                rx.heading('ATIMASA',
                           font_size=styles.Size.LARGE.value
                ),
                rx.heading(
                    'Departamento de Administración',
                    margin_top=styles.Size.ZERO,
                    font_size=styles.Size.DEFAULT.value,
                    weight='bold'
                ),
                align_items='start'
            ),
            spacing=styles.Spacing.BIG.value
        ),
        rx.vstack(
            rx.text(
                """‘’La única forma de hacer un gran trabajo es amar lo que haces’’""",
                color=colors.TextColor.BODY.value,
                font_size=styles.Size.DEFAULT.value,
            ),
            rx.text(
                """Steve Jobs""",
                color=colors.TextColor.BODY.value,
                font_size=styles.Size.DEFAULT.value,
            ),
            align_items='center',
            spacing=styles.Spacing.SMALL.value
        ),
        align_items='center',
        spacing=styles.Spacing.BIG.value,
        width='100%'
    )
