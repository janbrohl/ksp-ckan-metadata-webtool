# Metadata-Webtool

[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks!-%F0%9F%A6%89-1EAEDB.svg)](https://saythanks.io/to/janbrohl)


## Current Status

You can try it and the generated data *should* be good for submitting but the user interface is not great yet.


## Original Mission

What's currently specified is just a base to create brand new netkans for not-yet-hosted mods. Eventually expanding the UI to allow editing existing metadata would be great, but is likely much more in-depth.

Primarily this is a web form which results in a JSON file that is sent in a PR to KSP-CKAN/NetKAN. Workflow is pretty heavily reliant on where a mod is hosted. Most fields are also optional.
Spacedock, github, and all other hosts (curse will be a kref-able source in the near future) are the current workflow determinants.


## Can I Try?

Yes, you can try a possibly outdated and maybe even broken version at https://brohlsoft.de/apps/metadata-webtool/


## Can I also run the current version at my Computer?

Yes
Install web-dependencies with bower, install python dependencies with `pip install -r requirements.txt` (in a virtual environment), start main.py and open http://localhost:8080/metadata-webtool/

