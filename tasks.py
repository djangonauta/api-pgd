#!/usr/bin/env python3

import invoke


@invoke.task(default=True)
def run(ctx, host='0.0.0.0', port=5057, reload=True):
    reload = ' --reload' if reload else ''
    cmd = f'source .env && python3 run_after_db.py "uvicorn api:app --host {host} --port {port}{reload}"'
    ctx.run(cmd, pty=True, echo=True)
