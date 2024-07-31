service_name  = 'solr'

proxy_external_url = 'https://xxx.xxx.xxx.xxx'

c.JupyterHub.services.append(
    {
        'name': service_name,
        'admin': True,
        'url': f'http://nbsearch-{service_name}-proxy',
        'oauth_client_id': f'service-{service_name}',
        'api_token': '0123456789ABCDEFGHIJKLMN',
        'oauth_redirect_uri': f'{proxy_external_url}/services/solr/oauth2/callback',
        'oauth_no_confirm': True,
    }
)
