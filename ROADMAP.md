# pastegram
pastebin. but better
somewhere in between github gists and pastebin
good looking UI and UX :eyes:
simple links and profile page etc

# Features
- CRUD api for user functionality
- CRUD api for new pastes
- anonymous user endpoint for temporary pastes (no filename - url is randomly generated)

# later
- tags for pastes ( grouped by language )
- search for pastes based on tags
- following and feed functionality

# endpoints

## user
GET		/api/:username		gets user information (profile page stuff)
POST	/api/:username		make new user (body will contain schema data)
UPDATE	/api/:username		update values
DELETE 	/api/:username		move user to deleted collection for 30 days before deleting

## pastes
GET		/api/:username/pastes		get all pastes by that particular user
GET		/api/:username/:filename	get that particular paste by that user
POST	/api/paste					make new paste under that user
DELETE	/api/:username/:filename	delete paste

GET		(24 hr limit) /api/paste/:randomid		for anonymous pastes which expire in 24 hours

## auth
POST /auth/register
POST /auth/login
