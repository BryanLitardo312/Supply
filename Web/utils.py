import reflex as rx


preview = "https://moure.dev/preview.jpg"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@mouredev"}
]

#Index
index_title='Primax | Empresa N#1 en el Sector Hidrocarburífero',
index_description='Esta es una simple aplicación de prueba, rápida de aprender y fácil de usar!'

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)



#Modulo 1
modulo1_title='Primax | Empresa N#1 en el Sector Hidrocarburífero',
modulo1_description='Esta es una simple aplicación de prueba, rápida de aprender y fácil de usar!'

courses_meta = [
    {"name": "og:title", "content": modulo1_title},
    {"name": "og:description", "content": modulo1_description},
]
courses_meta.extend(_meta)




def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")