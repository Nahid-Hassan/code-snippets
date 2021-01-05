# HTML Elements Reference

- [HTML Elements Reference](#html-elements-reference)
  - [Main Root](#main-root)
    - [`<html>`: The HTML Document / Root Element](#html-the-html-document--root-element)
  - [Document metadata](#document-metadata)

## Main Root

### `<html>`: The HTML Document / Root Element

The HTML `<html>` element represents the root (top-level element) of an HTML document, so it is also referred to as the root element. All other elements must be descendants of this element.

| Option             | Description                                                                                                                                                                                |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content Categories | None                                                                                                                                                                                       |
| Permitted content  | One `<head>` element, followed by one `<body>` element.                                                                                                                                    |
| Tag omission       | The start tag may be omitted if the first thing inside the `<html>` element is not a comment. The end tag may be omitted if the `<html>` element is not immediately followed by a comment. |
| Permitted parents  | None. This is the root element of a document.                                                                                                                                              |

**Example**:

```html
<!DOCTYPE html>
<html lang="en">
  <head>...</head>
  <body>...</body>
</html>
```

## Document metadata

Metadata contains information about the page. This includes information about styles, scripts and data to help software (search engines, browsers, etc.) use and render the page. Metadata for styles and scripts may be defined in the page or link to another file that has the information. 

