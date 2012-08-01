#!/bin/sh
echo Content-Type: text/html
echo

TRAP_DIR="/data/snapdragon/traps"

cd ${TRAP_DIR}

cat /www/sites/css/ipncore.css
echo "{snapDragon} "
echo "[ <a href=/snapdragon/>Show NEW Traps</a> ]<p>"

	for trap in *ack; do {
	echo "{snapDragon Trap} <b>${trap}</b>"
	echo "<br>-------<pre>"
	cat ${trap}
	echo "</pre>---"
	echo "<p>"
	}; done
#cat /data/ufoix-style/footer.inc
