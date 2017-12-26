from pyramid.httpexceptions import HTTPFound
# from pyramid.security import (
#     remember,
#     forget,
#     )

from pyramid.view import (
    view_config,
    view_defaults
    )

# from ..security import (
#     USERS,
#     check_password
# )

from ...models import DBSession, Landlord

class LandLordlViews(object):
    def __init__(self, request):
        self.request = request
        self.landlord_id = request.cookies.get('landlord_id')

    @view_config(route_name='landlord_login', renderer='../../templates/landlord_login.mako')
    def landlord_login(self):
        request = self.request
        landlord_login = self.request.cookies.get('landlord_login')
        landlord = DBSession.query(Landlord).filter_by(login=landlord_login).first()
        if landlord:
            return HTTPFound(self.request.route_url('landlord_profile'))
        login_url = request.route_url('landlord_login')
        referrer = request.url
        if referrer == login_url:
            referrer = '/'  # never use login form itself as came_from
        came_from = request.route_url('home')
        message = ''
        login = ''
        password = ''
        if 'form.submitted' in request.params:
            login = request.params['login']
            password = request.params['password']
            # if check_password(password, USERS.get(login)):
            landlord = DBSession.query(Landlord).filter_by(login=login).first()
            if not landlord:
                message = 'Failed login'
            elif password == landlord.password:
                response = HTTPFound(location=came_from)
                response.set_cookie('landlord_login', value=login, max_age=31536000) # max_age = year
                return response
            message = 'Failed login'
        return dict(
            name='Login',
            message=message,
            url=login_url,
            came_from=came_from,
            login=login,
            password=password,
        )

    @view_config(route_name='landlord_logout')
    def landlord_logout(self):
        request = self.request
        # headers = forget(request)
        url = request.route_url('home')
        response =  HTTPFound(location=url)
        response.delete_cookie('landlord_login')
        return response