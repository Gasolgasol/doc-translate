# routes.py
def includeme(config):
	config.add_route('default', '/')
	config.add_route('primero', '/primero')
	config.add_route('getprimero', '/getprimero')
	config.add_route('main', '/main')
	config.add_route('store_pdf_view', '/store_pdf_view')
	config.add_route('wrong_format', '/wrong_format')
	config.add_route('draft', '/draftdraft')
	config.add_route('download_view', '/download/{server_name}/{name}/{bool}')
	config.add_route('info', '/api/v1/')
	config.add_route('good_upload', '/good_upload')
	config.add_route('register', '/api/v1/accounts')
	config.add_route('profile_detail', '/api/v1/accounts/{username}')
	config.add_route('login', '/api/v1/accounts/login')
	config.add_route('logout', '/api/v1/accounts/logout')
	config.add_route('tasks', '/api/v1/accounts/{username}/tasks')
	config.add_route('task_detail', '/api/v1/accounts/{username}/tasks/{id}')