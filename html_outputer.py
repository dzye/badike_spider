
#encoding:utf-8
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')
        fout.write("<html><meta charset='utf-8'><style>.c_url{width:15%;}.c_title{width:15%;}.c_summary{width:70%;}td{border:1px solid;text-align:center;}</style>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td class=c_url>%s</td>"%data['url'])
            fout.write("<td class=c_title>%s</td>" % data['title'].encode('utf8'))
            fout.write("<td class=c_summary>%s</td>" % data['summary'].encode('utf8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")