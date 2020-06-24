def overwrite_current_key(self):
	import secrets, json

	with open(self.setup_file_name) as f:
		data = json.load(f)
	with open(self.setup_file_name, 'w') as f:
		data['key'] = secrets.token_hex(64)
		json.dump(data, f)
