from django.db import models
import django

S = (
    ('svn','Subversion'),
    ('git','Git'),
    ('hg','Mercurial'),
    ('bzr','Bazaar'),
    ('ssh','SSH'),
    ('sftp','Secure FTP'),
)

class Requirement(models.Model):
    package = models.CharField(max_length=255,help_text='Install by either name, URL, or file')
    editable = models.BooleanField(default=False,help_text='Adds the -e flag for editing')
    find_links = models.BooleanField(default=False,help_text='Adds additional indexes')
    index = models.BooleanField(default=False,help_text='Removes the use of PyPI')
    scheme = models.CharField(max_length=4,choices=S)
    version = models.CharField(max_length=255,blank=True,null=True,help_text='Commit hash or a tag name')
    egg = models.CharField(max_length=255,blank=True,null=True,help_text='Install path')
    
    def __unicode__(self):
        t = ''
        if self.egg:
            t += self.egg
        else:
            t += self.package
        if self.version:
            t += ' @%s' % self.version
        return t
    
    def to_pip(self):
        if self.editable:
            yield '-e '
        if self.find_links:
            yield '--find-links '
        if self.index:
            yield '--index '
        if self.scheme:
            # svn+ssh://.../@rev#egg=package
            yield '%s+%s%s%s' % (self.scheme, self.package,
                               self.version and '@%s' % self.version or '',
                               self.egg and '#egg=%s' % self.egg or '')
        else:
            # django==1.1.1
            yield '%s%s' % \
                (self.package, self.version and '==%s' % self.version or '')
    
    @property
    def pip(self):
        return ' '.join(self.to_pip())
    
    @classmethod
    def from_pip(cls, s):
        s = s.strip()
        if not s: return
        a = s.split()
        k = {}
        if '-e' in a: k['editable'] = True
        if '--find-links' in a: k['find_links'] = True
        if '--index' in a: k['index'] = True
        # look for schema
        print s
        for v,_ in S:
            if s.find(' %s' % v)>-1:
                k['scheme'] = v
                k['package'] = s.split('%s+'%v)[1].split('#')[0].split('@')[0]
                if s.find('#egg=')>-1:
                    k['egg'] = s.split('#egg=')[1].split('@')[0]
                if s.find('@')>-1:
                    k['version'] = s.split('@')[-1].split('#egg=')[0]
                break
        if not 'package' in k:
            # no schema matches, either name, URL or file
            k['package'] = s.split('==')[0]
            if s.find('==')>-1:
                k['version'] = s.split('==')[1]
        return cls.objects.create(**k)
    

if not Requirement.objects.count():
    Requirement.objects.create(
        package = 'django==%s' % '.'.join(map(str,django.VERSION[:3]))
    )
