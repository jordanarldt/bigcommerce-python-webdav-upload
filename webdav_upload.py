import requests
from requests.auth import HTTPDigestAuth

# Below, put the URL of your BigCommerce WebDAV, including the file name you want to create/upload
#    If you're uploading a CSV that you want to use as a product import, you will put it in the /dav/import_files/ directory.

url='https://store-abcdefg123.mybigcommerce.com/dav/import_files/products_upload_filename.csv' # example

# Local filename relative to this python script to upload

files = open('products_upload_filename.csv', 'rb')

# BigCommerce WebDAV login credentials.
#    Found under Server Settings > File Access (WebDAV)

usern = 'youremail@email.com' # username
passw = 'password123' # password


# Make the file upload request
r = requests.request('PUT', url=url, data=files, auth=HTTPDigestAuth(usern, passw))

r.status_code

print(r.headers) 
print(r.status_code)
