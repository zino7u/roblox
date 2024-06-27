<!-- create_webhook.php -->

<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Eingaben aus dem Formular holen
    $username = $_POST['username'];
    $message = $_POST['message'];

    // Hier könntest du die Daten in eine temporäre Speicherung (Datei oder Datenbank) schreiben
    // Beispiel: Einfügen in eine Datei
    $file = 'temp_data.txt';
    $data = "Benutzername: $username\nNachricht: $message\n\n";
    file_put_contents($file, $data, FILE_APPEND);

    // Erzeuge einen temporären Link für 30 Minuten
    $timestamp = time() + (30 * 60); // Aktuelle Zeit + 30 Minuten
    $temporaryLink = "http://deine-domain.com/webhook_receiver.php?timestamp=$timestamp";

    // Hier kannst du die temporäre Speicherung aktualisieren oder speichern

    // Gib den temporären Link aus
    echo "Dein temporärer Webhook-Link: <a href='$temporaryLink' target='_blank'>$temporaryLink</a>";
}
?>
