# info: http://askubuntu.com/questions/798708/how-to-fetch-build-packages-from-other-apt-repositories-in-snapcraft
import snapcraft
import os

class RepositoryPlugin(snapcraft.BasePlugin):
    @classmethod
    def schema(cls):
        return {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'type': 'object',
            'additionalProperties': False,
            'properties': {},
        }

    def enable_cross_compilation(self):
        pass

    @property
    def PLUGIN_STAGE_SOURCES(self):
        return open('snap/repository/sources.list', 'r').read()

