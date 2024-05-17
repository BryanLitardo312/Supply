import reflex as rx
import datetime
import Web.Styles.styles as styles

def footer() -> rx.Component:
    return rx.vstack(
            rx.image(
            src='logo-primax.png',
            width='auto',
            height=styles.Size.VERY_BIG.value,
            alt='Logotipo de Primax Ecuador'
            ),
            rx.link(
                f'2023-{datetime.date.today().year} Primax Siempre Más',
                href='https://mouredev.com',
                is_external=True,
                font_size=styles.Size.MEDIUM.value
            ),
            rx.text('Bienvenido al juego!',
                       font_size=styles.Size.MEDIUM.value,
                       margin_top=styles.Size.ZERO.value
                       ),
            margin_bottom=styles.Size.BIG.value,
            padding_x=styles.Size.SMALL.value,
            align_items='center'
    )