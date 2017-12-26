<!DOCTYPE html>
<html lang="en">
<head>
    <title>Student Profile</title>
    <!-- bootstrap -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
</head>
<body>
    <center><h1>Student Profile</h1></center>
    <div class="col-sm-10 offset-sm-1 col-md-10 offset-md-1 col-lg-10 offset-lg-1">
        <div>
            <b>Full Name</b>: ${student.full_name}
        </div>
        <div>
            <b>Login</b>: ${student.login}
        </div>
        <div>
            <b>Email</b>: ${student.email}
        </div>
        <div>
            <b>Phone</b>: ${student.phone_number}
        </div>
        <a href="#" class="btn btn-warning">Edit</a>
        <a href="${request.route_path('student_logout')}" class="btn btn-primary">Log Out</a>
        <a href="${request.route_path('student_delete')}" class="btn btn-danger">Delete</a>
    </div>

</body>
</html>