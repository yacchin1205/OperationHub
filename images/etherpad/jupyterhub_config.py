with open('/opt/etherpad.token', 'r') as f:
    token = f.read().strip()

service_name = 'etherpad'

c.JupyterHub.services.append(
    {
        'name': service_name,
        'oauth_client_id': f'service-{service_name}',
        'admin': True,
        'url': "http://etherpad-proxy",
        'api_token': token,
        'oauth_redirect_uri': 'https://my.server/services/etherpad/ep_oauth2/callback',
    }
)

c.JupyterHub.load_roles = [
    {
        'name': 'etherpad-user',
        'users': ['rocky'],
        'scopes': [f'access:services!service={service_name}', 'self'],
    },
]
