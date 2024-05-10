<?php
require_once dirname(__FILE__) . '/private/conf.php';
require_once dirname(__FILE__) . '/private/auth.php';

if (isset($_POST['name']) && isset($_POST['team'])) {
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $team = filter_input(INPUT_POST, 'team', FILTER_SANITIZE_STRING);

    // Modificar jugador o añadir uno nuevo
    if (isset($_GET['id'])) {
        $id = filter_input(INPUT_GET, 'id', FILTER_SANITIZE_NUMBER_INT);
        $stmt = $db->prepare("REPLACE INTO players (playerid, name, team) VALUES (?, ?, ?)");
        $stmt->bindParam(1, $id, PDO::PARAM_INT);
    } else {
        $stmt = $db->prepare("INSERT INTO players (name, team) VALUES (?, ?)");
    }
    $stmt->bindParam(2, $name, PDO::PARAM_STR);
    $stmt->bindParam(3, $team, PDO::PARAM_STR);
    $stmt->execute();
} else if (isset($_GET['id'])) {
    $id = filter_input(INPUT_GET, 'id', FILTER_SANITIZE_NUMBER_INT);
    $stmt = $db->prepare("SELECT name, team FROM players WHERE playerid = ?");
    $stmt->bindParam(1, $id, PDO::PARAM_INT);
    $stmt->execute();
    $row = $stmt->fetch(PDO::FETCH_ASSOC) or die ("modifying a nonexistent player!");
    $name = htmlspecialchars($row['name'], ENT_QUOTES, 'UTF-8');
    $team = htmlspecialchars($row['team'], ENT_QUOTES, 'UTF-8');
}

# Mostrar formulario
?>
<!doctype html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="css/style.css">
        <title>Práctica RA3 - Players list</title>
    </head>
    <body>
        <header>
            <h1>Player</h1>
        </header>
        <main class="player">
            <form action="#" method="post">
                <input type="hidden" name="id" value="<?=$id?>"><br>
                <h3>Player name</h3>
                <textarea name="name"><?= $name ?></textarea><br>
                <h3>Team name</h3>
                <textarea name="team"><?= $team ?></textarea><br>
                <input type="submit" value="Send">
            </form>
            <form action="#" method="post" class="menu-form">
                <a href="index.php">Back to home</a>
                <a href="list_players.php">Back to list</a>
                <input type="submit" name="Logout" value="Logout" class="logout">
            </form>
        </main>
        <footer class="listado">
            <img src="images/logo-iesra-cadiz-color-blanco.png">
            <h4>Puesta en producción segura</h4>
            <p>Please <a href="http://www.donate.co?amount=100&destination=ACMEScouting/"> donate</a></p>
        </footer>
    </body>
</html>
