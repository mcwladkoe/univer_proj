# -*- coding: utf-8 -*-
import colander
import deform.widget

import datetime

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config

from ...models import DBSession, Landlord, LandlordAddress, Order

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

import logging
log = logging.getLogger(__name__)

class LandLordView(colander.MappingSchema):
    login = colander.SchemaNode(colander.String(), title="Login:", validator=colander.Length(max=50))
    full_name = colander.SchemaNode(colander.String(), title="Full Name:", validator=colander.Length(max=150))
    email = colander.SchemaNode(colander.String(), title="Email:", validator=colander.Length(max=50))
    phone = colander.SchemaNode(colander.String(), title="Phone:", validator=colander.Length(max=13))


class LandLords(object):
    def __init__(self, request):
        self.request = request

    @property
    def landlord_form(self):
        schema = LandLordView()
        return deform.Form(schema, buttons=('submit',))

    @property
    def reqts(self):
        return self.landlord_form.get_widget_resources()

    # @view_config(route_name='customer_list', renderer='../../templates/customer_list.mako', permission='edit')
    # def customer_list(self):
    #     customers = DBSession.query(Customer).order_by(Customer.login)
    #     return dict(title='Customers View', customers=customers)

    @view_config(route_name='landlord_register',
                 renderer='../../templates/landlord_register.mako')
    def landlord_register(self):
        landlord_login = self.request.cookies.get('landlord_login')
        landlord = DBSession.query(Landlord).filter_by(login=landlord_login).first()
        if landlord:
            return HTTPFound(self.request.route_url('landlord_profile'))
        form = self.landlord_form.render()

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = self.landlord_form.validate(controls)
            except deform.ValidationFailure as e:
                # Form is NOT valid
                return dict(form=e.render())

            # Add a new customer to the database
            new_login = appstruct['login']
            new_email = appstruct['email']
            new_full_name = appstruct['full_name']
            new_phone = appstruct['phone']
            try:
                DBSession.add(Landlord(
                    login = new_login,
                    password = 'master',
                    email = new_email,
                    full_name = new_full_name,
                    phone_number = new_phone
                ))
                DBSession.flush()
            except IntegrityError as e:
                log.exception(e)
                return Response('LandLord with this email or login is already exists.')
            except SQLAlchemyError as e:
                log.exception(e)
                return Response('SQL Error')

            # Get the new ID and redirect
            landlord = DBSession.query(Landlord).filter_by(login=new_login).one()
            new_uid = landlord.uid

            url = self.request.route_url('landlord_profile')
            return HTTPFound(url)

        return dict(form=form)

    @view_config(route_name='landlord_profile', renderer='../../templates/landlord_profile.mako')
    def landlord_profile(self):
        landlord_login = self.request.cookies.get('landlord_login')
        landlord = DBSession.query(Landlord).filter_by(login=landlord_login).first()
        if not landlord:
            response = HTTPFound(self.request.route_url('home'))
            response.delete_cookie('landlord_login')
            return response
        orders = DBSession.query(Order).join(LandlordAddress).join(Landlord)\
            .filter(Landlord.login == landlord_login)
        pending_orders = orders.filter(Order.status == 0)
        return dict(
            landlord=landlord,
            orders=orders,
            pending_orders=pending_orders,
        )


    @view_config(route_name='landlord_edit',
                 renderer='../../templates/landlord_edit.mako')
    def landlord_edit(self):
        landlord_login = self.request.cookies.get('landlord_login')
        landlord = DBSession.query(Landlord).filter_by(login=landlord_login).first()
        if not landlord:
            response = HTTPFound(self.request.route_url('home'))
            response.delete_cookie('landlord_login')
            return response
        landlord_form = self.landlord_form

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = landlord_form.validate(controls)
            except deform.ValidationFailure as e:
                return dict(landlord=landlord, form=e.render())

            # Change the content and redirect to the view
            landlord.login = appstruct['login']
            landlord.email = appstruct['email']
            landlord.full_name = appstruct['full_name']
            landlord.phone_number = appstruct['phone']
            try:
                DBSession.flush()
            except IntegrityError as e:
                log.exception(e)
                return Response('LandLord with this email or login is already exists.')

            url = self.request.route_url('landlord_profile')
            return HTTPFound(url)
        form = self.landlord_form.render(dict(
            uid=landlord.uid,
            login = landlord.login,
            email = landlord.email,
            full_name = landlord.full_name,
            phone = landlord.phone_number,
            )
        )

        return dict(landlord=landlord, form=form)
 

    @view_config(route_name='landlord_delete')
    def landlord_delete(self):
        landlord_login = self.request.cookies.get('landlord_login')
        landlord = DBSession.query(Landlord).filter_by(login=landlord_login).first()
        if not landlord:
            response = HTTPFound(self.request.route_url('home'))
            response.delete_cookie('landlord_login')
            return response
        try:
            DBSession.delete(landlord)
        except SQLAlchemyError:
            return HTTPFound(self.request.route_url('landlord_profile'))
        return HTTPFound(self.request.route_url('home'))
