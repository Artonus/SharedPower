import os

class Template:

    def __init__(self):
        pass
    # reading template for a piece of web page 
    def getTemplate(self, args):
        with open(os.getcwd() + '/gui/template/' + args + '.html', 'r') as temp:
            html = temp.read()
            return html    