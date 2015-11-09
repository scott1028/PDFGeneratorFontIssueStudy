# Installation

~~~
$ sudo apt-get install wkhtmltopdf
~~~

# PDF Generator Testing 結果

- 多國語系必須逐步設定字型。不可用單一字型產生 PDF 會有些國家的字無法顯示！
- 每個語系分區都有那個範圍的 Font 支援，似乎沒有看到全包的！ ref: http://www.alanwood.net/unicode/fontsbyrange.html
- 另類解法。用 Windows Unicode 補完計畫 + HTML 轉 PDF！ ref: https://175fd66bab27fccf9f16aa157d7261e6c150ae2a.googledrive.com/host/0BxHqn7o9vZBaWVZKVWhoUVNKa1U/
- HTML to PDF Library！ ref: https://pypi.python.org/pypi/pdfkit
- HTML to PDF，可解多語系字型問題！HTML 檔頭讀字碼一定要捨定！ ex: <meta http-equiv="content-type" content="text/html; charset=UTF-8">
- Noto Fonts Support！ ref: https://github.com/googlei18n/noto-fonts
- Noto CJK Fonts Support ref: https://github.com/googlei18n/noto-cjk
- Noto Font Brower ref: http://www.google.com/get/noto
- Droid font has support for CJK！ ref: http://stackoverflow.com/questions/18065028/does-dejavu-has-support-for-cjk-chinese-japanese-korean-glyphs
- 下載 Droid Sans 字型！ ref: http://eric.swiftzer.net/2011/05/download-droid-sans/, ref: https://www.google.com/fonts#UsePlace:use/Collection:Droid+Sans
- SakalBharati Font！ ref: http://stackoverflow.com/questions/30972339/is-there-any-single-font-which-support-all-indian-language-in-all-android-device
- Font Merge by yourself. ref: http://fontforge.github.io/en-US/
- test.ttf - DejaVuSans.ttf Merge fireflysung.ttf By Font Forge Tool, 必須產生為 TrueType Font！
- unifont.ttf - 可正常顯示很多國家的字包含 CJK！

# 結論

01. 使用 HTML to PDF 解吧！
02. 使用 unifont.tff

# Demo

![Alt text](https://raw.githubusercontent.com/scott1028/PDFGeneratorFontIssueStudy/master/test03.png "PDF View")
