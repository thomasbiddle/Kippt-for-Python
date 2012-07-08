<h1>Python Wrapper for Kippt</h1>

<p>
This is a Python wrapper for <a href="https://kippt.com/developers">Kippt's API</a>. It has all of the features of the <a href="http://haythem.github.com/Kippt.NET/">C# library</a>, plus some extras - and is still in development.

<h3>Documenation</h3>
<p>
The file is heavily commented on documentation - so just take a look if you need any further clarification. I tried to keep as close to the C# library as possible.

<pre>
Python 2.7.3 (default, May  9 2012, 23:42:16)
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import kippt_wrapper as kippt
>>> myClient = kippt.user('yourUsername','yourAPITokenHere')
>>> myClient.checkAuth()
True
>>> myClient.getLists()
({u'total_count': 4, u'limit': 0, u'offset': 0}, [{u'rss_url': u'https://kippt.com/feed/urinsan3/GQg00z0tSLJHGBj8PXrKouVtuos1/my-list', u'updated': u'1339296452', u'created': u'1339284366', u'title': u'My List', u'slug': u'my-list', u'id': 55284, u'resource_uri': u'/api/lists/55284/'}, {u'rss_url': u'https://kippt.com/feed/urinsan3/GQg00z0tSLJHGBj8PXrKouVtuos1/read-later', u'updated': u'1339093234', u'created': u'1339093234', u'title': u'Read Later', u'slug': u'read-later', u'id': 54828, u'resource_uri': u'/api/lists/54828/'}, {u'rss_url': u'https://kippt.com/feed/urinsan3/GQg00z0tSLJHGBj8PXrKouVtuos1/inbox', u'updated': u'1338946730', u'created': u'1338945940', u'title': u'Inbox', u'slug': u'inbox', u'id': 54432, u'resource_uri': u'/api/lists/54432/'}, {u'rss_url': u'https://kippt.com/feed/urinsan3/GQg00z0tSLJHGBj8PXrKouVtuos1/new-list-name', u'updated': u'1339093060', u'created': u'1338945940', u'title': u'new list name', u'slug': u'new-list-name', u'id': 54433, u'resource_uri': u'/api/lists/54433/'}])
>>> myClient.getList(55284)
{u'rss_url': u'https://kippt.com/feed/urinsan3/GQg00z0tSLJHGBj8PXrKouVtuos1/my-list', u'updated': u'1339296452', u'created': u'1339284366', u'title': u'My List', u'slug': u'my-list', u'id': 55284, u'resource_uri': u'/api/lists/55284/'}
>>> myClient.getClips()
({u'total_count': 2, u'limit': 0, u'offset': 0}, [{u'url_domain': u'google.com', u'updated': u'1339296441', u'title': u'Google', u'url': u'http://www.google.com/', u'notes': u'Testing Notes!', u'created': u'1339296431', u'list': u'/api/lists/55284/', u'is_starred': False, u'id': 2028643, u'resource_uri': u'/api/clips/2028643/'}, {u'url_domain': u'android-ui-utils.googlecode.com', u'updated': u'1339284376', u'title': u'Android Asset Studio', u'url': u'http://android-ui-utils.googlecode.com/hg/asset-studio/dist/index.html', u'notes': u'', u'created': u'1339281459', u'list': u'/api/lists/55284/', u'is_starred': False, u'id': 2028518, u'resource_uri': u'/api/clips/2028518/'}])
>>> myClient.getClip(2028643)
{u'url_domain': u'google.com', u'updated': u'1339296441', u'title': u'Google', u'url': u'http://www.google.com/', u'notes': u'Testing Notes!', u'created': u'1339296431', u'list': u'/api/lists/55284/', u'is_starred': False, u'id': 2028643, u'resource_uri': u'/api/clips/2028643/'}
>>> myClient.search('android')
({u'total_count': 1, u'offset': 0, u'limit': 0, u'query': u'android'}, [{u'url_domain': u'android-ui-utils.googlecode.com', u'updated': u'1339284376', u'title': u'Android Asset Studio', u'url': u'http://android-ui-utils.googlecode.com/hg/asset-studio/dist/index.html', u'notes': u'', u'created': u'1339281459', u'list': u'/api/lists/55284/', u'is_starred': False, u'id': 2028518, u'resource_uri': u'/api/clips/2028518/'}])
>>> u.getListCollab(55284)
[{u'username': u'thomasbiddle', u'avatar_url': u'https://secure.gravatar.com/avatar/a5cb7b8b8594fa9483d89c020e79014f/?default=https%3A%2F%2Fkippt.com%2Fstatic%2Fimg%2Fdefault-avatar.jpg&amp;s=160', u'id': 16993, u'resource_uri': u'/api/users/16993/'}]
</pre> 