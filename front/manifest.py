from manifesto import Manifest


class StaticManifest(Manifest):
    def cache(self):
        return ['/static/scripts.js', '/static/style.css', ]

    def network(self):
        return ['*']

    def fallback(self):
        return [('/', '/offline')]
