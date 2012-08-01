<?php
include "/www/sites/css/ipncore.css";
?>

<b>SnapDragon LOGIC</b>
<p>
SnapDragon receives raw snmp traps as defined per-switch<br>
i.e. snmp-server enable traps bgp
<p>
traps which match keywords.page are sent to techstaff and oncall aliases
and are escalated if not acknowledged after 15 minutes;
<br>
<pre>
<b>keywords.page:</b><br>
<?php
include "/data/snapdragon/etc/keywords.page"
?>
</pre>

traps which don't match keywords.page but match keywords.exclude
are discarded
<br>
<pre>
<b>keywords.exclude:</b><br>
<?php
include "/data/snapdragon/etc/keywords.exclude"
?>
</pre>

traps which match neither keywords.page nor keywords.exclude are
emailed to techstaff alias only, and are never escalated.
