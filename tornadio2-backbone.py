from tornadio2.conn import event, SocketConnection

class BackboneConnection(SocketConnection):
	@event
	def sync(self, method, model, options):
		print(method, model, options)
		return model

	def on_create(self, model, options):
		raise NotImplementedError

	def on_read(self, model, options):
		raise NotImplementedError

	def on_update(self, model, options):
		raise NotImplementedError

	def on_delete(self, model, options):
		raise NotImplementedError
