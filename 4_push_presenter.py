import config
import pbclient


pbclient.set('endpoint', config.ENDPOINT)
pbclient.set('api_key', config.API_KEY)


def push_presenter():
    html = open('presenter.html').read()

    # prepend categories to presenter
    cat_html = """
    <script type="text/javascript">
    window.LobbyFactsCategories = %s;
    </script>

    """ % open('categories.json').read()

    html = cat_html + html

    app = pbclient.find_app(short_name=config.APP)[0]

    app.info['task_presenter'] = html
    app.long_description = open('long-description.html').read().replace('%APP%', config.APP)
    app.info['sched'] = 'default'
    app.info['thumbnail'] = 'http://i46.tinypic.com/14js2tx.png'

    pbclient.update_app(app)


if __name__ == '__main__':
    push_presenter()
