import reflex as rx
from supply.Styles.styles import Size


def icono(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.LARGE.value,
            alt=alt
        ),
        href=url,
        is_external=True
    )