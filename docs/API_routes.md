# pastegram

- pastebin. but better
- somewhere in between github gists and pastebin and instagram
- good looking UI and UX :eyes:
- simple links and profile page etc

# needed for MVP

- CRUD api for user functionality
- CRUD api for new pastes
- anonymous user endpoint for temporary pastes (no filename - url is randomly generated)

# later

- tags for pastes ( grouped by language )
- search for pastes based on tags
- following and feed functionality

# endpoints

\* -> authorized access only

## user

- GET&ensp;&ensp;&ensp;&ensp;&ensp;/api/:username&ensp;&ensp;&ensp;&ensp;gets user information (profile page stuff)
- POST&ensp;&ensp;&ensp;&ensp;/api/:username&ensp;&ensp;&ensp;&ensp;make new user (body will contain schema data)
- \*UPDATE&ensp;&ensp;/api/:username&ensp;&ensp;&ensp; update values
- \*DELETE&ensp;&ensp;/api/:username&ensp;&ensp;&ensp;&ensp;move user to deleted collection for 30 days before deleting

## pastes

- GET /api/:username/pastes &ensp;&ensp;get all pastes by that particular user
- GET /api/:username/:filename &ensp;&ensp;&ensp;get that particular paste by that user
- POST /api/paste&ensp;&ensp;&ensp;&ensp;make new paste under that user
- DELETE /api/:username/:filename&ensp;&ensp;&ensp;&ensp;delete paste
- GET (24 hr limit) /api/paste/:randomid &ensp;&ensp;&ensp; for anonymous pastes which expire in 24 hours

## auth

- POST /auth/register
- POST /auth/login

JWT tokens are used for authentication and authorization
