page = '<p>holaaaaaaa</p><a href="http://elmundo.com">Inicio</a><h1>asdasd<h2><a href="http://udacity.com">Inicio</a>'


start_link = page.find('<a href=')

start_url = page.find('"',start_link)
end_url = page.find('"',start_url+1)

url = page[start_url+1:end_url]

print url;
