import reflex as rx
import Web.Styles.styles as styles
from Web.Styles.styles import Size, Spacing

def botones(title:str,body:str,image:str,url:str,is_external=True,highlight_color=None,animated=False) -> rx.Component:
    return rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=styles.Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title,size=Spacing.SMALL.value,style=styles.button_title_style),
                    rx.text(body,size=Spacing.VERY_SMALL.value,style=styles.button_body_style),
                    align_items='start',
                    spacing=Spacing.SMALL.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                align='center',
                width='100%'
            ),
            border=f"{'2px' if highlight_color != None else '0px'} solid {highlight_color}",
            class_name=styles.BOUNCEIN_ANIMATION if animated else None,
            on_click=rx.redirect(path=url, external=is_external)
        )