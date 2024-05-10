<?php
# On logout
if (isset($_POST['Logout'])) {
    # Expire cookies de manera segura
    setcookie('user', '', time() - 3600, '/', '', true, true);
    setcookie('password', '', time() - 3600, '/', '', true, true);
    setcookie('userId', '', time() - 3600, '/', '', true, true);

    # Redireccionar a la página de inicio
    header("Location: index.php");
    exit;  // Asegurar que se corte la ejecución del script después de redirigir
}
?>
<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="css/style.css">
    <title>Práctica RA3</title>
</head>
<body>
    <header>
        <h1>Developers Awards</h1>
    </header>
    <main>
        <h2><a href="insert_player.php">Add a new player</a></h2>
        <h2><a href="list_players.php">List of players</a></h2>
        <h2><a href="buscador.html">Search a player</a></h2>
    </main>
    <form action="#" method="post" class="menu-form">
        <input type="submit" name="Logout" value="Logout" class="logout-button">
    </form>
    <footer>
        <h4>Puesta en producción segura</h4>
        <p>Please <a href="http://www.donate.co?amount=100&destination=ACMEScouting/">donate</a></p>
    </footer>
</body>
</html>
