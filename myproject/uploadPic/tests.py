from django.test import TestCase
from StringIO import StringIO
from PIL import Image
from django.test import Client

class ListViewsTestCase(TestCase):
    def test_list(self):
        c = Client()
        # Generate a picture
        file = StringIO()
        image = Image.new("RGBA", size=(50,50), color=(256,0,0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        
        print "Here is the post data:", file.name
        # get post response from list form with parameter docfile = file
        resp = c.post('/uploadPic/list/',{'docfile': file})
        print "Response status:", resp.status_code
        print "Here is the response: ", resp
        