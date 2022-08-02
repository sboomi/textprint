import typer

app = typer.Typer()


@app.callback()
def callback():
    """
    textprint: your regex assistant
    """


@app.command()
def search():
    """
    Looks for a particular pattern on your text data
    """
