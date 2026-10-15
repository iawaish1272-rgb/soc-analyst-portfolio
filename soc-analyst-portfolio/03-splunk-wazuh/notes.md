# 03 - Splunk and Wazuh notes

## Splunk Free
- Data I loaded: TODO (sample data / my own syslog)
- What I learned about the interface: TODO

### Searches I ran
| Search | Purpose | Result |
|---|---|---|
| `index=main error` | find events containing "error" | TODO |
| `index=main error \| stats count` | count those events | TODO |
| `index=main (failed OR failure)` | find failures | TODO |
| `index=main "Failed password" \| rex "from (?<src_ip>\d+\.\d+\.\d+\.\d+)" \| stats count by src_ip \| sort - count` | which IPs fail logins most | TODO |

TODO: add a screenshot of one search and one dashboard panel to `screenshots/`.

## Wazuh (basics)
- What Wazuh is, in my own words: TODO
- What I did with it (install, agent, alerts): TODO
- Difference between Splunk and Wazuh as I understand it: TODO
