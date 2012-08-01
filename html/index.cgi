#!/bin/sh
echo Content-Type: text/html
echo

TRAP_DIR="/data/snapdragon/traps"

cd ${TRAP_DIR}

cat /www/sites/css/ipncore.css

echo "{snapDragon}<br>"
echo "[ <a href=/snapdragon/logic/>Program Logic</a> ]"
echo "[ <a href=/snapdragon/>Show NEW traps</a> ]"
echo "[ <a href=/snapdragon/ackindex.cgi>Show ACKnowledged traps</a> ]"
echo "[ <a href=/snapdragon/ackall.cgi>ACKnowledge ALL TRAPS</a> ]<p>"
echo "Traps are escalated to snapdragon-escalate  if not acknowledged within 15 minutes<p>"

	for trap in *trap; do {
	if [ -f "${trap}" ]; then {
	echo "{snapDragon Trap} <b>${trap}</b>"
	echo "[ <a href=/snapdragon/ack.php?DIR=${TRAP_DIR}&TRAP=${trap}>acknowledge</a> ]"
	echo "<br>-------<pre>"
	cat ${trap}
	echo "</pre>---"
	echo "<p>"
	}; fi
	}; done

#cat /data/ufoix-style/footer.inc
