import reflex as rx

config = rx.Config(
    app_name="supply",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV3Plugin(),
        # otros plugins aquí
    ],
)