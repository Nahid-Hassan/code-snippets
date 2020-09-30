# Add image in markdown
    To do this using ![alter text](url/ image_path "also can use tooltip text"). 

    ! -> Says that this is an image.
    [] -> Alternate text
    () -> url/image_path
    "tooltip_text" -> url _space_ "tooltip_text"

## Example - 1
![wow great image](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.XBAG1kug3kec2UtrvkZ4EQHaEK%26pid%3DApi&f=1 "This is the tooltip")

## Example - 2
    To do this using ![alter_text][number/token]
    
    ! -> Says that this is an image
    [alter_text] -> First square brackets
    [token] -> second square brackets

![Another example][image_path]

[image_path]: https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.sV7tva-728oySeOUL0-vOwHaHa%26pid%3DApi&f=1

## Example - 3
    Use image as a link

    [![alter_text](url)](url)

    []() -> Says that this is a link
    ![]() -> Says that this is an image
    
    Now, [ ![]() ]() - > link[image]. Or we can say that image as a link.


[![image](https://picsum.photos/seed/picsum/20/20)](https://picsum.photos/seed/picsum/1200/1000)

    [![image](http://unplash.it/50/50?image=1000)](http://unplash.it/500/500?image=1000)

    Sadly say's this url is not work. But to aim this example is that firstly you see a little image, next if you click on this little image you can see a bigger image.

    or you can use...
    [<img src='url' >](url). You see the same effect of this [![]()]()

[<img src="https://picsum.photos/seed/picsum/10/10">](https://picsum.photos/seed/picsum/1360/768)

## Example - 4
    This example is not working with Github. But if you write a blog or something like this you can use this method....

    <img src='url' height="500" width=100% alt='Alternate text'>

    <style>
        img {
            width: 200px;
            height: 300px;
        }
    </style>

<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/%D0%9A%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%81_%D0%9C%D0%B8%D1%80%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B7%D0%B0%D0%BC%D0%BA%D0%B0.JPG/1628px-%D0%9A%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%81_%D0%9C%D0%B8%D1%80%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B7%D0%B0%D0%BC%D0%BA%D0%B0.JPG' height="500" width=100% alt='Alternate text'>

<style>
    img {
        width: 200px;
        height: 200px;
    }
</style>