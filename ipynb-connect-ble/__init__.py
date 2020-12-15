from wificonnection.handlers import setup_handlers
# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'ipynb-connect-ble',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "notebook",
        "dest": "ipynb-connect-ble",
        "src": "static",
        "require": "ipynb-connect-ble/main"
    }]

def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp.web_app)
