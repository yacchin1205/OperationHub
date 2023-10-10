service_name  = 'zabbix'

c.JupyterHub.services.append(
    {
        'name': service_name,
        'admin': True,
        'url': f'http://zabbix-web-proxy',
    }
)
