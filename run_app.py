import uvicorn

PORT = 8000
BIND = "127.0.0.1"
WORKERS = 10
RELOAD = True

if __name__ == "__main__":
    # config = {
    #     'version': 1, 'disable_existing_loggers': True,
    #     'formatters': {'default': {'()': 'uvicorn.logging.DefaultFormatter', 'fmt': '%(levelprefix)s %(message)s',
    #                                'use_colors': None},
    #                    'access': {'()': 'uvicorn.logging.AccessFormatter',
    #                               'fmt': '%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'}},
    #     'handlers': {
    #         'default': {'formatter': 'default', 'class': 'logging.StreamHandler', 'stream': 'ext://sys.stderr'},
    #         'access': {'formatter': 'access', 'class': 'logging.StreamHandler', 'stream': 'ext://sys.stdout'}},
    #     'loggers': {'uvicorn': {'handlers': ['default'], 'level': 'INFO'},
    #                 'uvicorn.error': {'level': 'INFO', 'handlers': ['default'], 'propagate': True},
    #                 'uvicorn.access': {'handlers': ['access'], 'level': 'INFO', 'propagate': False},
    #                 },
    # }
    # uvicorn.run("hello:app", host=BIND, port=int(PORT), reload=RELOAD, debug=RELOAD, workers=int(WORKERS))
    uvicorn.run("app.main:app", host=BIND, port=int(PORT), reload=RELOAD, debug=RELOAD, workers=int(WORKERS))

