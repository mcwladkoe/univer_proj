# -*- coding: utf-8 -*-
import colander
import deform.widget

import datetime

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config

from ...models import DBSession, Student

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

import logging
log = logging.getLogger(__name__)

class StudentView(colander.MappingSchema):
    login = colander.SchemaNode(colander.String(), title="Login:", validator=colander.Length(max=50))
    full_name = colander.SchemaNode(colander.String(), title="Full Name:", validator=colander.Length(max=150))
    email = colander.SchemaNode(colander.String(), title="Email:", validator=colander.Length(max=50))
    phone = colander.SchemaNode(colander.String(), title="Phone:", validator=colander.Length(max=13))


class Students(object):
    def __init__(self, request):
        self.request = request

    @property
    def student_form(self):
        schema = StudentView()
        return deform.Form(schema, buttons=('submit',))

    @property
    def reqts(self):
        return self.student_form.get_widget_resources()

    # @view_config(route_name='customer_list', renderer='../../templates/customer_list.mako', permission='edit')
    # def customer_list(self):
    #     customers = DBSession.query(Customer).order_by(Customer.login)
    #     return dict(title='Customers View', customers=customers)

    @view_config(route_name='student_register',
                 renderer='../../templates/student_register.mako')
    def student_register(self):
        student_login = self.request.cookies.get('student_login')
        student = DBSession.query(Student).filter_by(login=student_login).first()
        if student:
            return HTTPFound(self.request.route_url('student_profile'))
        form = self.student_form.render()

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = self.student_form.validate(controls)
            except deform.ValidationFailure as e:
                # Form is NOT valid
                return dict(form=e.render())

            # Add a new customer to the database
            new_login = appstruct['login']
            new_email = appstruct['email']
            new_full_name = appstruct['full_name']
            new_phone = appstruct['phone']
            try:
                DBSession.add(Student(
                    login = new_login,
                    password = 'master',
                    email = new_email,
                    full_name = new_full_name,
                    phone_number = new_phone,
                ))
                DBSession.flush()
            except IntegrityError as e:
                log.exception(e)
                return Response('Student with this email or login is already exists.')
            except SQLAlchemyError as e:
                log.exception(e)
                return Response('SQL Error')

            # Get the new ID and redirect
            student = DBSession.query(Student).filter_by(login=new_login).one()
            new_uid = student.uid

            url = self.request.route_url('student_profile')
            return HTTPFound(url)

        return dict(form=form)

    @view_config(route_name='student_profile', renderer='../../templates/student_profile.mako')
    def student_profile(self):
        student_login = self.request.cookies.get('student_login')
        student = DBSession.query(Student).filter_by(login=student_login).first()
        if not student:
            response = HTTPFound(self.request.route_url('home'))
            response.delete_cookie('student_login')
            return response
        return dict(student=student)


    @view_config(route_name='student_edit',
                 renderer='../../templates/student_edit.mako')
    def student_edit(self):
        student_login = self.request.cookies.get('student_login')
        student = DBSession.query(Student).filter_by(login=student_login).first()
        if not student:
            response = HTTPFound(self.request.route_url('home'))
            response.delete_cookie('student_login')
            return response
        student_form = self.student_form

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = student_form.validate(controls)
            except deform.ValidationFailure as e:
                return dict(student=student, form=e.render())

            # Change the content and redirect to the view
            student.login = appstruct['login']
            student.email = appstruct['email']
            student.full_name = appstruct['full_name']
            student.phone_number = appstruct['phone']
            try:
                DBSession.flush()
            except IntegrityError as e:
                log.exception(e)
                return Response('Student with this email or login is already exists.')

            url = self.request.route_url('student_profile')
            return HTTPFound(url)
        form = self.student_form.render(dict(
            uid=student.uid,
            login = student.login,
            email = student.email,
            full_name = student.full_name,
            phone = student.phone_number,
            )
        )

        return dict(student=student, form=form)


    @view_config(route_name='student_delete')
    def student_delete(self):
        student_login = self.request.cookies.get('student_login')
        student = DBSession.query(Student).filter_by(login=student_login).first()
        if not student:
            response = HTTPFound(self.request.route_url('home'))
            response.delete_cookie('student_login')
            return response
        try:
            DBSession.delete(student)
        except SQLAlchemyError:
            return HTTPFound(self.request.route_url('student_profile'))
        return HTTPFound(self.request.route_url('home'))
