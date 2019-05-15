<!DOCTYPE HTML>
<html>
<head>
  <link rel="icon" href="RUatWorkIcon.png" type="image/gif" sizes="16x16">
  <title>RU@Work</title>
</head>
<body background="background.png">

<?php
session_start();

$hostname = "localhost";
$user_name = $_POST["username"];
$SESSION['user_name'] = $user_name;
$pass_word = $_POST["password"];
$SESSION['pass_word'] = $pass_word;
$db = "dataBaseName";

$dbconnect=mysqli_connect($hostname,$user_name,$pass_word,$db);

if ($dbconnect->connect_error) {
  die("Database connection failed: " . $dbconnect->connect_error);
}

?>


<form action="logout.php">
<input type="submit" value="Logout">
</form>



<?php
echo "<center><h1>Work time of {$user_name}</h1></center>";
echo "<center><p>Most recent first.</p></center>";
?>

<table id="tunnit" border="1" align="center" bgcolor="#FFFFFF">
<tr>
  <td>Date</td>
  <td>At work?</td>
  <td>Hours</td>
  <td></td>
  <td>Minutes</td>
</tr>

<?php

$query = mysqli_query($dbconnect, "select id, time, status, timestampdiff(minute, time, (select time from {$user_name} t2 where t1.id < t2.id order by t1.id desc limit 1)) as diff from {$user_name} t1 order by id desc")
   or die (mysqli_error($dbconnect));

while ($row = mysqli_fetch_array($query)) {
  if ($row['status'] == 1):
    $status = "Present for";
  else:
    $status = "Absent for";
  endif;
  $hours = $row['diff'] / 60;
  $rounded = number_format($hours, 2);
  echo
   "<tr>
    <td>{$row['time']}</td>
    <td>{$status}</td>
    <td>{$rounded} hours</td>
    <td>OR</td>
    <td>{$row['diff']} minutes</td>
   </tr>\n";

}

?>
</table>
</body>
</html>
