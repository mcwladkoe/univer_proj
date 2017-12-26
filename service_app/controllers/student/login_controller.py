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

from ...models import DBSession, Student

class StudentViews(object):
    def __init__(self, request):
        self.request = request
        self.student_id = request.cookies.get('student_id')

    @view_config(route_name='student_login', renderer='../../templates/student_login.mako')
    def student_login(self):
        request = self.request
        student_login = self.request.cookies.get('student_login')
        student = DBSession.query(Student).filter_by(login=student_login).first()
        if student:
            return HTTPFound(self.request.route_url('student_profile'))
        login_url = request.route_url('student_login')
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
            student = DBSession.query(Student).filter_by(login=login).first()
            if not student:
                message = 'Failed login'
            elif password == student.password:
                response = HTTPFound(location=came_from)
                response.set_cookie('student_login', value=login, max_age=31536000) # max_age = year
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

    @view_config(route_name='student_logout')
    def student_logout(self):
        request = self.request
        # headers = forget(request)
        url = request.route_url('home')
        response =  HTTPFound(location=url)
        response.delete_cookie('student_login')
        return response