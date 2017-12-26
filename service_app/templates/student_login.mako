<!DOCTYPE html>
<html lang="en">
<head>
    <title>Student Login</title>
    <!-- bootstrap -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
</head>
<body>
    <center><h1>Login as Student</h1></center>
    % if message:
        <span class="col-sm-offset-2 col-sm-3 col-md-offset-2 col-md-3 col-lg-offset-2 col-lg-3">
            <h3 class="badge badge-danger" style="font-size:15px;">
                ${message}
            </h3>
        </span>
    % endif

    <form action="${url}" method="post">
        <input type="hidden" name="came_from" value="${came_from}"/>
        <div class="input-group">
            <label class="control-label col-sm-1" for="login">Username</label>
            <input type="text" id="login" class="form-control col-sm-2" name="login" value="${login}"/><br/>
        </div>
        <br/>
        <div class="input-group">
            <label class="control-label col-sm-1" for="password">Password</label>
            <input type="password" class="form-control col-sm-2" id="password" name="password" value="${password}"/><br/>
        </div>
        <br/>
        <div class="btn-group col-sm-offset-2 col-sm-3 col-md-offset-2 col-md-3 col-lg-offset-2 col-lg-3">
            <a class="btn btn-success" href="${request.route_path('student_register')}">Register</a>
            <input class="btn btn-default" type="submit" name="form.submitted" value="Log In"/>
        </div>
    </form>
</body>
</html>