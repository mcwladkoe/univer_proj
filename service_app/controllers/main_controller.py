from pyramid.httpexceptions import HTTPFound
# from pyramid.security import (
#     remember,
#     forget,
#     )
from datetime import datetime

from pyramid.view import (
    view_config,
    view_defaults
    )

# from ..security import (
#     USERS,
#     check_password
# )

from ..models import DBSession, LandlordAddress, Order, Student, Landlord

@view_config(route_name='address_search', renderer='../templates/search.mako')
def address_search(request):
    ## student_login = self.request.cookies.get('student_login')
    ## student = DBSession.query(Student).filter_by(login=student_login).first()
    ## if student:
    ##     return HTTPFound(self.request.route_url('student_profile'))
    ## login_url = request.route_url('student_login')

    query = DBSession.query(LandlordAddress)
    if request.params.get('q'):
        query = query.filter(LandlordAddress.address.contains(request.params['q']))

    return dict(
        results = query.all(),
        request = request,
    )

@view_config(route_name='place_order')
def place_order(request):
    student_login = request.cookies.get('student_login')
    student = DBSession.query(Student).filter_by(login=student_login).first()
    if not student:
        return HTTPFound(request.route_url('student_profile'))
    
    order = Order()
    order.landlord_address_id = request.matchdict['uid']
    order.student_id = student.uid
    order.status = 0
    try:
        order.amount_of_days = int(request.params.get('amount_of_days', 0))
    except ValueError:
        order.amount_of_days = 0
    try:
        order.arrival_date = datetime(request.params.get('arrival_date', 0))
    except:
        order.arrival_date = datetime.now()
    try:
        order.number_of_persons = int(request.params.get('number_of_persons', 0))
    except:
        order.number_of_persons = 0
    order.comment = request.params.get('comment', '')
    try:
        order.total = float(request.params.get('total', ''))
    except:
        order.total = 0
    DBSession.add(order)
    return HTTPFound(request.route_url('student_profile'))

@view_config(route_name='confirm_order')
def confirm_order(request):
    landlord_login = request.cookies.get('landlord_login')
    landlord = DBSession.query(Landlord).filter_by(login=landlord_login).first()
    if not landlord:
        return HTTPFound(request.route_url('landlord_profile'))
    
    order = DBSession.query(Order).filter(Order.uid == request.matchdict['uid']).first()
    if not order:
        return HTTPFound(request.route_url('landlord_profile'))    
    order.status = 1
    DBSession.add(order)
    return HTTPFound(request.route_url('landlord_profile'))
