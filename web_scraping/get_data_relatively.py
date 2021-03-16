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
			<li class="green" id="python-li">Python</li>
		</ol>

	</body>
	</html>



"""

# parsed_html = BeautifulSoup(html_string, 'html.parser')
# data = parsed_html.body.contents # returns all the childs for body as a list. If any child have its own childs then it will be displayed as a one element
# print(data)

# '\n' in the list is a new line carret symbol BUT IT will be counted when you will try to get the elements by Id's

parsed_html = BeautifulSoup(html_string, 'html.parser')
# data = parsed_html.body.contents[7] # if you need to see its childs select 'contents' one mpre time
# data = parsed_html.body.contents[7].contents # if you need to see its childs select 'contents' one mpre time
# print(data)

# siblins is the element on one hierarhy if you want to get them call='next_sibling' so many time you need from one to another
# data = parsed_html.body.contents[1].next_sibling.next_sibling
# print(data)

# to switch from child to parent use 'parent' at the end
# data = parsed_html.find(id="css-li").parent.previous_sibling.previous_sibling
# print(data)

# to avoid '\n' empty strings you can use method find_next_sibling
# data = parsed_html.find(id="css-li").find_next_sibling()
# print(data)
# data = parsed_html.find(id="css-li").find_previous_sibling()
# print(data)

data = parsed_html.find(id="css-li").find_next_sibling(id="python-li")
print(data)

# same for Find Parent 'find_next_parent()' / 'find_Children()[1]'