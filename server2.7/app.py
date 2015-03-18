#trial version for markup project

import web

def make_text(string):
    return string

urls = ('/', 'tutorial')

render = web.template.render('templates/')

app = web.application(urls, globals())

my_form = web.form.Form(
                web.form.Textbox('Type it here =>', class_='textfield', id='textfield'),
                )

class tutorial:
    def GET(self):
        form = my_form()
        return render.tutorial(form, "The text will appear here.")
        
    def POST(self):
        form = my_form()
        form.validates()
        s = form.value['textfield']
        return make_text(s)

if __name__ == '__main__':
    app.run()

