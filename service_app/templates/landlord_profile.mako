<!DOCTYPE html>
<html lang="en">
<head>
    <title>LandLord Profile</title>
    <!-- bootstrap -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
</head>
<body>
    <center><h1>LandLord Profile</h1></center>
    <div class="col-sm-10 offset-sm-1 col-md-10 offset-md-1 col-lg-10 offset-lg-1">
        <div>
            <b>Full Name</b>: ${landlord.full_name}
            ##% if landlord.has_dinner:
            ##    <span class='badge badge-info'>Dinner</span>
            ##% endif
            ##% if landlord.has_language_cources:
            ##    <span class='badge badge-danger'>Language Cources</span>
            ##% endif
            ##% if landlord.has_transfer:
            ##    <span class='badge badge-success'>Transfer</span>
            ##% endif
        </div>
        <div>
            <b>Login</b>: ${landlord.login}
        </div>
        <div>
            <b>Email</b>: ${landlord.email}
        </div>
        <div>
            <b>Phone</b>: ${landlord.phone_number or ''}
        </div>
        <div>
            <b>Addresses</b>:<br/>
            <a href="${request.route_path('landlord_address_new')}" class="btn btn-warning">Add Address</a><br/>
            <table class="table table-striped table-bordered">
                <head>
                    <tr>
                        <td>Address</td>
                        <td>Number of seats</td>
                        <td>Has Dinner</td>
                        <td>Language Cources</td>
                        <td>Has Transfer</td>
                        <td>Additional</td>
                        <td>Price</td>
                        <td>Special Price</td>
                        <td>Special Price Minimum Order Number</td>
                        <td>Actions</td>
                    </tr>
                </head>
            % for address in landlord.addresses:
                <tr>
                    <td>${address.address}</td>
                    <td>${address.number_of_seats}</td>
                    <td>${address.has_dinner}</td>
                    <td>${address.has_language_cources}</td>
                    <td>${address.has_transfer}</td>
                    <td>${address.additional}</td>
                    <td>${address.price}</td>
                    <td>${address.special_price}</td>
                    <td>${address.special_price_min_num}</td>
                    <td width="170px;">
                        <a class="btn btn-sm btn-danger" href="${request.route_path('landlord_address_delete', uid=address.uid)}">Delete</a>
                        <a class="btn btn-sm btn-success" href="${request.route_path('landlord_address_edit', uid=address.uid)}">Edit</a>
                    </td>
                </tr>
            % endfor
            </table>
        </div>
        <a href="${request.route_path('landlord_edit')}" class="btn btn-warning">Edit</a>
        <a href="${request.route_path('landlord_logout')}" class="btn btn-primary">Log Out</a>
        <a href="${request.route_path('landlord_delete')}" class="btn btn-danger">Delete</a>
    </div>

</body>
</html>