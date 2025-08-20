import reflex as rx
from ..backend.backend import State
                
color_letra="#0A0A0A"
color_letra2="#010159"


def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon,color="white",size=25),
            rx.text(text, color="white",size="3", weight="medium"),
            width="100%",
            padding_left="2rem",
            padding_y="1rem",
            align="center",
            style={
                "_hover": {
                    "bg": "black",
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Resumen", "bar-chart-4", "/supabase"),
        sidebar_item("Novedades", "landmark", "/novedades"),
        sidebar_item("Suministros", "square-library", "/suministros"),
        sidebar_item("Devoluciones", "hand-coins", "/devoluciones"),
        spacing="3",
        width="100%",
        align="center",
        justify="center",
    )


def sidebar_bottom_profile() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.vstack(
                    rx.box(
                        rx.image(
                            src="/primax_logo.png",
                            width="11rem",
                            height="auto",
                            background="#212121",
                            border_radius="20%",
                            margin="0px",
                        ),
                        height="100%",
                        border="none",
                        border_radius="20%",
                        bg="#212121",
                        box_shadow="0 8px 32px rgba(255,255,255,0.38)"
                    ),
                    align="center",
                    justify="center",
                    padding_x="0.5rem",
                    width="100%",
                ),
                rx.box(height="1.5em"),
                sidebar_items(),
                rx.spacer(),
                rx.vstack(
                    rx.divider(height="3px",width="100%"),
                    rx.hstack(
                        rx.icon_button(
                            rx.icon("user"),
                            size="3",
                            radius="full",
                            color="white",
                            background_color="black",
                        ),
                        rx.vstack(
                            rx.box(
                                rx.text(
                                    "Mi cuenta",
                                    size="3",
                                    weight="bold",
                                    color="white",
                                ),
                                rx.text(
                                    State.email,
                                    size="2",
                                    weight="medium",
                                    color="white",
                                ),
                                width="100%",
                            ),
                            spacing="0",
                            align="start",
                            justify="start",
                            width="100%",
                        ),
                        padding_x="0.5rem",
                        align="center",
                        justify="start",
                        width="100%",
                    ),
                    rx.vstack(
                        #sidebar_item(
                            #"Settings", "settings", "/#"
                        #),
                        rx.button(
                            rx.hstack(
                                rx.icon("log-out",size=20,border_color="black"),
                                rx.text("Cerrar sesión", size="3",weight="medium"),
                                spacing="1",
                            ),
                            background_color="#0D0D0D",
                            on_click=State.logout,
                            width="100%",
                            align="center",
                            justify="center",
                            style={
                                "_hover": {
                                    "bg": "#E96207",
                                    "color": "white",
                                },
                            },
                            height="100%",
                            border_radius="md",
                        ),
                        width="100%",
                        height="3em"

                    ),
                    width="100%",
                    spacing="5",
                ),
                spacing="5",
                left="0px",
                top="0px",
                padding_x="1em",
                padding_y="1.5em",
                background="#212121",
                align="start",
                width="20em",
                height="100vh",
                position="sticky",
                
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                            ),
                            sidebar_items(),
                            rx.spacer(),
                            rx.vstack(
                                rx.vstack(
                                    sidebar_item(
                                        "Settings",
                                        "settings",
                                        "/#",
                                    ),
                                    sidebar_item(
                                        "Log out",
                                        "log-out",
                                        "/#",
                                    ),
                                    width="100%",
                                    spacing="1",
                                ),
                                rx.divider(margin="0"),
                                rx.hstack(
                                    rx.icon_button(
                                        rx.icon("user"),
                                        size="3",
                                        radius="full",
                                    ),
                                    rx.vstack(
                                        rx.box(
                                            rx.text(
                                                "My account",
                                                size="3",
                                                weight="bold",
                                            ),
                                            rx.text(
                                                State.email,
                                                size="2",
                                                weight="medium",
                                            ),
                                            width="100%",
                                        ),
                                        spacing="0",
                                        justify="start",
                                        width="100%",
                                    ),
                                    padding_x="0.5rem",
                                    align="center",
                                    justify="start",
                                    width="100%",
                                ),
                                width="100%",
                                spacing="5",
                            ),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        padding="1.5em",
                        bg="#edebeb",
                    ),
                    width="100%",
                    spacing="5",
                ),
                direction="left",
                spacing="5",
                left="0px",
                top="0px",
                padding_x="1em",
                padding_y="1.5em",
                bg="rgb(245, 245, 245)",
                align="start",
                width="17em",
                height="100vh",
                position="sticky",
            ),
        ),
        text_overflow="ellipsis",
        overflow="hidden",
    )