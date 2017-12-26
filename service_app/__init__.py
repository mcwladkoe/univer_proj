from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from .models import DBSession, Base
from .security import groupfinder

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings,
                          root_factory='.resources.Root')
    config.include('pyramid_mako')
    
        # Security policies
    authn_policy = AuthTktAuthenticationPolicy(
        settings['service_app.secret'], callback=groupfinder,
        hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    
    config.add_route('home', '/')
    config.add_route('landlord_login', '/landlord/login')
    config.add_route('landlord_logout', '/landlord/logout')
    config.add_route('landlord_register', '/landlord/reg')
    config.add_route('landlord_profile', '/landlord/profile')
    config.add_route('landlord_delete', '/landlord/delete')
    config.add_route('landlord_edit', '/landlord/edit')
    config.add_route('landlord_view_pending_orders', '/landlord/pending')
    config.add_route('landlord_view_orders', '/landlord/orders')
    config.add_route('landlord_confirm_order', '/landlord/order/{order_id}/confirm')
    # landlord address
    config.add_route('landlord_address_new', '/landlord/address/add')
    config.add_route('landlord_address_edit', '/landlord/address/{uid}/edit')
    config.add_route('landlord_address_view', '/landlord/address/{uid}/view')
    config.add_route('landlord_address_delete', '/landlord/address/{uid}/delete')
    # student
    config.add_route('student_login', '/student/login')
    config.add_route('student_logout', '/student/logout')
    config.add_route('student_register', '/student/reg')
    config.add_route('student_profile', '/student/profile')
    config.add_route('student_delete', '/student/delete')
    config.add_route('student_edit', '/student/{uid}/edit')
    config.add_route('student_view_pending_orders', '/student/{uid}/pending')
    config.add_route('student_view_orders', '/student/{uid}/orders')

    config.add_route('address_search', '/search')

    # config.add_route('login', '/')
    # config.add_route('login', '/login')
    # config.add_route('logout', '/logout')

    config.add_static_view('deform_static', 'deform:static/')
    config.add_static_view(name='static', path='service_app:static/')
    #config.add_static_view('static', 'static', 'service_app:static/')
    config.scan('.controllers')
    return config.make_wsgi_app()