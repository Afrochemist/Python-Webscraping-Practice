from bs4 import BeautifulSoup

html_doc = """
<html>
	<head>
		<title>The happy people</title>
	</head>
	<body>
		<p class="title>
			<b>Miami, FL</b>
		</p>
		<p class="story">Mary
			<a href="http://example.com/elsie class="sister" id="link1">Elsie</a>
			<a href="http://example.com/lacie class="sister" id="link2">Lacie</a>
			<a href="http://example.com/tillie class="sister" id="link3">Tillie</a>
		</p>
		<p class="story"> ...</p>
	</body>
</html>
"""

soup = BeautifulSoup(html_doc, "lxml")

p_tags = soup.find_all('p')

# p_tag = soup.find('p', class_ = title)#

a = soup.find_all('a', {'id':'link1'})

a_elsie = soup.find_all('a', string = 'Elsie')

#search for all child#
p = soup.find('p', class_ = 'story')
all_p_children = p.findChildren()

# search for parent
p = soup.find('p', class_ ='story')
p_parent =  p.findParent()

#search for siblings
first_a = soup.find('a')
remain_sibling = first_a.findNextSiblings()

#for loop with a_tags
for a in a_tags:
	print a['href']


print (p_parent)