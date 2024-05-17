from reflex import App, Title, Page, Paragraph

def test_page():
    return Page(
        children=[
            Title("Título de prueba"),
            Paragraph("Este es un párrafo de prueba.")
        ]
    )

app = App(pages=[test_page])

if __name__ == "__main__":
    app.run()
