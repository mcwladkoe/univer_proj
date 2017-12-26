<!DOCTYPE html>
<html lang="en">
<head>
    <title>
        Create Landlord Address
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
    </title>
    <link rel="stylesheet"
          href="${request.static_url('deform:static/css/bootstrap.min.css')}"
          type="text/css" media="screen" charset="utf-8"/>
    <link rel="stylesheet"
          href="${request.static_url('deform:static/css/form.css')}"
          type="text/css"/>
    <script src="${request.static_url('deform:static/scripts/jquery-2.0.3.min.js')}"
            type="text/javascript"></script>
    <script src="${request.static_url('deform:static/scripts/bootstrap.min.js')}"
            type="text/javascript"></script>
</head>
<body>
<style>
</style>
    ##<a class="btn" href="${request.route_url('customer_list')}">
    ##    Клиенты
    ##</a>
    <center>
        <h1>
            View Address
        </h1>
    </center>
    <style>
        .form-control {
            width: 400px !important
        }
        
        body {
            margin-left: 30px
        }
    </style>
    <div>
        <div>Name: ${address.landlord.full_name}
        % if address.has_dinner:
            <span class='badge badge-info'>Dinner</span>
        % endif
        % if address.has_language_cources:
            <span class='badge badge-danger'>Language Cources</span>
        % endif
        % if address.has_transfer:
            <span class='badge badge-success'>Transfer</span>
        % endif
        </div>
        <div>Address: ${address.address}</div>
        <div>Phone: ${address.landlord.phone_number}</div>
        <div>Additional: ${address.additional}</div>
        <div>Price: ${address.price}</div>
        <div>Special Price: ${address.special_price}(>${address.special_price_min_num} student(-s))</div>
    </div>
    % if request.cookies.get('student_login'):
        <form action="${request.route_path('place_order', uid=address.uid)}" method="post">
            Amount of days: <input type="number" name="amount_of_days" value="${request.params.get('amount_of_days', 0)}">
            Arrival Day: <input type="number" name="datetime" value="${request.params.get('arrival_date', 0)}">
            Number of persons: <input type="number" name="number_of_persons" value="${request.params.get('number_of_persons', 0)}">
            Comment: <input type="number" name="comment" value="${request.params.get('comment', 0)}">
            <button type="submit">Submit</button>
        </form>
    % else:
        Login as student to place order
    % endif
    <a class="btn btn-default" href="${request.route_path('address_search')}">
        Back
    </a>
</body>
</html>