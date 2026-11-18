import json
from .catalog import offered
from .measurement import consumption, questionnaire
from .slate import next_slots


def run_workbench(action, directory, key, ledger):
    source = json.loads((directory / 'workbench.json').read_text())
    market = key or 'es'
    if market not in source['slots']:
        raise ValueError('未知市场')
    versions = offered(source['releases'], market, source['as_of'])
    if action == 'catalog':
        return versions
    scores = consumption(source['sessions'], versions)
    if action == 'scorecard':
        return {'playback': scores, 'survey': questionnaire(source['cohorts'], market)}
    return {'market': market, 'shortlist': next_slots(scores, source['slots'][market])}
