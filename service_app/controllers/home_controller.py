
from pyramid.view import (
    view_config,
    view_defaults
    )
    
from pyramid.httpexceptions import HTTPFound

from ..models import DBSession, Landlord

@view_config(route_name='home', renderer='../templates/home.mako')
def home(request):
    # landlord_login = request.cookies.get('landlord_login')
    # landlord = DBSession.query(Landlord).filter_by(login=landlord_login).first()
    # if landlord:
    #     return HTTPFound(request.route_url('landlord_profile'))
    return dict(
        request=request,
    )
