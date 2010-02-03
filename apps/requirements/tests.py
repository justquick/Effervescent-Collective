
from django.test import TestCase
from models import Requirement

R="""-e  svn+http://code.djangoproject.com/svn/django/tags/releases/1.1.1/#egg=django
-e  svn+http://svn.aeracode.org/svn/south/tags/0.5#egg=south
-e  git+http://github.com/nathanborror/django-basic-apps.git#egg=basic
-e  git+http://github.com/justquick/django-tinymce.git#egg=tinymce
-e  git+http://github.com/justquick/django-tagging.git#egg=tagging
-e  hg+http://bitbucket.org/jespern/django-piston/#egg=piston
-e  hg+http://bitbucket.org/ubernostrum/django-contact-form/#egg=contact_form
-e  git+http://github.com/zerok/django-flatblocks.git#egg=flatblocks
-e  git+http://github.com/justquick/django-native-tags.git#egg=native_tags
-e  git+http://opensource.washingtontimes.com/git/public/django-staff.git/#egg=staff
-e  svn+http://django-mptt.googlecode.com/svn/trunk/#egg=mptt
-e  git+http://github.com/justquick/django-mptt-comments.git#egg=mptt_comments
-e  svn+http://django-template-utils.googlecode.com/svn/trunk/#egg=template_utils
-e  git+http://github.com/justquick/django-frontendadmin.git#egg=frontendadmin
-e  git+http://opensource.washingtontimes.com/git/public/django-categories.git/#egg=categories
simplejson==2.0.9
python-memcached==1.44
django-memcached==0.1.2
django-pagination==1.0.5
django-debug-toolbar==0.7.0
django-extensions==0.4.1
python-dateutil==1.4.1
setup/python-imaging_1.1.6-3.tar.gz
ipython
--find-links http://example.com/private-packages/
--index http://example.com/private-pypi/
-e hg+http://hg.myproject.org/MyProject/@da39a3ee5e6b#egg=MyProject
-e hg+http://hg.myproject.org/MyProject/@2019#egg=MyProject
-e hg+http://hg.myproject.org/MyProject/@v1.0#egg=MyProject
-e hg+http://hg.myproject.org/MyProject/@special_feature#egg=MyProject
-e hg+http://hg.myproject.org/MyProject/#egg=MyProject
-e hg+https://hg.myproject.org/MyProject/#egg=MyProject
-e hg+ssh://hg@myproject.org/MyProject/#egg=MyProject
-e git://git.myproject.org/MyProject.git@master#egg=MyProject
-e git://git.myproject.org/MyProject.git@v1.0#egg=MyProject
-e git://git.myproject.org/MyProject.git@da39a3ee5e6b4b0d3255bfef95601890afd80709#egg=MyProject
-e git://git.myproject.org/MyProject.git#egg=MyProject
-e git+http://git.myproject.org/MyProject/#egg=MyProject
-e git+ssh://git@myproject.org/MyProject/#egg=MyProject
-e svn+http://svn.myproject.org/svn/MyProject/trunk@2019#egg=MyProject
""".splitlines()

class SimpleTest(TestCase):
    def setUp(self):
        self.reqs = [Requirement.from_pip(l) for l in R]
        
    def test_import(self):
        self.assertEqual([r.pip for r in self.reqs], R)
        
    

