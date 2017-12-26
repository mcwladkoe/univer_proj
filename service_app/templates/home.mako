<!DOCTYPE html>
<html lang="en">
<head>
    <title>Home Page</title>
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
    <center><h1>Welcome !</h1></center>
    <center>
        <p> Welcome to the website for booking accommodation for the student exchange program </p>
        % if request.cookies.get('landlord_login'):
            <a class="btn btn-danger" href="${request.route_path('landlord_profile')}">My Profile</a>
        % elif request.cookies.get('student_login'):
            <a class="btn btn-danger" href="${request.route_path('student_profile')}">My Profile</a>
        % else:
            <a class="btn btn-danger" href="${request.route_path('landlord_login')}">Log in as LandLord</a>
            <a class="btn btn-success" href="${request.route_path('student_login')}"}>Log in as Student</a>
        % endif
    </center>
</body>
</html>