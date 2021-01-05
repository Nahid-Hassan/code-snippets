# Hyper Text Markup Language

## Table of Contents

- [Hyper Text Markup Language](#hyper-text-markup-language)
  - [Table of Contents](#table-of-contents)
    - [Anchor Tag](#anchor-tag)
    - [Abbreviation Tag](#abbreviation-tag)
    - [Address Tag](#address-tag)
    - [Area Tag](#area-tag)

### Anchor Tag

``` html
<a href="test.html" title="popup text" target="_blank" name="section_name" 
download="file_name" hreflang="en"></a>
```

| Attribute | Value                     | Example                                                                  |
| :-------- | :------------------------ | :----------------------------------------------------------------------- |
| href      | url/path                  | `<a href="images/girls.jpg">Link</a>`                                    |
| title     | Popup Text                | `<a title="This is a popup text">Link</a>`                               |
| target    | _blank,_self/_parent/_top | `<a target="_blank">Link</a>`                                            |
| name      | section_name              | `<a name="computer">Computer</a>` <br> `<a href="#computer">Computer</>` |
| hreflang  | target page language      | `<a hreflang="en">Link</a>`                                              |

### Abbreviation Tag

```html
<p>My name is Nahid and I am studying in <abbr title="Computer Science and Engineering">CSE</abbr> of <abbr
    title="Rajshahi University">RU</abbr></p>
```

| Attribute | Value      | Example                              |
| :-------- | :--------- | :----------------------------------- |
| title     | Popup Text | `<abbr title="Bangladesh">BD</abbr>` |

### Address Tag

```html
<address>
        Written By <a href="mailto:nahid.cseru@gmail.com">Md. Nahid Hassan</a> <br>
        Visit Us At <a href="https://sdt-inc.github.io/">Software and Data Technology</a> <br>
        Jamalpur, Bangladesh.
</address>
```

**Note**: Normally we write one `address` tag per page and one or more `article` tag per page.

### Area Tag

- The `<area>` tag defines an area inside an image-map (an image-map is an image with clickable areas).
- The `<area>` element always nested in a `<map>` tag.

For clear understand please click on this image.

[![Image Alt Text Here](https://img.youtube.com/vi/QpGXIGYclO4/0.jpg)](https://www.youtube.com/watch?v=QpGXIGYclO4)
