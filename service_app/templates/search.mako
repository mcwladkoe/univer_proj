<!DOCTYPE html>
<html lang="en">
<head>
    <title>Search Page</title>
    <!-- bootstrap -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
</head>
<body>
  <style>
   body {
    background: #F0FFFF; /* Цвет фона */
    color: #483D8B; /* Цвет текста */
   }
  </style>
 </head>
    <center><h1>Search!</h1></center>
    <center>
        <form action="#" method="post">
            <input type="text" name="q" value="${request.params.get('q', '')}">
        </form>
    </center>
    % if len(results) == 0:
        NO RESULTS FOR THIS QUERY
    % endif
    % for i in results:
        <div style="border: 1px solid;border-color: black; margin:2px 1px;" onlick="location.replace('${request.route_path('landlord_address_view', uid=i.uid)}');">
            <div>Name: ${i.landlord.full_name}
            % if i.has_dinner:
                <span class='badge badge-info'>Dinner</span>
            % endif
            % if i.has_language_cources:
                <span class='badge badge-danger'>Language Cources</span>
            % endif
            % if i.has_transfer:
                <span class='badge badge-success'>Transfer</span>
            % endif
            </div>
            <div>Address: ${i.address}</div>
            <div>Phone: ${i.landlord.phone_number}</div>
            <div>Additional: ${i.additional}</div>
            <div>Price: ${i.price}</div>
            <div>Special Price: ${i.special_price}(>${i.special_price_min_num} student(-s))</div>
        </div>
    % endfor
</body>
</html>