import reflex as rx
from ..Componentes.sidebar import sidebar

@rx.page(route="/", title="Recibos")
def recibo() -> rx.Component:
    return rx.hstack(
        sidebar(),
        rx.vstack(
            rx.vstack(
                rx.box(height="2em"),
                rx.heading('Pedido Septiembre', font_size="2em", font_weight="bold", color="white",align="left"),
                margin_left="2em",
            ),
            rx.vstack(
                rx.box(
                    rx.vstack(
                        rx.text("Aquí va el contenido principal de la página de recibos.", font_size="1.5em",color="white"),
                        rx.text("Aquí va el contenido principal de la página de recibos.", font_size="1.5em",color="white"),
                        spacing="3",
                    ),
                    bg="#212121",
                    width="90%",
                    padding="20px",
                    border_radius="10px",
                    height="h-screen",
                ),
                width="100%",
                spacing="5",
                align_items="center",
            ),
            width="100%",
            spacing="5",
            class_name="h-screen"
        ),
        bg="#0D0D0D"
    )