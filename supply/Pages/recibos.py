import reflex as rx
from ..Componentes.sidebar import sidebar

@rx.page(route="/", title="Recibos")
def recibo() -> rx.Component:
    return rx.hstack(
        sidebar(),
        rx.text('Hola mundo!'),
        bg="#0D0D0D"
    )