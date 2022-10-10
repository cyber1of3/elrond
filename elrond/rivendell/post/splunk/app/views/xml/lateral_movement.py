#!/usr/bin/env python3 -tt


def create_lateral_movement_xml(sd):
    with open(sd + "t1210.xml", "w") as t1210xml:
        t1210xml.write(
            '<form version="1.1" stylesheet="mitre.css" theme="dark">\n  <label>T1210: Exploitation of Remote Services</label>\n  <description>If a dashboard panel is not showing, no events exist which satisify that log source for this technique.</description>\n  '
        )
        t1210xml.write(
            '<search id="base">\n    <query>index=* | dedup index | search index=$case_tok$ host=$host_tok$ | table index host</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <search id="mitre_base">\n    <query>index=$case_tok$ host=$host_tok$ mitre_technique!=-</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <search id="dash">\n    <query>| rest /servicesNS/-/-/data/ui/views | search "eai:acl.app"=elrond label=T*</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <fieldset submitButton="false">\n    <input type="checkbox" token="it_tok">\n      <label></label>\n      <search>\n        <query><![CDATA[| gentimes start=-1 | eval it="Toggle MITRE Information"]]></query>\n      </search>\n      <fieldForLabel>it</fieldForLabel>\n      <fieldForValue>it</fieldForValue>\n    </input>\n    <input type="dropdown" token="case_tok" searchWhenChanged="true">\n      <label>Select a Case:</label>\n      <choice value="*">All</choice>\n      <default>*</default>\n      <initialValue>*</initialValue>\n      <fieldForLabel>index</fieldForLabel>\n      <fieldForValue>index</fieldForValue>\n      <search base="base">\n        <query>| dedup index | sort index</query>\n      </search>\n    </input>\n    <input type="dropdown" token="host_tok" searchWhenChanged="true">\n      <label>Select a Host:</label>\n      <choice value="*">All</choice>\n      <default>*</default>\n      <initialValue>*</initialValue>\n      <fieldForLabel>host</fieldForLabel>\n      <fieldForValue>host</fieldForValue>\n      <search base="base">\n        <query>| dedup host | sort host</query>\n      </search>\n    </input>\n    <input type="dropdown" token="mitre_tok" searchWhenChanged="true">\n      <label>Select MITRE Technique:</label>\n      <choice value="*">All</choice>\n      <fieldForLabel>mitre_technique</fieldForLabel>\n      <fieldForValue>mitre_technique</fieldForValue>\n      <search base="mitre_base">\n        <query>| `MITRE_lookup` '
        )
        t1210xml.write(
            '| search id="T1210" | stats count BY mitre_id mitre_technique | sort mitre_id | fields - mitre_id</query>\n      </search>\n      <default>*</default>\n      <prefix>"*</prefix>\n      <suffix>"</suffix>\n      <initialValue>*</initialValue>\n    </input>\n    <input type="time" token="time_tok" searchWhenChanged="true">\n      <label>Select a Time Range:</label>\n      <default>\n        <earliest>-7d@h</earliest>\n        <latest></latest>\n      </default>\n    </input>\n  </fieldset>\n  <row>\n    <panel>\n      '
        )
        t1210xml.write(
            '<html depends="$it_tok$" src="t1210.html"/>\n    </panel>\n  </row>\n  <row>\n    <panel depends="$t1210_memory_panel$">\n      <table>\n        '
        )
        t1210xml.write(
            "<title>Volatile activity in memory</title>\n        <search>\n          <query>index=$case_tok$ host=$host_tok$ mitre_technique!=- mitre_technique=$mitre_tok$ logtype=memory `standard_ports` | `MITRE_lookup` "
        )
        t1210xml.write(
            '| search id="T1210" | stats count values(LocalAddress) AS LocalAddresses values(ForeignAddress) AS ForeignAddresses BY host ProcessName PID LocalPort ForeignPort Protocol State | sort -count | table host ProcessName PID LocalAddresses LocalPort ForeignAddresses ForeignPort Protocol State count</query>\n          <earliest>$time_tok.earliest$</earliest>\n          <latest>$time_tok.latest$</latest>\n          <sampleRatio>1</sampleRatio>\n          <progress>\n            <condition match="\'job.resultCount\' > 0">\n              <set token="t1210_memory_panel">true</set>\n            </condition>\n            <condition>\n              <unset token="t1210_memory_panel"/>\n            </condition>\n          </progress>\n        </search>\n        <option name="count">5</option>\n        <option name="dataOverlayMode">none</option>\n        <option name="drilldown">none</option>\n        <option name="percentagesRow">false</option>\n        <option name="refresh.display">progressbar</option>\n        <option name="rowNumbers">false</option>\n        <option name="totalsRow">false</option>\n        <option name="wrap">false</option>\n      </table>\n    '
        )
        t1210xml.write("\n    </panel>\n  </row>\n</form>")
    with open(sd + "t1534.xml", "w") as t1534xml:  # undetectable
        t1534xml.write(
            '<form version="1.1" stylesheet="mitre.css" theme="dark">\n  <label>T1534: Internal Spearphishing</label>\n  <description>If a dashboard panel is not showing, no events exist which satisify that log source for this technique.</description>\n  '
        )
        t1534xml.write(
            '<search id="base">\n    <query>index=* | dedup index | search index=$case_tok$ host=$host_tok$ | table index host</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <search id="mitre_base">\n    <query>index=$case_tok$ host=$host_tok$ mitre_technique!=-</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <search id="dash">\n    <query>| rest /servicesNS/-/-/data/ui/views | search "eai:acl.app"=elrond label=T*</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <fieldset submitButton="false">\n    <input type="checkbox" token="it_tok">\n      <label></label>\n      <search>\n        <query><![CDATA[| gentimes start=-1 | eval it="Toggle MITRE Information"]]></query>\n      </search>\n      <fieldForLabel>it</fieldForLabel>\n      <fieldForValue>it</fieldForValue>\n    </input>\n    <input type="dropdown" token="case_tok" searchWhenChanged="true">\n      <label>Select a Case:</label>\n      <choice value="*">All</choice>\n      <default>*</default>\n      <initialValue>*</initialValue>\n      <fieldForLabel>index</fieldForLabel>\n      <fieldForValue>index</fieldForValue>\n      <search base="base">\n        <query>| dedup index | sort index</query>\n      </search>\n    </input>\n    <input type="dropdown" token="host_tok" searchWhenChanged="true">\n      <label>Select a Host:</label>\n      <choice value="*">All</choice>\n      <default>*</default>\n      <initialValue>*</initialValue>\n      <fieldForLabel>host</fieldForLabel>\n      <fieldForValue>host</fieldForValue>\n      <search base="base">\n        <query>| dedup host | sort host</query>\n      </search>\n    </input>\n    <input type="dropdown" token="mitre_tok" searchWhenChanged="true">\n      <label>Select MITRE Technique:</label>\n      <choice value="*">All</choice>\n      <fieldForLabel>mitre_technique</fieldForLabel>\n      <fieldForValue>mitre_technique</fieldForValue>\n      <search base="mitre_base">\n        <query>| `MITRE_lookup` '
        )
        t1534xml.write(
            '| search id="T1534" | stats count BY mitre_id mitre_technique | sort mitre_id | fields - mitre_id</query>\n      </search>\n      <default>*</default>\n      <prefix>"*</prefix>\n      <suffix>"</suffix>\n      <initialValue>*</initialValue>\n    </input>\n    <input type="time" token="time_tok" searchWhenChanged="true">\n      <label>Select a Time Range:</label>\n      <default>\n        <earliest>-7d@h</earliest>\n        <latest></latest>\n      </default>\n    </input>\n  </fieldset>\n  <row>\n    <panel>\n      '
        )
        t1534xml.write(
            '<html depends="$it_tok$" src="t1534.html"/>\n    </panel>\n  </row>\n  <row>\n    <panel>\n      <html src="na.html"/>\n    </panel>\n  </row>\n</form>\n'
        )
    with open(sd + "t1570.xml", "w") as t1570xml:
        t1570xml.write(
            '<form version="1.1" stylesheet="mitre.css" theme="dark">\n  <label>T1570: Lateral Tool Transfer</label>\n  <description>If a dashboard panel is not showing, no events exist which satisify that log source for this technique.</description>\n  '
        )
        t1570xml.write(
            '<search id="base">\n    <query>index=* | dedup index | search index=$case_tok$ host=$host_tok$ | table index host</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <search id="mitre_base">\n    <query>index=$case_tok$ host=$host_tok$ mitre_technique!=-</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <search id="dash">\n    <query>| rest /servicesNS/-/-/data/ui/views | search "eai:acl.app"=elrond label=T*</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <fieldset submitButton="false">\n    <input type="checkbox" token="it_tok">\n      <label></label>\n      <search>\n        <query><![CDATA[| gentimes start=-1 | eval it="Toggle MITRE Information"]]></query>\n      </search>\n      <fieldForLabel>it</fieldForLabel>\n      <fieldForValue>it</fieldForValue>\n    </input>\n    <input type="dropdown" token="case_tok" searchWhenChanged="true">\n      <label>Select a Case:</label>\n      <choice value="*">All</choice>\n      <default>*</default>\n      <initialValue>*</initialValue>\n      <fieldForLabel>index</fieldForLabel>\n      <fieldForValue>index</fieldForValue>\n      <search base="base">\n        <query>| dedup index | sort index</query>\n      </search>\n    </input>\n    <input type="dropdown" token="host_tok" searchWhenChanged="true">\n      <label>Select a Host:</label>\n      <choice value="*">All</choice>\n      <default>*</default>\n      <initialValue>*</initialValue>\n      <fieldForLabel>host</fieldForLabel>\n      <fieldForValue>host</fieldForValue>\n      <search base="base">\n        <query>| dedup host | sort host</query>\n      </search>\n    </input>\n    <input type="dropdown" token="mitre_tok" searchWhenChanged="true">\n      <label>Select MITRE Technique:</label>\n      <choice value="*">All</choice>\n      <fieldForLabel>mitre_technique</fieldForLabel>\n      <fieldForValue>mitre_technique</fieldForValue>\n      <search base="mitre_base">\n        <query>| `MITRE_lookup` '
        )
        t1570xml.write(
            '| search id="T1570" | stats count BY mitre_id mitre_technique | sort mitre_id | fields - mitre_id</query>\n      </search>\n      <default>*</default>\n      <prefix>"*</prefix>\n      <suffix>"</suffix>\n      <initialValue>*</initialValue>\n    </input>\n    <input type="time" token="time_tok" searchWhenChanged="true">\n      <label>Select a Time Range:</label>\n      <default>\n        <earliest>-7d@h</earliest>\n        <latest></latest>\n      </default>\n    </input>\n  </fieldset>\n  <row>\n    <panel>\n      '
        )
        t1570xml.write(
            '<html depends="$it_tok$" src="t1570.html"/>\n    </panel>\n  </row>\n  <row>\n    <panel depends="$t1570_memory_panel$">\n      <table>\n        '
        )
        t1570xml.write(
            "<title>Volatile activity in memory</title>\n        <search>\n          <query>index=$case_tok$ host=$host_tok$ mitre_technique!=- mitre_technique=$mitre_tok$ logtype=memory `standard_ports` | `MITRE_lookup` "
        )
        t1570xml.write(
            '| search id="T1570" | stats count values(LocalAddress) AS LocalAddresses values(ForeignAddress) AS ForeignAddresses BY host ProcessName PID LocalPort ForeignPort Protocol State | sort -count | table host ProcessName PID LocalAddresses LocalPort ForeignAddresses ForeignPort Protocol State count</query>\n          <earliest>$time_tok.earliest$</earliest>\n          <latest>$time_tok.latest$</latest>\n          <sampleRatio>1</sampleRatio>\n          <progress>\n            <condition match="\'job.resultCount\' > 0">\n              <set token="t1570_memory_panel">true</set>\n            </condition>\n            <condition>\n              <unset token="t1570_memory_panel"/>\n            </condition>\n          </progress>\n        </search>\n        <option name="count">5</option>\n        <option name="dataOverlayMode">none</option>\n        <option name="drilldown">none</option>\n        <option name="percentagesRow">false</option>\n        <option name="refresh.display">progressbar</option>\n        <option name="rowNumbers">false</option>\n        <option name="totalsRow">false</option>\n        <option name="wrap">false</option>\n      </table>\n    </panel>\n  </row>\n  <row>\n    <panel depends="$t1570_journal_panel$">\n      <table>\n        '
        )
        t1570xml.write(
            "<title>Windows-based file activity</title>\n        <search>\n          <query>index=$case_tok$ host=$host_tok$ mitre_technique!=- mitre_technique=$mitre_tok$ logtype=journal | `MITRE_lookup` "
        )
        t1570xml.write(
            '| search id="T1570" | `make_fileinfo` | table index host mitre_id mitre_technique LastWriteTime Filepath Filename Fileext</query>\n          <earliest>$time_tok.earliest$</earliest>\n          <latest>$time_tok.latest$</latest>\n          <sampleRatio>1</sampleRatio>\n          <progress>\n            <condition match="\'job.resultCount\' > 0">\n              <set token="t1570_journal_panel">true</set>\n            </condition>\n            <condition>\n              <unset token="t1570_journal_panel"/>\n            </condition>\n          </progress>\n        </search>\n        <option name="count">5</option>\n        <option name="dataOverlayMode">none</option>\n        <option name="drilldown">none</option>\n        <option name="percentagesRow">false</option>\n        <option name="refresh.display">progressbar</option>\n        <option name="rowNumbers">false</option>\n        <option name="totalsRow">false</option>\n        <option name="wrap">false</option>\n      </table>\n        '
        )
        t1570xml.write(
            '\n    </panel>\n  </row>\n  <row>\n    <panel depends="$t1570_usb_panel$">\n      <table>\n        '
        )
        t1570xml.write(
            '<title>USB activity</title>\n        <search>\n          <query>index=$case_tok$ host=$host_tok$ mitre_technique=$mitre_tok$ `usb_out`</query>\n          <earliest>$time_tok.earliest$</earliest>\n          <latest>$time_tok.latest$</latest>\n          <sampleRatio>1</sampleRatio>\n          <progress>\n            <condition match="\'job.resultCount\' > 0">\n              <set token="t1570_usb_panel">true</set>\n            </condition>\n            <condition>\n              <unset token="t1570_usb_panel"/>\n            </condition>\n          </progress>\n        </search>\n        <option name="count">5</option>\n        <option name="dataOverlayMode">none</option>\n        <option name="drilldown">none</option>\n        <option name="percentagesRow">false</option>\n        <option name="refresh.display">progressbar</option>\n        <option name="rowNumbers">false</option>\n        <option name="totalsRow">false</option>\n        <option name="wrap">false</option>\n      </table>\n    </panel>\n  </row>\n  <row>\n    <panel depends="$t1570_audit_panel$">\n      <table>\n        '
        )
        t1570xml.write(
            "<title>Audit file entries</title>\n        <search>\n          <query>index=$case_tok$ host=$host_tok$ mitre_technique!=- mitre_technique=$mitre_tok$ logtype=audit | `MITRE_lookup` "
        )
        t1570xml.write(
            '| search id="T1570" | `audit_assignments` | table index host mitre_id mitre_technique audit_file LastAccessTime Filename Filesize Entropy SHA256 | fillnull value=-</query>\n          <earliest>$time_tok.earliest$</earliest>\n          <latest>$time_tok.latest$</latest>\n          <sampleRatio>1</sampleRatio>\n          <progress>\n            <condition match="\'job.resultCount\' > 0">\n              <set token="t1570_audit_panel">true</set>\n            </condition>\n            <condition>\n              <unset token="t1570_audit_panel"/>\n            </condition>\n          </progress>\n        </search>\n        <option name="count">5</option>\n        <option name="dataOverlayMode">none</option>\n        <option name="drilldown">none</option>\n        <option name="percentagesRow">false</option>\n        <option name="rowNumbers">false</option>\n        <option name="totalsRow">false</option>\n        <option name="wrap">false</option>\n      </table>\n    '
        )
        t1570xml.write("</panel>\n  </row>\n</form>")
    with open(sd + "t1563.xml", "w") as t1563xml:
        t1563xml.write(
            '<form version="1.1" stylesheet="mitre.css" theme="dark">\n  <label>T1563: Remote Service Session Hijacking</label>\n  <description>If a dashboard panel is not showing, no events exist which satisify that log source for this technique.</description>\n  '
        )
        t1563xml.write(
            '<search id="base">\n    <query>index=* | dedup index | search index=$case_tok$ host=$host_tok$ | table index host</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <search id="mitre_base">\n    <query>index=$case_tok$ host=$host_tok$ mitre_technique!=-</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <search id="dash">\n    <query>| rest /servicesNS/-/-/data/ui/views | search "eai:acl.app"=elrond label=T*</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <fieldset submitButton="false">\n    <input type="checkbox" token="it_tok">\n      <label></label>\n      <search>\n        <query><![CDATA[| gentimes start=-1 | eval it="Toggle MITRE Information"]]></query>\n      </search>\n      <fieldForLabel>it</fieldForLabel>\n      <fieldForValue>it</fieldForValue>\n    </input>\n    <input type="dropdown" token="case_tok" searchWhenChanged="true">\n      <label>Select a Case:</label>\n      <choice value="*">All</choice>\n      <default>*</default>\n      <initialValue>*</initialValue>\n      <fieldForLabel>index</fieldForLabel>\n      <fieldForValue>index</fieldForValue>\n      <search base="base">\n        <query>| dedup index | sort index</query>\n      </search>\n    </input>\n    <input type="dropdown" token="host_tok" searchWhenChanged="true">\n      <label>Select a Host:</label>\n      <choice value="*">All</choice>\n      <default>*</default>\n      <initialValue>*</initialValue>\n      <fieldForLabel>host</fieldForLabel>\n      <fieldForValue>host</fieldForValue>\n      <search base="base">\n        <query>| dedup host | sort host</query>\n      </search>\n    </input>\n    <input type="dropdown" token="mitre_tok" searchWhenChanged="true">\n      <label>Select MITRE Technique:</label>\n      <choice value="*">All</choice>\n      <fieldForLabel>mitre_technique</fieldForLabel>\n      <fieldForValue>mitre_technique</fieldForValue>\n      <search base="mitre_base">\n        <query>| `MITRE_lookup` '
        )
        t1563xml.write(
            '| search id="T1563" | stats count BY mitre_id mitre_technique | sort mitre_id | fields - mitre_id</query>\n      </search>\n      <default>*</default>\n      <prefix>"*</prefix>\n      <suffix>"</suffix>\n      <initialValue>*</initialValue>\n    </input>\n    <input type="time" token="time_tok" searchWhenChanged="true">\n      <label>Select a Time Range:</label>\n      <default>\n        <earliest>-7d@h</earliest>\n        <latest></latest>\n      </default>\n    </input>\n  </fieldset>\n  <row>\n    <panel>\n      '
        )
        t1563xml.write(
            '<html depends="$it_tok$" src="t1563.html"/>\n    </panel>\n  </row>\n  <row>\n    <panel depends="$t1563_memory_panel$">\n      <table>\n        '
        )
        t1563xml.write(
            "<title>Volatile activity in memory</title>\n        <search>\n          <query>index=$case_tok$ host=$host_tok$ mitre_technique!=- mitre_technique=$mitre_tok$ logtype=memory `standard_ports` | `MITRE_lookup` "
        )
        t1563xml.write(
            '| search id="T1563" | stats count values(LocalAddress) AS LocalAddresses values(ForeignAddress) AS ForeignAddresses BY host ProcessName PID LocalPort ForeignPort Protocol State | sort -count | table host ProcessName PID LocalAddresses LocalPort ForeignAddresses ForeignPort Protocol State count</query>\n          <earliest>$time_tok.earliest$</earliest>\n          <latest>$time_tok.latest$</latest>\n          <sampleRatio>1</sampleRatio>\n          <progress>\n            <condition match="\'job.resultCount\' > 0">\n              <set token="t1563_memory_panel">true</set>\n            </condition>\n            <condition>\n              <unset token="t1563_memory_panel"/>\n            </condition>\n          </progress>\n        </search>\n        <option name="count">5</option>\n        <option name="dataOverlayMode">none</option>\n        <option name="drilldown">none</option>\n        <option name="percentagesRow">false</option>\n        <option name="refresh.display">progressbar</option>\n        <option name="rowNumbers">false</option>\n        <option name="totalsRow">false</option>\n        <option name="wrap">false</option>\n      </table>\n    </panel>\n  </row>\n  <row>\n    <panel depends="$t1563_timeline_panel$">\n      <table>\n        '
        )
        t1563xml.write(
            "<title>Timeline activity</title>\n        <search>\n          <query>index=$case_tok$ host=$host_tok$ mitre_technique!=- mitre_technique=$mitre_tok$ logtype=timeline | `MITRE_lookup` "
        )
        t1563xml.write(
            '| search id="T1563" | stats count BY index host mitre_id mitre_technique LastWriteTime source_long Artefact Message | sort 0 -count LastWriteTime | fields - count</query>\n          <earliest>$time_tok.earliest$</earliest>\n          <latest>$time_tok.latest$</latest>\n          <sampleRatio>1</sampleRatio>\n          <progress>\n            <condition match="\'job.resultCount\' > 0">\n              <set token="t1563_timeline_panel">true</set>\n            </condition>\n            <condition>\n              <unset token="t1563_timeline_panel"/>\n            </condition>\n          </progress>\n        </search>\n        <option name="count">5</option>\n        <option name="dataOverlayMode">none</option>\n        <option name="drilldown">none</option>\n        <option name="percentagesRow">false</option>\n        <option name="refresh.display">progressbar</option>\n        <option name="rowNumbers">false</option>\n        <option name="totalsRow">false</option>\n        <option name="wrap">false</option>\n      </table>\n    </panel>\n  </row>\n  <row>\n    <panel depends="$t1563_journal_panel$">\n      <table>\n        '
        )
        t1563xml.write(
            "<title>Windows-based file activity</title>\n        <search>\n          <query>index=$case_tok$ host=$host_tok$ mitre_technique!=- mitre_technique=$mitre_tok$ logtype=journal | `MITRE_lookup` "
        )
        t1563xml.write(
            '| search id="T1563" | `make_fileinfo` | table index host mitre_id mitre_technique LastWriteTime Filepath Filename Fileext</query>\n          <earliest>$time_tok.earliest$</earliest>\n          <latest>$time_tok.latest$</latest>\n          <sampleRatio>1</sampleRatio>\n          <progress>\n            <condition match="\'job.resultCount\' > 0">\n              <set token="t1563_journal_panel">true</set>\n            </condition>\n            <condition>\n              <unset token="t1563_journal_panel"/>\n            </condition>\n          </progress>\n        </search>\n        <option name="count">5</option>\n        <option name="dataOverlayMode">none</option>\n        <option name="drilldown">none</option>\n        <option name="percentagesRow">false</option>\n        <option name="refresh.display">progressbar</option>\n        <option name="rowNumbers">false</option>\n        <option name="totalsRow">false</option>\n        <option name="wrap">false</option>\n      </table>\n    </panel>\n  </row>\n  <row>\n    <panel depends="$t1563_audit_panel$">\n      <table>\n        '
        )
        t1563xml.write(
            "<title>Audit file entries</title>\n        <search>\n          <query>index=$case_tok$ host=$host_tok$ mitre_technique!=- mitre_technique=$mitre_tok$ logtype=audit | `MITRE_lookup` "
        )
        t1563xml.write(
            '| search id="T1563" | `audit_assignments` | table index host mitre_id mitre_technique audit_file LastAccessTime Filename Filesize Entropy SHA256 | fillnull value=-</query>\n          <earliest>$time_tok.earliest$</earliest>\n          <latest>$time_tok.latest$</latest>\n          <sampleRatio>1</sampleRatio>\n          <progress>\n            <condition match="\'job.resultCount\' > 0">\n              <set token="t1563_audit_panel">true</set>\n            </condition>\n            <condition>\n              <unset token="t1563_audit_panel"/>\n            </condition>\n          </progress>\n        </search>\n        <option name="count">5</option>\n        <option name="dataOverlayMode">none</option>\n        <option name="drilldown">none</option>\n        <option name="percentagesRow">false</option>\n        <option name="rowNumbers">false</option>\n        <option name="totalsRow">false</option>\n        <option name="wrap">false</option>\n      </table>\n    '
        )
        t1563xml.write("\n    </panel>\n  </row>\n</form>")
    with open(sd + "t1021.xml", "w") as t1021xml:
        t1021xml.write(
            '<form version="1.1" stylesheet="mitre.css" theme="dark">\n  <label>T1021: Remote Services</label>\n  <description>If a dashboard panel is not showing, no events exist which satisify that log source for this technique.</description>\n  '
        )
        t1021xml.write(
            '<search id="base">\n    <query>index=* | dedup index | search index=$case_tok$ host=$host_tok$ | table index host</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <search id="mitre_base">\n    <query>index=$case_tok$ host=$host_tok$ mitre_technique!=-</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <search id="dash">\n    <query>| rest /servicesNS/-/-/data/ui/views | search "eai:acl.app"=elrond label=T*</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <fieldset submitButton="false">\n    <input type="checkbox" token="it_tok">\n      <label></label>\n      <search>\n        <query><![CDATA[| gentimes start=-1 | eval it="Toggle MITRE Information"]]></query>\n      </search>\n      <fieldForLabel>it</fieldForLabel>\n      <fieldForValue>it</fieldForValue>\n    </input>\n    <input type="dropdown" token="case_tok" searchWhenChanged="true">\n      <label>Select a Case:</label>\n      <choice value="*">All</choice>\n      <default>*</default>\n      <initialValue>*</initialValue>\n      <fieldForLabel>index</fieldForLabel>\n      <fieldForValue>index</fieldForValue>\n      <search base="base">\n        <query>| dedup index | sort index</query>\n      </search>\n    </input>\n    <input type="dropdown" token="host_tok" searchWhenChanged="true">\n      <label>Select a Host:</label>\n      <choice value="*">All</choice>\n      <default>*</default>\n      <initialValue>*</initialValue>\n      <fieldForLabel>host</fieldForLabel>\n      <fieldForValue>host</fieldForValue>\n      <search base="base">\n        <query>| dedup host | sort host</query>\n      </search>\n    </input>\n    <input type="dropdown" token="mitre_tok" searchWhenChanged="true">\n      <label>Select MITRE Technique:</label>\n      <choice value="*">All</choice>\n      <fieldForLabel>mitre_technique</fieldForLabel>\n      <fieldForValue>mitre_technique</fieldForValue>\n      <search base="mitre_base">\n        <query>| `MITRE_lookup` '
        )
        t1021xml.write(
            '| search id="T1021" | stats count BY mitre_id mitre_technique | sort mitre_id | fields - mitre_id</query>\n      </search>\n      <default>*</default>\n      <prefix>"*</prefix>\n      <suffix>"</suffix>\n      <initialValue>*</initialValue>\n    </input>\n    <input type="time" token="time_tok" searchWhenChanged="true">\n      <label>Select a Time Range:</label>\n      <default>\n        <earliest>-7d@h</earliest>\n        <latest></latest>\n      </default>\n    </input>\n  </fieldset>\n  <row>\n    <panel>\n      '
        )
        t1021xml.write(
            '<html depends="$it_tok$" src="t1021.html"/>\n    </panel>\n  </row>\n  <row>\n    <panel depends="$t1021_memory_panel$">\n      <table>\n        '
        )
        t1021xml.write(
            "<title>Volatile activity in memory</title>\n        <search>\n          <query>index=$case_tok$ host=$host_tok$ mitre_technique!=- mitre_technique=$mitre_tok$ logtype=memory `standard_ports` | `MITRE_lookup` "
        )
        t1021xml.write(
            '| search id="T1021" | stats count values(LocalAddress) AS LocalAddresses values(ForeignAddress) AS ForeignAddresses BY host ProcessName PID LocalPort ForeignPort Protocol State | sort -count | table host ProcessName PID LocalAddresses LocalPort ForeignAddresses ForeignPort Protocol State count</query>\n          <earliest>$time_tok.earliest$</earliest>\n          <latest>$time_tok.latest$</latest>\n          <sampleRatio>1</sampleRatio>\n          <progress>\n            <condition match="\'job.resultCount\' > 0">\n              <set token="t1021_memory_panel">true</set>\n            </condition>\n            <condition>\n              <unset token="t1021_memory_panel"/>\n            </condition>\n          </progress>\n        </search>\n        <option name="count">5</option>\n        <option name="dataOverlayMode">none</option>\n        <option name="drilldown">none</option>\n        <option name="percentagesRow">false</option>\n        <option name="refresh.display">progressbar</option>\n        <option name="rowNumbers">false</option>\n        <option name="totalsRow">false</option>\n        <option name="wrap">false</option>\n      </table>\n    </panel>\n  </row>\n  <row>\n    <panel depends="$t1021_timeline_panel$">\n      <table>\n        '
        )
        t1021xml.write(
            "<title>Timeline activity</title>\n        <search>\n          <query>index=$case_tok$ host=$host_tok$ mitre_technique!=- mitre_technique=$mitre_tok$ logtype=timeline | `MITRE_lookup` "
        )
        t1021xml.write(
            '| search id="T1021" | stats count BY index host mitre_id mitre_technique LastWriteTime source_long Artefact Message | sort 0 -count LastWriteTime | fields - count</query>\n          <earliest>$time_tok.earliest$</earliest>\n          <latest>$time_tok.latest$</latest>\n          <sampleRatio>1</sampleRatio>\n          <progress>\n            <condition match="\'job.resultCount\' > 0">\n              <set token="t1021_timeline_panel">true</set>\n            </condition>\n            <condition>\n              <unset token="t1021_timeline_panel"/>\n            </condition>\n          </progress>\n        </search>\n        <option name="count">5</option>\n        <option name="dataOverlayMode">none</option>\n        <option name="drilldown">none</option>\n        <option name="percentagesRow">false</option>\n        <option name="refresh.display">progressbar</option>\n        <option name="rowNumbers">false</option>\n        <option name="totalsRow">false</option>\n        <option name="wrap">false</option>\n      </table>\n    </panel>\n  </row>\n  <row>\n    <panel depends="$t1021_evt_panel$">\n      <table>\n        '
        )
        t1021xml.write(
            "<title>Windows event log activity</title>\n        <search>\n          <query>index=$case_tok$ host=$host_tok$ mitre_technique!=- mitre_technique=$mitre_tok$ logtype=evt | `MITRE_lookup` "
        )
        t1021xml.write(
            '| search id="T1021" | eval TargetSids=mvappend(TargetSid,TargetUserSid) | table SystemTime host Computer Channel EventID LogonType SubjectUserName SubjectUserSid DisplayName WorkstationName TargetSids</query>\n          <earliest>$time_tok.earliest$</earliest>\n          <latest>$time_tok.latest$</latest>\n          <sampleRatio>1</sampleRatio>\n          <progress>\n            <condition match="\'job.resultCount\' > 0">\n              <set token="t1021_evt_panel">true</set>\n            </condition>\n            <condition>\n              <unset token="t1021_evt_panel"/>\n            </condition>\n          </progress>\n        </search>\n        <option name="count">5</option>\n        <option name="dataOverlayMode">none</option>\n        <option name="drilldown">none</option>\n        <option name="percentagesRow">false</option>\n        <option name="refresh.display">progressbar</option>\n        <option name="rowNumbers">false</option>\n        <option name="totalsRow">false</option>\n        <option name="wrap">false</option>\n      </table>\n    '
        )
        t1021xml.write("</panel>\n  </row>\n</form>")
    with open(sd + "t1080.xml", "w") as t1080xml:  # undetectable
        t1080xml.write(
            '<form version="1.1" stylesheet="mitre.css" theme="dark">\n  <label>T1080: Taint Shared Content</label>\n  <description>If a dashboard panel is not showing, no events exist which satisify that log source for this technique.</description>\n  '
        )
        t1080xml.write(
            '<search id="base">\n    <query>index=* | dedup index | search index=$case_tok$ host=$host_tok$ | table index host</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <search id="mitre_base">\n    <query>index=$case_tok$ host=$host_tok$ mitre_technique!=-</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <search id="dash">\n    <query>| rest /servicesNS/-/-/data/ui/views | search "eai:acl.app"=elrond label=T*</query>\n    <earliest>$time_tok.earliest$</earliest>\n    <latest>$time_tok.latest$</latest>\n  </search>\n  <fieldset submitButton="false">\n    <input type="checkbox" token="it_tok">\n      <label></label>\n      <search>\n        <query><![CDATA[| gentimes start=-1 | eval it="Toggle MITRE Information"]]></query>\n      </search>\n      <fieldForLabel>it</fieldForLabel>\n      <fieldForValue>it</fieldForValue>\n    </input>\n    <input type="dropdown" token="case_tok" searchWhenChanged="true">\n      <label>Select a Case:</label>\n      <choice value="*">All</choice>\n      <default>*</default>\n      <initialValue>*</initialValue>\n      <fieldForLabel>index</fieldForLabel>\n      <fieldForValue>index</fieldForValue>\n      <search base="base">\n        <query>| dedup index | sort index</query>\n      </search>\n    </input>\n    <input type="dropdown" token="host_tok" searchWhenChanged="true">\n      <label>Select a Host:</label>\n      <choice value="*">All</choice>\n      <default>*</default>\n      <initialValue>*</initialValue>\n      <fieldForLabel>host</fieldForLabel>\n      <fieldForValue>host</fieldForValue>\n      <search base="base">\n        <query>| dedup host | sort host</query>\n      </search>\n    </input>\n    <input type="dropdown" token="mitre_tok" searchWhenChanged="true">\n      <label>Select MITRE Technique:</label>\n      <choice value="*">All</choice>\n      <fieldForLabel>mitre_technique</fieldForLabel>\n      <fieldForValue>mitre_technique</fieldForValue>\n      <search base="mitre_base">\n        <query>| `MITRE_lookup` '
        )
        t1080xml.write(
            '| search id="T1080" | stats count BY mitre_id mitre_technique | sort mitre_id | fields - mitre_id</query>\n      </search>\n      <default>*</default>\n      <prefix>"*</prefix>\n      <suffix>"</suffix>\n      <initialValue>*</initialValue>\n    </input>\n    <input type="time" token="time_tok" searchWhenChanged="true">\n      <label>Select a Time Range:</label>\n      <default>\n        <earliest>-7d@h</earliest>\n        <latest></latest>\n      </default>\n    </input>\n  </fieldset>\n  <row>\n    <panel>\n      '
        )
        t1080xml.write(
            '<html depends="$it_tok$" src="t1080.html"/>\n    </panel>\n  </row>\n  <row>\n    <panel>\n      <html src="na.html"/>\n    </panel>\n  </row>\n</form>\n'
        )
