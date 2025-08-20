import reflex as rx
from ..Componentes.sidebar import sidebar

def recibo() -> rx.Component:
    return rx.hstack(
        sidebar(),
        rx.text('Hola mundo!')
    )