
import markdown

def md2html(mdstr):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

    html = '''
    <html lang="en">
    <head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link rel="stylesheet" href="zMarkdownStyles.css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>zCV</title>
    <link
        href="https://fonts.googleapis.com/css2?family=Source+Code+Pro:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,200;1,300;1,500;1,600;1,700;1,800;1,900&display=swap"
        rel="stylesheet"
    />
    <link rel="icon" href="/resources/LogoIcon.png" type="image/x-icon"/>
    </head>
    <body>
    <img class="portrait" src="resources/Zac_6.jpg" alt="portrait">
    %s
    </body>
    </html>
    '''

    ret = markdown.markdown(mdstr,extensions=exts)
    return html % ret

location = "zCV.md"
htmlLocation = "zCV.html"
md = open(location, "r", encoding="utf-8")
mdTexts = md.read()
# print (md2html(mdTexts))
md.close()

html = open(htmlLocation, "w", encoding="utf-8")
html.write(md2html(mdTexts))
html.close()
print ("z: THIS FILE WOULD BE MODIFIED: zCV.html")