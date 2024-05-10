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
    <header class="listado">
        <h1>Players list</h1>
    </header>
    <main class="listado">
        <section>
            <ul>
            <?php
            require_once dirname(__FILE__) . '/private/conf.php';
            require_once dirname(__FILE__) . '/private/auth.php';

            // Utilizar sentencias preparadas para las consultas a la base de datos
            $stmt = $db->prepare("SELECT playerid, name, team FROM players ORDER BY playerId DESC");
            $stmt->execute();
            $results = $stmt->fetchAll(PDO::FETCH_ASSOC);

            foreach ($results as $row) {
                $playerId = htmlspecialchars($row['playerid'], ENT_QUOTES, 'UTF-8');
                $name = htmlspecialchars($row['name'], ENT_QUOTES, 'UTF-8');
                $team = htmlspecialchars($row['team'], ENT_QUOTES, 'UTF-8');

                echo "<li>
                        <div>
                            <span>Name: $name</span>
                            <span>Team: $team</span>
                        </div>
                        <div>
                            <a href=\"show_comments.php?id=$playerId\">(show/add comments)</a>
                            <a href=\"insert_player.php?id=$playerId\">(edit player)</a>
                        </div>
                      </li>\n";
            }
            ?>
            </ul>
            <form action="#" method="post" class="menu-form">
                <a href="index.php">Back to home</a>
                <input type="submit" name="Logout" value="Logout" class="logout">
            </form>
        </section>
    </main>
    <footer class="listado">
        <img src="images/logo-iesra-cadiz-color-blanco.png">
        <h4>Puesta en producción segura</h4>
        <p>Please <a href="http://www.donate.co?amount=100&amp;destination=ACMEScouting/"> donate</a></p>
    </footer>
</body>
</html>
