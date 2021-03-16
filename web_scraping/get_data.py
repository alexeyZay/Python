from bs4 import BeautifulSoup

html_string = """
	<!DOCTYPE html>
	<html>
	<head>
		<title>Web Development Page</title>
		<style type="text/css">

			h1{
				color: white;
				background: blue;
			}

			li{
				color: red;
			}

			#css-li{
				color: blue;
			}

			.green{
				color: green;
			}

		</style>
	</head>
	<body>
		<h1>Web Development</h1>
		<h1 class="green">Web</h1>
		<h3>Programming Languages</h3>

		<ol>
			<li>HTML</li>
			<li id="css-li">CSS</li>
			<li class="green bold">JavaScript</li>
			<li class="green">Python</li>
		</ol>

	</body>
	</html>



"""

parsed_html = BeautifulSoup(html_string, 'html.parser')

# print(parsed_html.body.ol.li)
# print(parsed_html.find('li'))
# print(type(parsed_html.find('li')))
# print(parsed_html.find_all('li'))
# print(type(parsed_html.find_all('li')))
# print(parsed_html.find(id="css-li"))
# print(parsed_html.select('#css-li')[0])
# print(parsed_html.find_all(class_="green"))
# print(parsed_html.select(".green")[1])
# print(parsed_html.select("li")[3])
# html_elem=parsed_html.select("li")[3]
# print(html_elem.get_text())
# html_elem_list=parsed_html.select("li")
# for html_elem in html_elem_list:
#     print(html_elem.get_text())
# for classes
# html_class_green_list=parsed_html.select(".green")
# for html_class_elem in html_class_green_list:
#     print(html_class_elem.get_text())
# for html_class_elem in html_class_green_list:
#     print(html_class_elem.name)
#
# html_class_green_list=parsed_html.select("li")
# for html_class_elem in html_class_green_list:
#     print(html_class_elem.attrs)

# to get more specific attrs you can use
html_list=parsed_html.select("li")[3]
for html_elem in html_list:
#    print(html_list.attrs["class"]) # return class trribute for selected element
    print(html_list["class"]) # return class trribute for selected element