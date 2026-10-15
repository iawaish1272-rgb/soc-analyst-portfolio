# 02 - Wireshark notes

## Setup
- Tool: Wireshark in my Kali VM
- Capture interface: TODO: eth0 / wlan0
- Captures are not uploaded (see `.gitignore`) because they can contain personal data.

## Display filters I used
| Filter | What it shows | What I saw |
|---|---|---|
| `http` | unencrypted web traffic | TODO |
| `dns` | name lookups | TODO |
| `ip.addr == <ip>` | traffic to or from one host | TODO |
| `http.request.method == "POST"` | form submissions | TODO |

## Exercise: why HTTPS matters
I visited a test site that is made for security practice and used Follow > TCP Stream on the POST request.

- Test site I used: TODO
- What I could read in plain text: TODO
- What this taught me: TODO

## Screenshots
Add your own screenshots to `screenshots/`. Do not show real passwords, personal accounts or your real public IP.
