import config
import pbclient

pbclient.set('endpoint', config.ENDPOINT)
pbclient.set('api_key', config.API_KEY)

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
app.info['sched'] = 'default'

pbclient.update_app(app)
