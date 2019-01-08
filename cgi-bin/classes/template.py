import os

class Template:

    def __init__(self):
        pass

    def getTemplate(self, args):
        with open(os.getcwd() + '/cgi-bin/gui/template/' + args + '.html', 'r') as temp:
            html = temp.read()
            return html

    def getPage(self, args):
        with open(os.getcwd() + '/cgi-bin/gui/' + args + '.html', 'r') as temp:
            html = temp.read()
            return html