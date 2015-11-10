# Installation

~~~
$ sudo apt-get install wkhtmltopdf
~~~

# PDF Generator Testing 結果

- 如果沒有涵蓋大範圍 Unicode 的 字型，多國語系必須逐步設定字型。單一字型產生 PDF 會有些國家的字無法顯示！
- 每個語系分區都有那個範圍的 Font 支援！ ref: http://www.alanwood.net/unicode/fontsbyrange.html
- 另類解法。用 Windows Unicode 補完計畫 + HTML 轉 PDF！ ref: https://175fd66bab27fccf9f16aa157d7261e6c150ae2a.googledrive.com/host/0BxHqn7o9vZBaWVZKVWhoUVNKa1U/
- HTML to PDF Library！ ref: https://pypi.python.org/pypi/pdfkit
- HTML to PDF，可解多語系字型問題！HTML 檔頭讀字碼一定要捨定！ ex: <meta http-equiv="content-type" content="text/html; charset=UTF-8">
- Unifont 字型系列：unifont.ttf - 可正常顯示很多國家的字包含 CJK！
- Unifont 字型系列：unifont-all.ttf - unitfont smooth version！ ref: https://math.berkeley.edu/~serganov/ilyaz.org/software/fonts/
- Arial Unicode MS 字型系列：arialuni.ttf - Arial Unicode MS 可正常顯示很多國家的字包含 CJK！！
- ref: http://unifoundry.com/unifont.html
- ref: http://ergoemacs.org/emacs/emacs_unicode_fonts.html
- 支援中文的 Unicode Font 至少也是 1x MB 以上。如過太小估計不支援中文！
- ref: https://github.com/rolandwalker/unicode-fonts
- ref: http://unicode.org/resources/fonts.html ( Unicode 官網推薦 )

# 結論

01. 使用 HTML to PDF 解吧！ (推薦)
![Alt text](https://raw.githubusercontent.com/scott1028/PDFGeneratorFontIssueStudy/master/test03.png "PDF View")
02. 使用 unifont.tff (幾乎都支援到最新的Unicode版本，但是字體不好看，有一好沒兩好！)
![Alt text](https://raw.githubusercontent.com/scott1028/PDFGeneratorFontIssueStudy/master/unifont.ttf.jpg "Unifont View")
**03. 使用 arialuni.ttf - Arial Unicode MS (推薦)**
![Alt text](https://raw.githubusercontent.com/scott1028/PDFGeneratorFontIssueStudy/master/test04.jpg "Unifont View")
