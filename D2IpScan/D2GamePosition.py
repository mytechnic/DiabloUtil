def getDisplayPosition(display):
    config = {
        '1280x768': {
            'tabMenu': (810, 75, 940, 98),
            'title': (885, 150, 1135, 160),
            'password': (885, 198, 1135, 208),
            'createButton': (945, 480, 1080, 505),
            'exitButton': (555, 355, 745, 380)
        }
    }

    return config[display]
