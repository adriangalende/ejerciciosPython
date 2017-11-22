def domain_name(url):
    assert isinstance(url,str),"No mete String como parametro"
    assert len(url) > 0, "la url viene vacia"

    if len(url.split('.')[1]) <= 3:
        return url.split('://')[1].split('.')[0]
    else:
        return url.split('.')[1]


#print(domain_name("http://.github.com/carbonfive/raygun"))
#print(domain_name("http://www.zombie-bites.com"))
#print(domain_name("https://www.cnet.com"))
print(domain_name("http://google.com"))
