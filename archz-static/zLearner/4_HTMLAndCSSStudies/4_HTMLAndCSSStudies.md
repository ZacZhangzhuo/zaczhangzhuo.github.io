# htmlAndCssStudies

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale = 1" />
    <meta name="keywords" content="html, css " />
    <meta name="description" content="This is the personal website of ArchZ " />
    <!-- meta name="description" is to show the brief of the webpage, like 'Apple' '探索 Apple 充满创新的世界....'-->
    <title>My first web page</title>
    <!--  This is the name in the tab -->
    <style>
      /* css style about the images */
      img {
        width: 100px;

        border-radius: 50px;
        /* Circular corner, if border-radius = width*0.5, the image is a circle */

        float: left;
        /* floating in the right*/

        margin-right: 10px;
        /* Margin in the right of the image */

        object-fit: cover;
      }

      .username {
        font-weight: bold;
      }

      em {
        color: red;
        font-style: normal;
      }
    </style>
  </head>
  <body>
    <h1>h1</h1>
    <h2>h2</h2>
    <!-- Choosing headings are meant to create hierarchies not the size. Remember the size can always be changed by css-->
    <!-- it is better that each website only have one single H1. Not too much  -->

    <img src="images/logo.jpg" alt="logo.jpg" />

    <p class="username">@ArchZ</p>
    <!-- class is a way to categorize the elements -->

    <p>I am <em>ArchZ</em></p>
    <!-- <em> means emphasize, !but remember that DO NOT use <em> for italic proposes, and everything about styling should be in css. <em> also helps search engine to find important elements  -->
    <!-- Similar: <em>, <strong>, <i>(italic), <b>(bold)  -->

    <p>I love Architecture</p>

    <!-- !HTML entity:        < = &lt;         >=&gt;           © =  &copy;       -->

    <a href="about.html"> <img src="images/logo.jpg" alt="images" /> </a>
    <!-- URL of a element use <a> -->
    <!-- To go one level up of the location: ../ . Ex1: ../index.html. Ex2: ../../../index.html-->

    <!-- Link images -->
    <a href="images/logo.jpg">image</a>
    <!-- Link images and automatic download -->
    <a href="images/logo.jpg" download> image and download</a>

    <!-- Jump when click -->
    <h2 id="section-css">CSS</h2>
    <a href="#section-css">jumpToCss</a>

    <!-- Jump to top -->
    <a href="#"> Jump to top</a>

    <!-- Link to google and open in a new window -->
    <a href="https://www.google.com/" target="_blank">Google</a>

    <!-- Mail to -->
    <a href="mailto:ArchZ@outlook.com">Email me</a>
  </body>
</html>
```

```CSS
  .img:hover {
    /* only apply when hover. Pseudo Class */
  }
```

## CSS structure
* block element
* in-line block element
* in-line element
* By default, a paragraph is a block element (Takes up the entire line)

## Div = Division