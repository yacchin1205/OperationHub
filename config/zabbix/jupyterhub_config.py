c.JupyterHub.services.append(
    {
        'name': 'zabbix',
        'admin': False,
        'url': f'http://zabbix-web-proxy/',
    }
)
