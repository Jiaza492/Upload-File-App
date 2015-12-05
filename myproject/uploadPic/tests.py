from django.test import TestCase
from StringIO import StringIO
from PIL import Image

class ListViewsTestCase(TestCase):
    def test_list(self):
        # Generate a picture
        file = StringIO()
        image = Image.new("RGBA", size=(50,50), color=(256,0,0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        # get post response from list form with parameter docfile = file
        resp = self.client.get('/uploadPic/list/',{'docfile': file})
#         print resp.status_code
        self.assertEqual(resp.status_code, 200)
        