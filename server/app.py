from sanic import response

def attach(sanic):
    
    @sanic.route('/')
    async def root(request):
        return response.text('Hello There!')
