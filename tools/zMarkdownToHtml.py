
import markdown

def md2html(mdstr):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

    html = '''
    <html lang="en">
    <head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link rel="stylesheet" href="zStyles.css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>ArchZ</title>
    <link
        href="https://fonts.googleapis.com/css2?family=Source+Code+Pro:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,200;1,300;1,500;1,600;1,700;1,800;1,900&display=swap"
        rel="stylesheet"
    />
    <link rel="icon" href="/resources/LogoIcon.png" type="image/x-icon"/>
    </head>
    <body>
    %s
    </body>
    </html>
    '''

    ret = markdown.markdown(mdstr,extensions=exts)
    return html % ret

location = "C:\Zac\GitHub\ZacZhangzhuo.github.io\zCV.md"
md = open(location, "r", encoding="utf-8")
mdTexts = md.read()
print (md2html(mdTexts))


# if __name__ == '__main__':

#     if len(sys.argv) < 3:
#         print('usage: md2html source_filename target_file')
#         sys.exit()

#     infile = open(sys.argv[1],'r')
#     md = infile.read()
#     infile.close()


#     if os.path.exists(sys.argv[2]):
#         os.remove(sys.argv[2])


#     outfile = open(sys.argv[2],'a')
#     outfile.write(md2html(md))
#     outfile.close()

#     print('convert %s to %s success!'%(sys.argv[1],sys.argv[2]))