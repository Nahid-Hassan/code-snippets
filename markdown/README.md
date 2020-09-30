# Paragraph Tag
* *Italic*
* _Italic_
* **Bold**
* __Bold__
* ~~Strike~~
* In line paragraph

# Heading Tag
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

# Links
## First way
    Using <> tag
    Example:
        <https://www.google.com>

<https://www.google.com>
## Second way
    using [alternate_text](url)
    Example: 
        [Google](https://www.google.com)

[Google](https://www.google.com)

## Third way
    using [alternate_text](url space "Tooltip Text")
    If you hover on this link you see this tooltip text.

    Example: 
        [Google](https://www.google.com "Google url links.")

[Google](https://www.google.com "Google url links(Tooltip)")

## Forth way
    using [alternate_text][token/number]
    If you hover on this link you see this tooltip text.

    Example: 
        [Google][link]
        [Google][1]

    [link]: https://www.google.com
    [1]: https://www.google.com

[Google][link]

[Google][1]

[link]: https://www.google.com
[1]: https://www.google.com

# Image tag
## First way
    ![alternate_text](url/image_path)

    Example:
        ![Google Photo](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.TkPZZS4ttok6gOrfTasv2wHaEK%26pid%3DApi&f=1)

![Google Photo](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.TkPZZS4ttok6gOrfTasv2wHaEK%26pid%3DApi&f=1)


## Second way
    ![alternate_text](url/image_path _space_ "tooltip text")

    Example:
        ![Google Photo](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.TkPZZS4ttok6gOrfTasv2wHaEK%26pid%3DApi&f=1 "Google Logo")

![Google Photo](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.TkPZZS4ttok6gOrfTasv2wHaEK%26pid%3DApi&f=1 "Google Logo")

## Third way
    ![alternate_text][url/image_path]

    Example:
        ![Google Photo](image_url)

    [image_url]: https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.TkPZZS4ttok6gOrfTasv2wHaEK%26pid%3DApi&f=1

![Google Photo][image_url]

[image_url]: https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.TkPZZS4ttok6gOrfTasv2wHaEK%26pid%3DApi&f=1

## Forth way
    Use picture as a link
    []() -> represent a link
    ![]() -> represent a image
    [![()]]() -> represent image link

    [![alternate_text_for_image](image_path/image_url)](image_path/image_url)

    Example:
    [![image](https://picsum.photos/seed/picsum/20/20)](https://picsum.photos/seed/picsum/1200/1000)

    Here you can see a small image. To see original image click on the image.
    For this we use picsum.potos website image. You see for first_image_url 
    we set /20/20, that means height and width is 20 and 20 respectfully.
    For second portion we use 1200 and 1000.

[![image](https://picsum.photos/seed/picsum/20/20)](https://picsum.photos/seed/picsum/1200/1000)

`Fifth way. But this way is not work in github. You see that in t5_image.md file.`

# List tag
## Unordered list
    *,+,- sign for point. You can use any of them.
* Upper
  * Depth1
    * Depth2
  * Depth1 <br>
    [![image](https://picsum.photos/seed/picsum/20/20)](https://picsum.photos/seed/picsum/1200/1000)

## Ordered list
    Use:
        1. Age
        1. Name
        1. Id
        1. Year
## Effect
1. Age
1. Name
1. Id
1. Year

# Line breaks and Horizontal rule
## Line break
    For line break use <br> tag
## Horizontal rule
    For create horizontal rule use --- (at least 3 dash) 
        below the heading or any other sentence or word
    or you can use === (at least 3 equal sign) 
        below the heading or any other sentence or word
    
    Example:
        Heading1
        This line will be empty.
        ===

        Heading 2
        This line will be empty.
        ---
Heading 1

====

Heading 2

---
# Code block
    Use:
    ```language_type
    Write/paste your code here.
    ```
    Example - 1:
    ```py
    import os

    flag = True

    if flag:
        print(os.getcwd())
    ```
    Example - 2:
    ```diff
    + This line is added 
    - This line is deleted 
    ```
```py
import os

flag = True

if flag:
    print(os.getcwd())
```
```diff
var x = 10;
+ var y = 1000;
- var y = 2000;
```

# Table
    Use, 
        Center Align: | :---------: | :--------: |
        Left Align: | :--------- | :-------- |
        Right Align: | ---------: | --------: |

    Use case for center align
    | Dog's name | Dog's Age |
    | :--------: | :-------: |
    |   Buldog   |    12     |
    |   Nelly    |    13     |
    
## Center Align
| Dog's name | Dog's Age |
| :--------: | :-------: |
|   Buldog   |    12     |
|   Nelly    |    13     |


# Checkbox
## Check box
    * _space_ [X/Null] Text/Token
  
      * [X] Name
      * [ ] Age
      * [ ] Id
      * [ ] Year

## Effect
* [X] Name
* [ ] Age
* [ ] Id
* [X] Year

## Github treats
    I had same problem in #51 but fixed in #86 @github_user_name @mursalin117 

## Effect
I had same problem in #51 but fixed in #86 @github_user_name @mursalin117

# Task Lists
    - [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
    - [x] list syntax required (any unordered or ordered list supported)
    - [x] this is a complete item
    - [ ] this is an incomplete item

- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

# Emoji
    GitHub supports emoji!
    To see a list of every image we support, check out the Emoji Cheat Sheet.

[Emoji](https://help.github.com/articles/basic-writing-and-formatting-syntax/#using-emoji)

[Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)

# Github markdown mastering link
[Github markdown mastering](https://guides.github.com/features/mastering-markdown/)