from urllib import request
gog_url = 'https://www.forbes.com/sites/freddiedawson/2014/09/30/how-to-create-a-social-network-that-makes-money/#8d452b72c802'
def download_page(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'gog.csv'
    fx = open(dest_url,"w")
    for line in lines:
        fx.write(line +"\n")
    fx.close()
download_page(gog_url)
