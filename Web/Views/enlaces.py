import reflex as rx
from Web.Componentes.botones import botones
from Web.Componentes.title import titulo
from Web.Styles.styles import Color, Spacing
from Web.routes import Route

def enlaces() -> rx.Component:
    return rx.vstack(
        titulo("Servicios Atimasa"),
        botones('Conciliación Bancaria','Pasos a seguir','/icons/code.svg',Route.MODULO1.value,False,Color.SECONDARY.value),
        botones('Conciliación Financiera','Pasos a seguir','/icons/twitch.svg','https://www.google.com/'),
        botones('Conciliación Crediticia','Pasos a seguir','/icons/discord.svg','https://www.google.com/'),
        botones('Conciliación TC','Pasos a seguir','/icons/code.svg','https://www.google.com/'),
        botones('Conciliación Inventario','Pasos a seguir','/icons/discord.svg','https://www.google.com/'),
        width='100%',
        spacing=Spacing.DEFAULT.value
    )