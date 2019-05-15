<!DOCTYPE HTML>
<html>
<head>
  <link rel="icon" href="RUatWorkIcon.png" type="image/gif" sizes="16x16">
  <title>Logged out</title>
</head>

<body background="background.png">

<?php
session_start();
session_unset();
session_destroy();
?>

<center>
<h1>You have logged out.</h1><br><br>
<h2>Please close this browser tab or sign in again.</h2><br><br>
<form action="index.html">
<input type="submit" value="Sign in again">
</form>

</center>
</body>
</html>
