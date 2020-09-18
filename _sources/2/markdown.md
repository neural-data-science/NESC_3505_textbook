```{figure} images/markdown_logo.png
---
align: left
width: 65px
```
# Markdown

[**Markdown**](https://daringfireball.net/projects/markdown/) is a "plain text formatting syntax" and a tool for converting such plain text to a formatted version, such as [HTML](https://en.wikipedia.org/wiki/HTML) for display in a web page. Recall earlier the discussion about plain text (.txt files) versus rich text (such as in Microsoft Word or Google Docs). Rich text files display the text that you enter, and the formatting you choose (e.g., boldface), and hide the information telling your computer to make that text boldface "behind the scenes" in a complex file. In contrast, when you open a plain text file, what you see is literally the contents of that file, with nothing hiding in the background (except for a couple of hidden features, like markers for line breaks and tabs).

So a plain text file can never contain formatting like boldface or italic. Markdown allows you to create a text file with special codes that you type to "mark" certain text for formatting, and then run a program on that text file to produce a formatted output. For example, text surrounded by `*one asterisk*` shows up in italics: *one asterisk*; while text surrounded by `**two asterisks**` shows up as boldface: **two asterisks**. Different levels of headings can be indicated with hash marks; the more hash marks, the more deeply embedded a header is. So, the following:
`# Heading 1`
`## Heading 2`
`### Heading 3`
 Produces:
 # Heading 1
 ## Heading 2
 ### Heading 3


 If you haven't already guessed, the online textbook you are currently reading is written largely in Markdown.

While originally Markdown was designed to simplify creating web pages in HTML (the coding language for web pages), there are now a huge number of output formats available (e.g., PDF, Microsoft Word, ePub) in different applications, and many Markdown apps that allow you write and edit Markdown files while viewing a preview of the formatted output in another window alongside your Markdown text file.

HTML — and by extension, Markdown — embodies a design philosophy of separating the content of a document from its formatting. That is, when writing the content, you focus on writing, not how it's going to look, and then later, you apply formatting to make it look a certain way. This means that the same document can be formatted in virtually any possible way, with different fonts, sizes, etc.. It also provides consistency (e.g., you don't have to remember to manually make every first-level heading a specific larger font size, and bold) and makes it very easy to produce professional-looking output without professional web design skills.

 As noted earlier, Jupyter notebook cells can also contain Markdown, allowing you to produce rich and professional-looking text alongside your code. So, you will use Markdown a lot in this course in writing up assignments and projects. It's pretty simple and quick to learn. The [official Markdown site](https://daringfireball.net/projects/markdown/syntax) provides thorough documentation on its syntax, although I find this [Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/) more efficient for finding the most commonly-needed things — or [this one](https://www.ibm.com/support/knowledgecenter/en/SSGNPV_2.0.0/dsx/markd-jupyter.html) for some extra fancy Markdown you can use in Jupyter notebooks.
