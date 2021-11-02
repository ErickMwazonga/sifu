# MARKDOWN
# HEADER 1
## TEXT
### Headers
# This is an <h1> tag

## This is an <h2> tag

###### This is an <h6> tag

### Emphasis

_This text will be italic_
_This will also be italic_

### BOLD

**This text will be bold**
**This will also be bold**

_You **can** combine them_

### Strikethrough
Any word wrapped with two tildes (like ~~this~~) will appear crossed out.

### Comments

Hiding content with comments

## <!-- This content will not appear in the rendered Markdown -->

---

## LISTS

### Unordered

You can make an unordered list by preceding one or more lines of text with - or \*.

* Item 1
* Item 2
  - Item 2a
  - Item 2b

### Ordered

order your list, precede each line with a number.

1. Item 1
2. Item 2
3. Item 3
   1. Item 3a
   2. Item 3b

---

## Images
![GitHub Logo](/md.png)

---

## URL

URL: [Google Link](www.google.com)

---

## Blockquotes

As Kanye West said:

> We're living the future so
> the present is our past.

---

## CODE

### Inline Code

I think you should use an
`<addr>` element here instead.

### Syntax Highlighting

```
git status
git add
git commit
```

```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

```js
function fancyAlert(arg) {
  if (arg) {
    $.facebox({ div: "#foo" });
  }
}
```

```py
def foo():
    if not bar:
        return True
```

---

### Definition Lists

Some Markdown processors allow you to create definition lists of terms and their corresponding definitions

Melanin
: This is the definition of the first term.

---

## Task Lists

- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [ ] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

---

## Tables

| First Header                | Second Header                |
| --------------------------- | ---------------------------- |
| Content from cell 1         | Content from cell 2          |
| Content in the first column | Content in the second column |

---

## Emojis

[Refer Here](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)
Syntax -> :smiley:
