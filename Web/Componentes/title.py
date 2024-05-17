import reflex as rx
import Web.Styles.styles as styles

def titulo(text:str) -> rx.Component:
    return rx.heading(
        text,
        style=styles.title_style
    )