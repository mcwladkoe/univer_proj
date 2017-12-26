# -*- coding: utf-8 -*-
import colander
import deform.widget

import datetime

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config

from ...models import DBSession, Landlord, LandlordAddress

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

import logging
log = logging.getLogger(__name__)

class LandLordAddressView(colander.MappingSchema):
    address = colander.SchemaNode(colander.String(), title="Address:", validator=colander.Length(max=300))

    number_of_seats = colander.SchemaNode(colander.Integer(), title="Number of Seats:")   
    has_dinner = colander.SchemaNode(colander.Boolean(), title="Dinner:")
    has_language_cources = colander.SchemaNode(colander.Boolean(), title="Langeage Cources:")
    has_transfer = colander.SchemaNode(colander.Boolean(), title="Transfer:")

    additional = colander.SchemaNode(colander.String(), title="Additional:")
    price = colander.SchemaNode(colander.Float(), title="Price:")
    special_price = colander.SchemaNode(colander.Float(), title="Special Price:")
    special_price_min_num = colander.SchemaNode(colander.Integer(), title="Special Price Minimum Order Number:")


class LandLordAddresses(object):
    def __init__(self, request):
        self.request = request

    @property
    def address_form(self):
        schema = LandLordAddressView()
        return deform.Form(schema, buttons=('submit',))

    @property
    def reqts(self):
        return self.address_form.get_widget_resources()

    # @view_config(route_name='customer_list', renderer='../../templates/customer_list.mako', permission='edit')
    # def customer_list(self):
    #     customers = DBSession.query(Customer).order_by(Customer.login)
    #     return dict(title='Customers View', customers=customers)

    @view_config(route_name='landlord_address_new',
                 renderer='../../templates/landlord_address_new.mako')
    def landlord_address_new(self):
        landlord_login = self.request.cookies.get('landlord_login')
        landlord = DBSession.query(Landlord).filter_by(login=landlord_login).first()
        if not landlord:
            response = HTTPFound(self.request.route_url('home'))
            response.delete_cookie('landlord_login')
            return response
        form = self.address_form.render()

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = self.address_form.validate(controls)
            except deform.ValidationFailure as e:
                # Form is NOT valid
                return dict(form=e.render())

            # Add a new customer to the database
            new_address = appstruct['address']
            new_number_of_seats = appstruct['number_of_seats']
            new_has_dinner = appstruct['has_dinner']
            new_has_language_cources = appstruct['has_language_cources']
            new_has_transfer = appstruct['has_transfer']
            new_additional = appstruct['has_transfer']
            new_price = appstruct['price']
            new_special_price = appstruct['special_price']
            new_special_price_min_num = appstruct['special_price_min_num']
            try:
                DBSession.add(LandlordAddress(
                    landlord_id = landlord.uid,
                    address = new_address,
                    number_of_seats = new_number_of_seats,
                    has_dinner = new_has_dinner,
                    has_language_cources = new_has_language_cources,
                    has_transfer = new_has_transfer,
                    additional = new_additional,
                    price = new_price,
                    special_price = new_special_price,
                    special_price_min_num = new_special_price_min_num,
                ))
                DBSession.flush()
            except IntegrityError as e:
                log.exception(e)
                return Response('LandLord Address with this address is already exists.')
            except SQLAlchemyError as e:
                log.exception(e)
                return Response('SQL Error')

            url = self.request.route_url('landlord_profile')
            return HTTPFound(url)

        return dict(form=form)

    @view_config(route_name='landlord_address_edit',
                 renderer='../../templates/landlord_address_edit.mako')
    def landlord_address_edit(self):
        landlord_login = self.request.cookies.get('landlord_login')
        landlord = DBSession.query(Landlord).filter_by(login=landlord_login).first()
        if not landlord:
            response = HTTPFound(self.request.route_url('home'))
            response.delete_cookie('landlord_login')
            return response
        id = self.request.matchdict.get('uid')
        address = DBSession.query(LandlordAddress).join(Landlord)\
            .filter(Landlord.login == landlord_login)\
            .filter(LandlordAddress.uid == id).first()
        if not address:
            return HTTPFound(self.request.route_url('landlord_profile'))

        address_form = self.address_form

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = address_form.validate(controls)
            except deform.ValidationFailure as e:
                return dict(landlord=landlord, form=e.render())

            # Change the content and redirect to the view
            address.address = appstruct['address']
            address.number_of_seats = appstruct['number_of_seats']
            address.has_dinner = appstruct['has_dinner']
            address.has_language_cources = appstruct['has_language_cources']
            address.has_transfer = appstruct['has_transfer']
            address.additional = appstruct['has_transfer']
            address.price = appstruct['price']
            address.special_price = appstruct['special_price']
            address.special_price_min_num = appstruct['special_price_min_num']
            try:
                DBSession.flush()
            except IntegrityError as e:
                log.exception(e)
                return Response('Address with this data is already exists.')

            url = self.request.route_url('landlord_profile')
            return HTTPFound(url)
        form = self.address_form.render(dict(
            uid = address.uid,
            address = address.address,
            number_of_seats = address.number_of_seats,
            has_dinner = address.has_dinner,
            has_language_cources = address.has_language_cources,
            has_transfer = address.has_transfer,
            additional = address.additional,
            price = address.price,
            special_price = address.special_price,
            special_price_min_num = address.special_price_min_num,
            )
        )

        return dict(address=address, form=form)
 

    @view_config(route_name='landlord_address_delete')
    def landlord_address_delete(self):
        landlord_login = self.request.cookies.get('landlord_login')
        landlord = DBSession.query(Landlord).filter_by(login=landlord_login).first()
        if not landlord:
            response = HTTPFound(self.request.route_url('home'))
            response.delete_cookie('landlord_login')
            return response
        id = self.request.matchdict.get('uid')
        address = DBSession.query(LandlordAddress).join(Landlord)\
            .filter(Landlord.login == landlord_login)\
            .filter(LandlordAddress.uid == id).first()
        if not address:
            return HTTPFound(self.request.route_url('landlord_profile'))
        try:
            DBSession.delete(address)
        except SQLAlchemyError:
            return HTTPFound(self.request.route_url('landlord_profile'))
        return HTTPFound(self.request.route_url('landlord_profile'))


    @view_config(route_name='landlord_address_view', renderer='../../templates/landlord_address_view.mako')
    def landlord_address_view(self):
        id = self.request.matchdict.get('uid')
        address = DBSession.query(LandlordAddress)\
            .filter(LandlordAddress.uid == id).first()
        if not address:
            return HTTPFound(self.request.route_url('address_search'))
        return dict(
            request = self.request,
            address = address,
        )