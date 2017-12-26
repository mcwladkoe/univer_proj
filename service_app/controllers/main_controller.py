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

from ..models import DBSession, LandlordAddress

@view_config(route_name='address_search', renderer='../templates/search.mako')
def address_search(request):
    ## student_login = self.request.cookies.get('student_login')
    ## student = DBSession.query(Student).filter_by(login=student_login).first()
    ## if student:
    ##     return HTTPFound(self.request.route_url('student_profile'))
    ## login_url = request.route_url('student_login')

    query = DBSession.query(LandlordAddress)
    if request.params.get('q'):
        query = query.filet(LandlordAddress.address.contains(request.params['q']))

    return dict(
        results = query.all(),
        request = request,
    )
