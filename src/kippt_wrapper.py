import json, ast, urllib, requests, sys

class user:
	# Example:
	# client = kippt_wrapper.user('myUsername','kjsdfklj2lhg323423klj42')
	def __init__(self, username, apitoken):
		self.username = username
		self.apitoken = apitoken
		self.header = {'X-Kippt-Username': username, 'X-Kippt-API-Token': apitoken, 'X-Kippt-Client': 'Kippt-Python-Wrapper,me@ThomasBiddle.com,https://github.com/thomasbiddle/Kippt-Projects', 'content-type': 'application/vnd.kippt.20120609+json'}
	
	# Example:
	# user.checkAuth()
	#
	# Return True on success and False on failure.
	def checkAuth(self):
		r = requests.get('https://kippt.com/api/account/', headers=self.header)
		if r.status_code is 200: return True
		else: return False
	
	# Example:
	# meta, lists = user.getLists(offset = 5)
	# meta, lists = user.getLists(50, 5) # (limit, offset)
	# meta, lists = user.getLists()
	# x = meta['total_count']
	# y = lists['title']
	# 
	# Available values in meta:
	# total_count, limit, offset
	# Available values in each list:
	# rss_url, updated, title, created, slug, id, resource_uri
	#
	# Returns data on success, and false on failure.
	def getLists(self, limit = 0, offset = 0):	
		url = 'https://kippt.com/api/lists?limit=' + str(limit) + '&offset=' + str(offset)
		r = requests.get(url, headers=self.header)
		if r.status_code is 200:
			return r.json['meta'], r.json['objects']
		else: return False, False
	
	# Example:
	# myList = user.getList(54433)
	# x = myList['title']
	#
	# Available values in list:
	# rss_url, updated, title, created, slug, id, resource_uri
	#
	# Returns data on success, and false on failure.
	def getList(self, id):
		r = requests.get('https://kippt.com/api/lists/' + str(id), headers=self.header)
		if r.status_code is 200: 
			return r.json
		else: return False
		
	# Example:
	# myClips = user.getClips()
	# myClips = user.getClips(54332, 20, 5) # (listID, limit, offset)
	# myClicps = user.getClips(limit = 20)
	#
	# Available values in meta:
	# total_count, limit, offset
	# Available values in clip:
	# id, url, title, list, notes, is_starred, url_domain, created, updated, resource_uri
	#
	# Returns data on success, and false on failure.
	def getClips(self, listID = None, limit = 0, offset = 0):
		url = 'https://kippt.com/api/clips?limit=' + str(limit) + '&offset=' + str(offset)
		if not listID is None: url = url + '&list=' + str(listID)
		r = requests.get(url, headers=self.header)
		if r.status_code is 200:
			return r.json['meta'], r.json['objects']
		else: return False, False
		
	# Example:
	# myClip = user.getClip(2027593)
	# x = myClip['title']
	#
	# Available values in clip:
	# id, url, title, list, notes, is_starred, url_domain, created, updated, resource_uri
	#
	# Returns data on success, and false on failure.	
	def getClip(self, id):
		r = requests.get('https://kippt.com/api/clips/' + str(id), headers=self.header)
		if r.status_code is 200: 
			return r.json
		else: return False
	# Example:
	# mySearch = user.search("Programming")
	#
	# Available values in meta:
	# total_count, limit, offset
	# Available values in clip:
	# id, url, title, list, notes, is_starred, url_domain, created, updated, resource_uri
	#
	# Returns data on success, and false on failure.
	def search(self, query, limit = 0, offset = 0):
		query = urllib.quote_plus(query)
		r = requests.get('https://kippt.com/api/search/clips/?q=' + query + '&limit=' + str(limit) + '&offset=' + str(offset), headers=self.header)
		if r.status_code is 200:
			return r.json['meta'], r.json['objects']
		else: return False, False
		
	#######################################
	# Extra on top of C# Library ( Will continue to add to this )
	#######################################
	# Examples:
	# user.addClip('www.kippt.com')
	# user.addClip('www.kippt.com',title="My Title!")
	# user.addClip('www.kippt.com',1234,starred="true",notes='My Notes!')
	#
	# Will return Status Code 201 on success.
	def addClip(self, url, listID=0, title = None, starred = None, notes = None, ): 	
		clipdata = {'url': url, 'list': '/api/lists/' + str(listID)}
		if not title is None: clipdata['title'] = title
		if not starred is None: clipdata['is_starred'] = starred
		if not notes is None: clipdata['notes'] = notes
		r = requests.post('https://kippt.com/api/clips/', data=json.dumps(clipdata), headers=self.header)
		return r.status_code
		
# Testing purposes ( Faster than using the interpreter every time ;) )	
if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "Looks like your forgot something, or added too much!"
		print "Please start the script like so: python kippt_wrapper.py <username> <API_Token>"
	else:
		client = user(sys.argv[1],sys.argv[2])


		
