import i18n


errors = {
    'HTTPBadRequestException': {
        'message': i18n.t('errors.WA4000'),
        'status': 400,
        'code': 'WA4000'
    },
    'HTTPNotFoundException': {
        'message': i18n.t('errors.WA4004'),
        'status': 404,
        'code': 'WA4004'
    },
    'HTTPServerInternalException': {
        'message': i18n.t('errors.WA5000'),
        'status': 500,
        'code': 'WA5000'
    }
}