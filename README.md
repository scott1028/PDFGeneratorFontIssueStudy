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

# 結論

- 使用 HTML to PDF 解吧！
