
#encoding:utf-8
import pymongo
class HtmlOutputer(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        db = client.test_db
        self.datas = db['data']

    def collect_data(self, data):
        if data is None:
            return
        self.datas.insert(data)

    def output_html(self):
        fout = open('output.html','w')
        fout.write("<html><meta charset='utf-8'><style>.c_url{width:15%;}.c_title{width:15%;}.c_summary{width:70%;}td{border:1px solid;text-align:center;}</style>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas.find():
            fout.write("<tr>")
            fout.write("<td class=c_url>%s</td>"%data.get('url'))
            fout.write("<td class=c_title>%s</td>" % data.get('title').encode('utf8'))
            fout.write("<td class=c_summary>%s</td>" % data.get('summary').encode('utf8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")